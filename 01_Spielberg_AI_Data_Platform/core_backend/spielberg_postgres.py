#!/usr/bin/env python3
"""
Spielberg MCP Postgres Server
Exposes tools to query Spielberg data from Postgres

Run: python -m mcp.server spielberg_postgres
Or: mcp run spielberg_postgres
"""

import json
import os
from datetime import datetime, date
from typing import Optional, Any
from contextlib import contextmanager

import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv

load_dotenv()

# Database configuration
DB_HOST = os.getenv("POSTGRES_HOST", "localhost")
DB_PORT = int(os.getenv("POSTGRES_PORT", "5432"))
DB_NAME = os.getenv("POSTGRES_DB", "spielberg")
DB_USER = os.getenv("POSTGRES_USER", "postgres")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD", "postgres")


@contextmanager
def get_db_cursor():
    """Context manager for database connections"""
    conn = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    cur = conn.cursor(cursor_factory=RealDictCursor)
    try:
        yield cur
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cur.close()
        conn.close()


def json_serializer(obj: Any) -> str:
    """JSON serializer for objects not serializable by default"""
    if isinstance(obj, (date, datetime)):
        return obj.isoformat()
    raise TypeError(f"Type {type(obj)} not serializable")


class SpielbergPostgresTools:
    """Collection of tools for Spielberg Postgres queries"""
    
    @staticmethod
    def list_projects(
        status: Optional[str] = None,
        client: Optional[str] = None,
        limit: int = 100,
        offset: int = 0
    ) -> dict:
        """
        List Altair projects with optional filters
        
        Args:
            status: Filter by project status (active, completed, upcoming)
            client: Filter by client name (case-insensitive substring match)
            limit: Number of results
            offset: Pagination offset
        
        Returns:
            List of projects with work codes and vendors
        """
        with get_db_cursor() as cur:
            where_clauses = []
            params = []
            
            if status:
                where_clauses.append("status = %s")
                params.append(status)
            
            if client:
                where_clauses.append("LOWER(client) LIKE LOWER(%s)")
                params.append(f"%{client}%")
            
            where_sql = " AND ".join(where_clauses) if where_clauses else "1=1"
            
            # Get projects
            query = f"""
                SELECT * FROM altair_projects
                WHERE {where_sql}
                ORDER BY start_date DESC
                LIMIT %s OFFSET %s
            """
            params.extend([limit, offset])
            cur.execute(query, params)
            projects = cur.fetchall()
            
            # Get total count
            count_query = f"SELECT COUNT(*) as total FROM altair_projects WHERE {where_sql}"
            cur.execute(count_query, params[:-2])
            total = cur.fetchone()["total"]
            
            # Enrich each project with work codes and vendors
            results = []
            for proj in projects:
                proj_dict = dict(proj)
                
                # Get work codes
                cur.execute(
                    "SELECT code, label, unit, rate FROM altair_project_work_codes WHERE project_id = %s",
                    [proj["project_id"]]
                )
                proj_dict["work_codes"] = [dict(row) for row in cur.fetchall()]
                
                # Get vendors
                cur.execute(
                    "SELECT vendor_type, role, days, rate FROM altair_project_vendors WHERE project_id = %s",
                    [proj["project_id"]]
                )
                proj_dict["vendors"] = [dict(row) for row in cur.fetchall()]
                
                results.append(proj_dict)
            
            return {
                "rows": results,
                "total": total,
                "limit": limit,
                "offset": offset
            }
    
    @staticmethod
    def get_project(bf_id: str) -> dict:
        """
        Get a single project by BF ID with all details
        
        Args:
            bf_id: Unique project identifier (e.g., BF-2026-252876)
        
        Returns:
            Project details including work codes, vendors, and timesheets
        """
        with get_db_cursor() as cur:
            cur.execute("SELECT * FROM altair_projects WHERE bf_id = %s", [bf_id])
            project = cur.fetchone()
            
            if not project:
                return {"error": f"Project {bf_id} not found"}
            
            proj_dict = dict(project)
            
            # Work codes
            cur.execute(
                "SELECT code, label, unit, rate FROM altair_project_work_codes WHERE project_id = %s",
                [project["project_id"]]
            )
            proj_dict["work_codes"] = [dict(row) for row in cur.fetchall()]
            
            # Vendors
            cur.execute(
                "SELECT vendor_type, role, days, rate FROM altair_project_vendors WHERE project_id = %s",
                [project["project_id"]]
            )
            proj_dict["vendors"] = [dict(row) for row in cur.fetchall()]
            
            # Timesheets
            cur.execute(
                """SELECT employee_key, date, work_code, hours, status 
                   FROM roar_timesheets 
                   WHERE bf_id = %s 
                   ORDER BY date DESC""",
                [bf_id]
            )
            proj_dict["timesheets"] = [dict(row) for row in cur.fetchall()]
            
            return proj_dict
    
    @staticmethod
    def list_timesheets(
        employee_key: Optional[str] = None,
        bf_id: Optional[str] = None,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        work_code: Optional[str] = None,
        limit: int = 100,
        offset: int = 0
    ) -> dict:
        """
        List ROAR timesheets with optional filters
        
        Args:
            employee_key: Filter by employee
            bf_id: Filter by project
            start_date: Filter from date (YYYY-MM-DD)
            end_date: Filter to date (YYYY-MM-DD)
            work_code: Filter by work code (CGI, PM, etc.)
            limit: Number of results
            offset: Pagination offset
        
        Returns:
            List of timesheet entries with statistics
        """
        with get_db_cursor() as cur:
            where_clauses = []
            params = []
            
            if employee_key:
                where_clauses.append("employee_key = %s")
                params.append(employee_key)
            
            if bf_id:
                where_clauses.append("bf_id = %s")
                params.append(bf_id)
            
            if start_date:
                where_clauses.append("date >= %s")
                params.append(start_date)
            
            if end_date:
                where_clauses.append("date <= %s")
                params.append(end_date)
            
            if work_code:
                where_clauses.append("work_code = %s")
                params.append(work_code)
            
            where_sql = " AND ".join(where_clauses) if where_clauses else "1=1"
            
            # Get timesheets
            query = f"""
                SELECT * FROM roar_timesheets
                WHERE {where_sql}
                ORDER BY date DESC
                LIMIT %s OFFSET %s
            """
            params.extend([limit, offset])
            cur.execute(query, params)
            timesheets = [dict(row) for row in cur.fetchall()]
            
            # Get total count and sum hours
            count_query = f"""
                SELECT COUNT(*) as total, COALESCE(SUM(hours), 0) as total_hours 
                FROM roar_timesheets 
                WHERE {where_sql}
            """
            cur.execute(count_query, params[:-2])
            stats = cur.fetchone()
            
            return {
                "rows": timesheets,
                "total": stats["total"],
                "total_hours": float(stats["total_hours"]),
                "limit": limit,
                "offset": offset
            }
    
    @staticmethod
    def list_people(
        department: Optional[str] = None,
        role: Optional[str] = None,
        contract_type: Optional[str] = None,
        search: Optional[str] = None,
        limit: int = 100,
        offset: int = 0
    ) -> dict:
        """
        List OneClick people with optional filters
        
        Args:
            department: Filter by department
            role: Filter by role
            contract_type: Filter by contract type (permanent, contractor, etc.)
            search: Search in employee_key, display_name, role
            limit: Number of results
            offset: Pagination offset
        
        Returns:
            List of people
        """
        with get_db_cursor() as cur:
            where_clauses = []
            params = []
            
            if department:
                where_clauses.append("department = %s")
                params.append(department)
            
            if role:
                where_clauses.append("LOWER(role) LIKE LOWER(%s)")
                params.append(f"%{role}%")
            
            if contract_type:
                where_clauses.append("contract_type = %s")
                params.append(contract_type)
            
            if search:
                where_clauses.append(
                    "(LOWER(employee_key) LIKE LOWER(%s) OR LOWER(display_name) LIKE LOWER(%s) OR LOWER(role) LIKE LOWER(%s))"
                )
                params.extend([f"%{search}%", f"%{search}%", f"%{search}%"])
            
            where_sql = " AND ".join(where_clauses) if where_clauses else "1=1"
            
            # Get people
            query = f"""
                SELECT * FROM oneclick_people
                WHERE {where_sql}
                ORDER BY employee_key
                LIMIT %s OFFSET %s
            """
            params.extend([limit, offset])
            cur.execute(query, params)
            people = [dict(row) for row in cur.fetchall()]
            
            # Get total count
            count_query = f"SELECT COUNT(*) as total FROM oneclick_people WHERE {where_sql}"
            cur.execute(count_query, params[:-2])
            total = cur.fetchone()["total"]
            
            return {
                "rows": people,
                "total": total,
                "limit": limit,
                "offset": offset
            }
    
    @staticmethod
    def list_absences(
        employee_key: Optional[str] = None,
        absence_type: Optional[str] = None,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        limit: int = 100,
        offset: int = 0
    ) -> dict:
        """
        List OneClick absences with optional filters
        
        Args:
            employee_key: Filter by employee
            absence_type: Filter by absence type (vacation, sick_leave, etc.)
            start_date: Filter from date (YYYY-MM-DD)
            end_date: Filter to date (YYYY-MM-DD)
            limit: Number of results
            offset: Pagination offset
        
        Returns:
            List of absence entries
        """
        with get_db_cursor() as cur:
            where_clauses = []
            params = []
            
            if employee_key:
                where_clauses.append("employee_key = %s")
                params.append(employee_key)
            
            if absence_type:
                where_clauses.append("type = %s")
                params.append(absence_type)
            
            if start_date:
                where_clauses.append("date >= %s")
                params.append(start_date)
            
            if end_date:
                where_clauses.append("date <= %s")
                params.append(end_date)
            
            where_sql = " AND ".join(where_clauses) if where_clauses else "1=1"
            
            # Get absences
            query = f"""
                SELECT * FROM oneclick_absences
                WHERE {where_sql}
                ORDER BY date DESC
                LIMIT %s OFFSET %s
            """
            params.extend([limit, offset])
            cur.execute(query, params)
            absences = [dict(row) for row in cur.fetchall()]
            
            # Get total count
            count_query = f"SELECT COUNT(*) as total FROM oneclick_absences WHERE {where_sql}"
            cur.execute(count_query, params[:-2])
            total = cur.fetchone()["total"]
            
            return {
                "rows": absences,
                "total": total,
                "limit": limit,
                "offset": offset
            }
    
    @staticmethod
    def get_person_details(employee_key: str) -> dict:
        """
        Get complete person profile with timesheets and absences
        
        Args:
            employee_key: Employee identifier
        
        Returns:
            Person details including timesheets and absences
        """
        with get_db_cursor() as cur:
            # Get person
            cur.execute("SELECT * FROM oneclick_people WHERE employee_key = %s", [employee_key])
            person = cur.fetchone()
            
            if not person:
                return {"error": f"Person {employee_key} not found"}
            
            person_dict = dict(person)
            
            # Get timesheets
            cur.execute(
                """SELECT date, bf_id, work_code, hours, status 
                   FROM roar_timesheets 
                   WHERE employee_key = %s 
                   ORDER BY date DESC 
                   LIMIT 100""",
                [employee_key]
            )
            person_dict["timesheets"] = [dict(row) for row in cur.fetchall()]
            
            # Get absences
            cur.execute(
                """SELECT date, type, status 
                   FROM oneclick_absences 
                   WHERE employee_key = %s 
                   ORDER BY date DESC 
                   LIMIT 100""",
                [employee_key]
            )
            person_dict["absences"] = [dict(row) for row in cur.fetchall()]
            
            return person_dict


# CLI for testing
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python spielberg_postgres.py <command> [args]")
        print("Commands:")
        print("  list-projects [--status STATUS] [--client CLIENT]")
        print("  get-project <bf_id>")
        print("  list-timesheets [--employee EMPLOYEE] [--bf-id BF_ID]")
        print("  list-people [--department DEPT] [--role ROLE]")
        print("  get-person <employee_key>")
        sys.exit(1)
    
    command = sys.argv[1]
    tools = SpielbergPostgresTools()
    
    try:
        if command == "list-projects":
            result = tools.list_projects()
        elif command == "get-project":
            result = tools.get_project(sys.argv[2])
        elif command == "list-timesheets":
            result = tools.list_timesheets()
        elif command == "list-people":
            result = tools.list_people()
        elif command == "get-person":
            result = tools.get_person_details(sys.argv[2])
        else:
            print(f"Unknown command: {command}")
            sys.exit(1)
        
        print(json.dumps(result, default=json_serializer, indent=2))
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
