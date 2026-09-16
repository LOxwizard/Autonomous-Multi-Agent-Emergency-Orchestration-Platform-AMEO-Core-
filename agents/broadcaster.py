import asyncio
import random
from config import PlanOfAction, AlertMessage

class BroadcasterAgent:
    """Formats and transmits emergency alerts across public alert infrastructure."""
    
    def build_public_alert(self, plan: PlanOfAction) -> AlertMessage:
        level = "EMERGENCY BROADCAST" if plan.threat_level in ["HIGH", "CRITICAL"] else "PUBLIC ADVISORY"
        
        instructions = f"Take immediate precautions for {plan.disaster_type}. Priority Action: {plan.priority_measures[0]}"
        
        return AlertMessage(
            channel="Multi-Channel Emergency Alert System (Cell, Siren, Radio)",
            alert_level=level,
            public_instruction=instructions
        )

    async def broadcast_alerts(self, alert: AlertMessage) -> None:
        print(f"\n[Broadcaster] Preparing emergency broadcast dispatch across network nodes...")
        await asyncio.sleep(0.3)
        
        channels = ["Cellular Emergency Broadcast Network", "Local Radio FM 93.5 & TV Networks", "Public Siren Systems"]
        
        for ch in channels:
            # Simulate network transmission status
            success = random.random() > 0.05  # 95% delivery rate
            status = "DELIVERED TO PUBLIC" if success else "RETRYING TRANSMISSION"
            print(f"[Broadcaster -> {ch}] Status: {status}")
            print(f"   >>> ALERT TEXT: [{alert.alert_level}] {alert.public_instruction}")
            await asyncio.sleep(0.2)