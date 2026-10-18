"""
Services pour utiliser le MCP Postgres dans FastAPI

Remplace les chargements de JSON en mémoire par des requêtes Postgres
"""

from typing import Optional, Dict, Any, List
from .integrations.spielberg_postgres import SpielbergPostgresTools


class SpielbergDataService:
    """Service wrapper pour accéder aux données via MCP Postgres"""
    
    def __init__(self):
        self.tools = SpielbergPostgresTools()
    
    # ========================================================================
    # ALTAIR PROJECTS
    # ========================================================================
    
    def list_altair_projects(
        self,
        status: Optional[str] = None,
        client: Optional[str] = None,
        limit: int = 100,
        offset: int = 0
    ) -> Dict[str, Any]:
        """
        List Altair projects (remplace load_altair_projects + mocks)
        
        Utilisation dans main.py :
            @app.get("/api/altair/projects")
            def api_altair_projects(status: Optional[str] = None, client: Optional[str] = None):
                service = SpielbergDataService()
                return service.list_altair_projects(status=status, client=client)
        """
        return self.tools.list_projects(status=status, client=client, limit=limit, offset=offset)
    
    def get_altair_project(self, bf_id: str) -> Dict[str, Any]:
        """Get a single Altair project with all details"""
        return self.tools.get_project(bf_id)
    
    # ========================================================================
    # ROAR TIMESHEETS
    # ========================================================================
    
    def list_roar_timesheets(
        self,
        employee_key: Optional[str] = None,
        bf_id: Optional[str] = None,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        work_code: Optional[str] = None,
        limit: int = 100
    ) -> Dict[str, Any]:
        """
        List ROAR timesheets (remplace load_roar_timesheets + mocks)
        
        Utilisation dans main.py :
            @app.get("/api/roar/timesheets")
            def api_roar_timesheets(employee: Optional[str] = None):
                service = SpielbergDataService()
                return service.list_roar_timesheets(employee_key=employee)
        """
        return self.tools.list_timesheets(
            employee_key=employee_key,
            bf_id=bf_id,
            start_date=start_date,
            end_date=end_date,
            work_code=work_code,
            limit=limit
        )
    
    # ========================================================================
    # ONECLICK PEOPLE
    # ========================================================================
    
    def list_oneclick_people(
        self,
        department: Optional[str] = None,
        role: Optional[str] = None,
        search: Optional[str] = None,
        limit: int = 100
    ) -> Dict[str, Any]:
        """
        List OneClick people (remplace load_oneclick_people + mocks)
        
        Utilisation dans main.py :
            @app.get("/api/people")
            def api_people(department: Optional[str] = None):
                service = SpielbergDataService()
                return service.list_oneclick_people(department=department)
        """
        return self.tools.list_people(
            department=department,
            role=role,
            search=search,
            limit=limit
        )
    
    def get_oneclick_person(self, employee_key: str) -> Dict[str, Any]:
        """Get complete person profile with timesheets and absences"""
        return self.tools.get_person_details(employee_key)
    
    # ========================================================================
    # ONECLICK ABSENCES
    # ========================================================================
    
    def list_oneclick_absences(
        self,
        employee_key: Optional[str] = None,
        absence_type: Optional[str] = None,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        limit: int = 100
    ) -> Dict[str, Any]:
        """
        List OneClick absences (remplace load_oneclick_absences + mocks)
        
        Utilisation dans main.py :
            @app.get("/api/oneclick/absences")
            def api_oneclick_absences(employee: Optional[str] = None):
                service = SpielbergDataService()
                return service.list_oneclick_absences(employee_key=employee)
        """
        return self.tools.list_absences(
            employee_key=employee_key,
            absence_type=absence_type,
            start_date=start_date,
            end_date=end_date,
            limit=limit
        )


# Instance globale (pattern singleton)
_data_service: Optional[SpielbergDataService] = None


def get_data_service() -> SpielbergDataService:
    """Get or create the singleton data service"""
    global _data_service
    if _data_service is None:
        _data_service = SpielbergDataService()
    return _data_service
