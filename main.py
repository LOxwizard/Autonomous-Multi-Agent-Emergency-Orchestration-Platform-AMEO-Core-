import asyncio
from datetime import datetime
from config import DisasterEvent
from agents.simulator import SimulatorAgent
from agents.planner import PlannerAgent
from agents.broadcaster import BroadcasterAgent
from agents.responder import ResponderAgent

async def run_disaster_pipeline():
    print("==================================================================================")
    print("         AEGIS-NET: COMMAND & CONTROL AUTOMATED EMERGENCY ORCHESTRATOR           ")
    print("==================================================================================")
    
    print("\n[INPUT INGESTION] ENTER INCIDENT DATA:")
    disaster_type = input("  > Disaster Type (e.g., Earthquake, Cyclone, Flood): ").strip()
    
    try:
        metric_val = float(input("  > Severity Value (e.g., 6.8 for Richter, 140 for km/h): ").strip())
    except ValueError:
        metric_val = 5.0
        
    unit = input("  > Metric Unit (e.g., Richter Magnitude, km/h, meters): ").strip()
    location = input("  > Incident Location (e.g., Coastal Zone 4, Metro Sector 1): ").strip()

    event = DisasterEvent(
        disaster_type=disaster_type if disaster_type else "Earthquake",
        severity_metric=metric_val,
        unit=unit if unit else "Magnitude",
        location_name=location if location else "Sector 1"
    )

    simulator = SimulatorAgent()
    planner = PlannerAgent()
    broadcaster = BroadcasterAgent()
    responder = ResponderAgent()

    # PHASE 1: SIMULATOR TELEMETRY
    print("\n=================== PHASE 1: TELEMETRY & DAMAGE ASSESSMENT ===================")
    impact = simulator.evaluate_disaster(event)
    print(f"  LOCATION        : {impact['location']} (Grid Target: {impact['coordinates']})")
    print(f"  IMPACT SCORE    : {impact['severity_score']}")
    print(f"  DAMAGE RADIUS   : {impact['damage_radius_km']} km")
    print(f"  EST. POPULATION : {impact['estimated_affected_pop']:,} citizens at risk")
    await asyncio.sleep(0.4)

    # PHASE 2: TACTICAL PLANNING
    print("\n=================== PHASE 2: STRATEGIC ACTION DIRECTIVE ===================")
    plan = planner.generate_plan(impact)
    print("  PRIORITIZED RESPONSE PROTOCOLS:")
    for m in plan.priority_measures:
        print(f"    [{m['priority']}] {m['description']}")
        print(f"         └─ Allocated Assets: {m['assets']}")
    await asyncio.sleep(0.4)

    # PHASE 3: MULTI-CHANNEL PUBLIC BROADCAST
    print("\n=================== PHASE 3: MULTI-CHANNEL EMERGENCY DISPATCH ===================")
    await broadcaster.broadcast_alerts(plan)
    await asyncio.sleep(0.4)

    # PHASE 4: FIELD RESPONDER EXECUTION
    print("\n=================== PHASE 4: FIELD UNIT DEPLOYMENT TELEMETRY ===================")
    await responder.execute_assignments(plan.assigned_units)
    
    print("\n==================================================================================")
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] ALL AGENT WORKFLOWS EXECUTED SUCCESSFULLY.")
    print("==================================================================================")

if __name__ == "__main__":
    asyncio.run(run_disaster_pipeline())