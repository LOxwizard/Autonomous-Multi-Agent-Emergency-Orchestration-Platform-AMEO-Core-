from dataclasses import dataclass, field
from typing import List, Dict, Any

@dataclass
class DisasterEvent:
    disaster_type: str
    severity_metric: float
    unit: str
    location_name: str
    coordinates: Dict[str, int] = field(default_factory=lambda: {"x": 12, "y": 45})

@dataclass
class PlanOfAction:
    disaster_type: str
    threat_level: str
    damage_radius_km: float
    priority_measures: List[Dict[str, Any]]
    assigned_units: List[Dict[str, Any]]

@dataclass
class ChannelAlert:
    channel_name: str
    header: str
    message: str
    severity_code: str