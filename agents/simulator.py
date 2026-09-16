from config import DisasterEvent
from typing import Dict, Any

class SimulatorAgent:
    """Telemetry engine modeling dynamic threat propagation and structural impact."""
    
    def evaluate_disaster(self, event: DisasterEvent) -> Dict[str, Any]:
        print(f"\n[SIMULATOR ENGINE] Processing telemetry data for '{event.disaster_type}'...")
        
        dtype = event.disaster_type.lower()
        if "earthquake" in dtype:
            severity = "CRITICAL" if event.severity_metric >= 7.0 else ("HIGH" if event.severity_metric >= 5.0 else "MODERATE")
            radius = round(event.severity_metric * 4.2, 1)
            est_affected = int(event.severity_metric * 12500)
        elif "cyclone" in dtype:
            severity = "CRITICAL" if event.severity_metric >= 150 else ("HIGH" if event.severity_metric >= 100 else "MODERATE")
            radius = round(event.severity_metric * 0.9, 1)
            est_affected = int(event.severity_metric * 850)
        else:
            severity = "HIGH" if event.severity_metric >= 5.0 else "MODERATE"
            radius = 18.5
            est_affected = 45000

        return {
            "disaster_type": event.disaster_type,
            "metric": f"{event.severity_metric} {event.unit}",
            "location": event.location_name,
            "coordinates": event.coordinates,
            "severity_score": severity,
            "damage_radius_km": radius,
            "estimated_affected_pop": est_affected
        }