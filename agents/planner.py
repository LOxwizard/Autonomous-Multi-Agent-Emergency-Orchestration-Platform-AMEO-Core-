from typing import Dict, Any, List
from config import PlanOfAction

class PlannerAgent:
    """Tactical orchestration engine computing dynamic triage priorities and unit routes."""
    
    def generate_plan(self, impact_data: Dict[str, Any]) -> PlanOfAction:
        print(f"\n[TACTICAL PLANNER] Synthesizing command directives for threat level: {impact_data['severity_score']}...")
        
        disaster_type = impact_data["disaster_type"].lower()
        
        if "earthquake" in disaster_type:
            measures = [
                {"priority": "P1", "description": "Deploy heavy USAR (Urban Search & Rescue) to collapsed structures.", "assets": "K9 Units, Acoustic Sensors"},
                {"priority": "P2", "description": "Isolate natural gas mainlines at distribution substations to prevent fire breakout.", "assets": "Automated Shutoff Valves"},
                {"priority": "P3", "description": "Establish Mobile Triage units at safe perimeter coordinates.", "assets": "Field Hospitals, Ambulances"}
            ]
        elif "cyclone" in disaster_type:
            measures = [
                {"priority": "P1", "description": "Execute mandatory evacuation protocol for low-lying coastal surge sectors.", "assets": "Transport Busses, Air-Siren Arrays"},
                {"priority": "P2", "description": "Clear primary arterial evacuation corridors of debris and fallen high-voltage lines.", "assets": "Heavy Machinery Teams"},
                {"priority": "P3", "description": "Stage emergency diesel generators at municipal hospitals and water treatment plants.", "assets": "Logistics Fleets"}
            ]
        else:
            measures = [
                {"priority": "P1", "description": "Deploy rapid-response swiftwater rescue craft to trapped residential sectors.", "assets": "Zodiac Boats, Helicopter Hoists"},
                {"priority": "P2", "description": "Construct high-capacity water diversion barriers around power grid hubs.", "assets": "Sandbag Deployers"},
                {"priority": "P3", "description": "Distribute emergency survival rations and medical supplies to high-ground shelters.", "assets": "Supply Drones"}
            ]

        units = [
            {"unit_id": "RESCUE-ALPHA", "objective": "Sector 4 Triage Grid", "status": "DISPATCHED", "eta": "8 Mins"},
            {"unit_id": "LOGISTICS-BETA", "objective": "Evacuation Route Corridor B", "status": "EN ROUTE", "eta": "14 Mins"},
            {"unit_id": "HAZMAT-DELTA", "objective": "Utility Isolation Point 2", "status": "STAGED", "eta": "3 Mins"}
        ]

        return PlanOfAction(
            disaster_type=impact_data["disaster_type"],
            threat_level=impact_data["severity_score"],
            damage_radius_km=impact_data["damage_radius_km"],
            priority_measures=measures,
            assigned_units=units
        )