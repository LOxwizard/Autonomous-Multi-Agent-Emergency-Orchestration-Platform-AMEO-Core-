from typing import Dict, Any, List
from config import PlanOfAction

class PlannerAgent:
    """Generates prioritized strategic actions and deployment plans based on simulator assessment."""
    
    def generate_plan(self, impact_data: Dict[str, Any]) -> PlanOfAction:
        print(f"\n[Planner] Computing optimal Plan of Action for threat level: {impact_data['severity_score']}...")
        
        disaster_type = impact_data["disaster_type"].lower()
        severity = impact_data["severity_score"]
        
        priorities = []
        
        # Determine dynamic priorities based on disaster profile
        if "earthquake" in disaster_type:
            priorities = [
                "1. Immediate structural triage and heavy search & rescue in collapsed collapse zones.",
                "2. Shut down gas supply mainlines to prevent secondary urban fires.",
                "3. Deploy mobile medical field units to target coordinates."
            ]
        elif "cyclone" in disaster_type:
            priorities = [
                "1. Mandatory evacuation of coastal and low-lying storm surge areas.",
                "2. Clear main arterial roads of fallen debris/trees for emergency vehicles.",
                "3. Distribute emergency power backup generators to local hospitals."
            ]
        else:
            priorities = [
                "1. Deploy water extraction pumps and inflatable rescue boats.",
                "2. Move trapped populations to high-ground shelters.",
                "3. Deliver clean drinking water packets to prevent waterborne disease."
            ]

        if severity == "CRITICAL":
            priorities.insert(0, "0. [URGENT] Request national disaster relief reinforcements.")

        routes = [
            {"unit": "Alpha-1", "objective": "Sector 4 Triage Point", "status": "Dispatched"},
            {"unit": "Beta-2", "objective": "Evacuation Center Hub", "status": "En Route"}
        ]

        return PlanOfAction(
            disaster_type=impact_data["disaster_type"],
            threat_level=severity,
            priority_measures=priorities,
            assigned_routes=routes
        )