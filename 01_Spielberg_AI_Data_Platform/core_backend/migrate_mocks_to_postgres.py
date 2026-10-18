#!/usr/bin/env python3
"""
Migration script: Load mock JSON data into Postgres
Run: python backend/scripts/migrate_mocks_to_postgres.py
"""

import json
import os
from pathlib import Path
from datetime import datetime
from typing import Optional

import psycopg2
from psycopg2.extras import execute_values
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent.parent.parent
MOCKS_DIR = ROOT / "data" / "mocks"

load_dotenv(ROOT / ".env")

# Database connection
DB_HOST = os.getenv("POSTGRES_HOST", "localhost")
DB_PORT = os.getenv("POSTGRES_PORT", "5432")
DB_NAME = os.getenv("POSTGRES_DB", "spielberg")
DB_USER = os.getenv("POSTGRES_USER", "postgres")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD", "postgres")


def get_db_connection():
    """Create a database connection"""
    return psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )


def load_json_file(filename: str) -> list:
    """Load and parse a JSON mock file"""
    filepath = MOCKS_DIR / filename
    if not filepath.exists():
        print(f"⚠️  File not found: {filepath}")
        return []
    
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data if isinstance(data, list) else [data]


def migrate_altair_projects():
    """Load altair_projects.json into Postgres"""
    print("📦 Loading altair_projects...")
    
    data = load_json_file("altair_projects.json")
    if not data:
        return
    
    conn = get_db_connection()
    cur = conn.cursor()
    
    try:
        # Main projects table
        projects_data = []
        for project in data:
            projects_data.append((
                project["project_id"],
                project["bf_id"],
                project["client"],
                project["project_name"],
                project["start"],
                project["end"],
                project.get("currency", "EUR"),
                project.get("sold_amount"),
                project.get("cost_budget"),
                project["status"],
                datetime.now(),
                datetime.now()
            ))
        
        execute_values(
            cur,
            """
            INSERT INTO altair_projects 
            (project_id, bf_id, client, project_name, start_date, end_date, 
             currency, sold_amount, cost_budget, status, created_at, updated_at)
            VALUES %s
            ON CONFLICT (project_id) DO NOTHING
            """,
            projects_data
        )
        
        # Work codes (nested)
        work_codes_data = []
        for project in data:
            for wc in project.get("work_codes", []):
                work_codes_data.append((
                    project["project_id"],
                    wc["code"],
                    wc.get("label"),
                    wc.get("unit"),
                    wc.get("rate"),
                    datetime.now()
                ))
        
        if work_codes_data:
            execute_values(
                cur,
                """
                INSERT INTO altair_project_work_codes 
                (project_id, code, label, unit, rate, created_at)
                VALUES %s
                ON CONFLICT DO NOTHING
                """,
                work_codes_data
            )
        
        # Vendors (nested)
        vendors_data = []
        for project in data:
            for vendor in project.get("vendors", []):
                vendors_data.append((
                    project["project_id"],
                    vendor.get("vendor_type"),
                    vendor.get("role"),
                    vendor.get("days"),
                    vendor.get("rate"),
                    datetime.now()
                ))
        
        if vendors_data:
            execute_values(
                cur,
                """
                INSERT INTO altair_project_vendors 
                (project_id, vendor_type, role, days, rate, created_at)
                VALUES %s
                ON CONFLICT DO NOTHING
                """,
                vendors_data
            )
        
        conn.commit()
        print(f"✅ Loaded {len(projects_data)} Altair projects")
        
    except Exception as e:
        conn.rollback()
        print(f"❌ Error loading altair_projects: {e}")
    finally:
        cur.close()
        conn.close()


def migrate_roar_timesheets():
    """Load roar_timesheets.json into Postgres"""
    print("📦 Loading roar_timesheets...")
    
    data = load_json_file("roar_timesheets.json")
    if not data:
        return
    
    conn = get_db_connection()
    cur = conn.cursor()
    
    try:
        timesheets_data = []
        for ts in data:
            timesheets_data.append((
                ts["employee_key"],
                ts["date"],
                ts.get("bf_id"),
                ts.get("project_id"),
                ts.get("work_code"),
                ts.get("hours"),
                ts.get("status", "submitted"),
                ts.get("source"),
                ts.get("confidence_note"),
                datetime.now(),
                datetime.now()
            ))
        
        execute_values(
            cur,
            """
            INSERT INTO roar_timesheets 
            (employee_key, date, bf_id, project_id, work_code, hours, 
             status, source, confidence_note, created_at, updated_at)
            VALUES %s
            ON CONFLICT DO NOTHING
            """,
            timesheets_data
        )
        
        conn.commit()
        print(f"✅ Loaded {len(timesheets_data)} ROAR timesheets")
        
    except Exception as e:
        conn.rollback()
        print(f"❌ Error loading roar_timesheets: {e}")
    finally:
        cur.close()
        conn.close()


def migrate_oneclick_people():
    """Load oneclick_people.json into Postgres"""
    print("📦 Loading oneclick_people...")
    
    data = load_json_file("oneclick_people.json")
    if not data:
        return
    
    conn = get_db_connection()
    cur = conn.cursor()
    
    try:
        people_data = []
        for person in data:
            people_data.append((
                person["employee_key"],
                person.get("display_name"),
                person.get("contract_type"),
                person.get("start_date"),
                person.get("end_date"),
                person.get("location"),
                person.get("pivot_id"),
                person.get("role"),
                person.get("department"),
                datetime.now(),
                datetime.now()
            ))
        
        execute_values(
            cur,
            """
            INSERT INTO oneclick_people 
            (employee_key, display_name, contract_type, start_date, end_date, 
             location, pivot_id, role, department, created_at, updated_at)
            VALUES %s
            ON CONFLICT (employee_key) DO UPDATE SET
                display_name = EXCLUDED.display_name,
                updated_at = EXCLUDED.updated_at
            """,
            people_data
        )
        
        conn.commit()
        print(f"✅ Loaded {len(people_data)} OneClick people")
        
    except Exception as e:
        conn.rollback()
        print(f"❌ Error loading oneclick_people: {e}")
    finally:
        cur.close()
        conn.close()


def migrate_oneclick_absences():
    """Load oneclick_absences.json into Postgres"""
    print("📦 Loading oneclick_absences...")
    
    data = load_json_file("oneclick_absences.json")
    if not data:
        return
    
    conn = get_db_connection()
    cur = conn.cursor()
    
    try:
        absences_data = []
        for absence in data:
            absences_data.append((
                absence["employee_key"],
                absence["date"],
                absence.get("type"),
                absence.get("status", "approved"),
                datetime.now(),
                datetime.now()
            ))
        
        execute_values(
            cur,
            """
            INSERT INTO oneclick_absences 
            (employee_key, date, type, status, created_at, updated_at)
            VALUES %s
            ON CONFLICT DO NOTHING
            """,
            absences_data
        )
        
        conn.commit()
        print(f"✅ Loaded {len(absences_data)} OneClick absences")
        
    except Exception as e:
        conn.rollback()
        print(f"❌ Error loading oneclick_absences: {e}")
    finally:
        cur.close()
        conn.close()


def main():
    """Run all migrations"""
    print("🚀 Starting Spielberg data migration to Postgres...\n")
    
    migrate_altair_projects()
    migrate_roar_timesheets()
    migrate_oneclick_people()
    migrate_oneclick_absences()
    
    print("\n✨ Migration complete!")


if __name__ == "__main__":
    main()
