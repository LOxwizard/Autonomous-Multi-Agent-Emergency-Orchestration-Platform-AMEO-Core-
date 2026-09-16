from dataclasses import dataclass, field
from typing import List, Dict, Any

@dataclass
class DisasterEvent:
    disaster_type: str        # e.g., "Earthquake", "Cyclone", "Flood"
    severity_metric: float    # e.g., 4.5 for Richter magnitude, 120 for wind speed (km/h)
    unit: str                 # e.g., "Magnitude", "km/h", "meters"
    location_name: str        # e.g., "Visakhapatnam Zone 2"

@dataclass
class PlanOfAction:
    disaster_type: str
    threat_level: str
    priority_measures: List[str]
    assigned_routes: List[Dict[str, Any]]

@dataclass
class AlertMessage:
    channel: str              # e.g., "Cell Broadcast", "Radio", "Siren Grid"
    alert_level: str          # e.g., "CRITICAL", "WARNING", "ADVISORY"
    public_instruction: str