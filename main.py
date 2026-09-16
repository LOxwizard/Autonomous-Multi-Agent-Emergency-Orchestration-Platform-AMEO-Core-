import asyncio
from config import DisasterEvent
from agents.simulator import SimulatorAgent
from agents.planner import PlannerAgent
from agents.broadcaster import BroadcasterAgent
from agents.responder import ResponderAgent

async def run_disaster_pipeline():
    print("===============================================================")
    print("       MULTI-AGENT EMERGENCY ORCHESTRATION SYSTEM             ")
    print("===============================================================")
    
    # User Inputs
    print("\n--- ENTER DISASTER SIMULATION DATA ---")
    disaster_type = input("Enter Disaster Type (e.g., Earthquake, Cyclone, Flood): ").strip()
    
    try:
        metric_val = float(input("Enter Severity Value (e.g., 4.5 for magnitude, 120 for wind speed in km/h): ").strip())
    except ValueError:
        print("Invalid number entered. Defaulting metric to 5.0")
        metric_val = 5.0
        
    unit = input("Enter Metric Unit (e.g., Magnitude, km/h, meters): ").strip()
    location = input("Enter Location / Zone (e.g., Sector 7, Coastal Zone A): ").strip()

    # Create Event Object
    event = DisasterEvent(
        disaster_type=disaster_type if disaster_type else "Earthquake",
        severity_metric=metric_val,
        unit=unit if unit else "Magnitude",
        location_name=location if location else "Zone 1"
    )

    # Initialize Agents
    simulator = SimulatorAgent()
    planner = PlannerAgent()
    broadcaster = BroadcasterAgent()
    responder = ResponderAgent(unit_id="Field-Unit-Alpha")

    # Pipeline Step 1: Simulator Assessment
    print("\n================ STEP 1: DAMAGE SIMULATION ================")
    impact_data = simulator.evaluate_disaster(event)
    await asyncio.sleep(0.5)

    # Pipeline Step 2: Planning & Strategy
    print("\n================ STEP 2: PLAN OF ACTION ================")
    plan = planner.generate_plan(impact_data)
    
    print(f"\nThreat Level Assessed: {plan.threat_level}")
    print("Prioritized Measures to Take:")
    for measure in plan.priority_measures:
        print(f"  {measure}")
    await asyncio.sleep(0.5)

    # Pipeline Step 3: Public Broadcaster
    print("\n================ STEP 3: PUBLIC ALERT BROADCAST ================")
    alert_msg = broadcaster.build_public_alert(plan)
    await broadcaster.broadcast_alerts(alert_msg)
    await asyncio.sleep(0.5)

    # Pipeline Step 4: Responder Field Execution
    print("\n================ STEP 4: FIELD OPERATIONAL EXECUTION ================")
    responder.execute_assignments(plan.assigned_routes)
    
    print("\n================ PROCESS COMPLETE ================")
    print("All dynamic agent workflows executed for review session.")

if __name__ == "__main__":
    asyncio.run(run_disaster_pipeline())