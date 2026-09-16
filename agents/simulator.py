from config import DisasterEvent
from typing import Dict, Any

class SimulatorAgent:
    """Evaluates disaster input, calculates damage radius/severity, and models environmental impact."""
    
    def evaluate_disaster(self, event: DisasterEvent) -> Dict[str, Any]:
        print(f"\n[Simulator] Processing disaster impact for '{event.disaster_type}'...")
        
        # Calculate severity index based on type and input metric
        severity_score = "LOW"
        damage_radius_km = 5
        
        dtype = event.disaster_type.lower()
        if "earthquake" in dtype:
            if event.severity_metric >= 7.0: severity_score = "CRITICAL"
            elif event.severity_metric >= 5.0: severity_score = "HIGH"
            else: severity_score = "MODERATE"
            damage_radius_km = round(event.severity_metric * 3.5, 1)
            
        elif "cyclone" in dtype:
            if event.severity_metric >= 150: severity_score = "CRITICAL"
            elif event.severity_metric >= 100: severity_score = "HIGH"
            else: severity_score = "MODERATE"
            damage_radius_km = round(event.severity_metric * 0.8, 1)
            
        else: # Default/Flood/Other
            if event.severity_metric >= 5.0: severity_score = "HIGH"
            else: severity_score = "MODERATE"
            damage_radius_km = 15.0

        print(f"[Simulator] Impact Assessment Complete | Severity Level: {severity_score} | Radius: {damage_radius_km} km")
        
        return {
            "disaster_type": event.disaster_type,
            "metric": f"{event.severity_metric} {event.unit}",
            "location": event.location_name,
            "severity_score": severity_score,
            "damage_radius_km": damage_radius_km
        }