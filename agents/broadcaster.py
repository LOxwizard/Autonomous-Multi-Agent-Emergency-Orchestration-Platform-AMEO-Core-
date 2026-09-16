import asyncio
import random
from datetime import datetime
from typing import List
from config import PlanOfAction, ChannelAlert

class BroadcasterAgent:
    """Dispatches distinct, protocol-specific alerts across public & tactical communication grids."""
    
    def generate_channel_messages(self, plan: PlanOfAction) -> List[ChannelAlert]:
        top_priority = plan.priority_measures[0]["description"] if plan.priority_measures else "Evacuate area immediately."
        
        alerts = [
            ChannelAlert(
                channel_name="CIVIL DEFENSE SIREN GRID",
                header="[SIREN SIGNAL: PATTERN ALPHA]",
                message=f"CONTINUOUS AUDIBLE ALARM ACTIVATED — {plan.disaster_type.upper()} IMMINENT.",
                severity_code="LEVEL-1 CRITICAL"
            ),
            ChannelAlert(
                channel_name="CELLULAR EMERGENCY BROADCAST (WEA)",
                header="[WEA ALERT - IMMEDIATE ACTION REQUIRED]",
                message=f"EMERGENCY: {plan.disaster_type.upper()} impacting area (Radius: {plan.damage_radius_km}km). {top_priority}",
                severity_code="CRITICAL ADVISORY"
            ),
            ChannelAlert(
                channel_name="NATIONAL EMERGENCY TV & RADIO (EAS)",
                header="[EAS BULLETIN BROADCAST]",
                message=f"The Civil Defense Command has issued an automated broadcast for {plan.disaster_type.upper()}. Mandatory Response Protocols: " +
                        "; ".join([f"({idx+1}) {m['description']}" for idx, m in enumerate(plan.priority_measures)]),
                severity_code="PUBLIC BROADCAST"
            ),
            ChannelAlert(
                channel_name="TACTICAL FIRST-RESPONDER ENCRYPTED LINK",
                header="[TACT-NET ENCRYPTED TELEMETRY]",
                message=f"COMMAND ORDER: Priority dispatch units initializing grid isolation for {plan.disaster_type.upper()}. Standby for asset deployment routes.",
                severity_code="TACTICAL DIRECTIVE"
            )
        ]
        return alerts

    async def broadcast_alerts(self, plan: PlanOfAction) -> None:
        alerts = self.generate_channel_messages(plan)
        print(f"\n[BROADCASTER COMMAND] Initializing multi-channel emergency message dispatch...")
        await asyncio.sleep(0.3)

        for alert in alerts:
            timestamp = datetime.now().strftime("%H:%M:%S")
            # Simulate high-reliability transmission per channel
            success = random.random() > 0.05
            status = "TRANSMITTED [100% REACH]" if success else "RETRYING ON SECURE BACKUP NODE"
            
            print(f"\n-------------------------------------------------------------------")
            print(f"[{timestamp}] CHANNEL: {alert.channel_name}")
            print(f"STATUS  : {status} | CODE: {alert.severity_code}")
            print(f"HEADER  : {alert.header}")
            print(f"PAYLOAD : {alert.message}")
            print(f"-------------------------------------------------------------------")
            await asyncio.sleep(0.2)