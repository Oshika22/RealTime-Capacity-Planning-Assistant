import logging
from src.models.state_models import MainState

logger = logging.getLogger(__name__)

def decision_node(state: MainState):
    logger.info("Decision Phase: Analyzing Metrics + Context...")

    # 1. Extract the latest data from the lists
    # Since we use operator.add, we take the last element
    health = state["SystemHealth"][-1] if state["SystemHealth"] else None
    statData = state["statData"][-1] if state["statData"] else None
    context = state["context"][-1] if state["context"] else None
    
    # 2. Default Values
    decision = "MAINTAIN"
    reasoning = "Metrics stable and no significant business events detected."

    if not health:
        return {"decision": "MAINTAIN", "report": "Error: No health metrics available."}

    # 3. Decision Logic (The "SRE Brain")
    
    # Check for Critical System Metrics first (Safety First)
    if health.error_rate > 0.05 or health.response_time_ms > 500:
        decision = "SCALE_UP"
        reasoning = f"CRITICAL: High error rate ({health.error_rate}) or Latency ({health.response_time_ms}ms)."
    
    # Check Business Context
    elif context and context.suggested_action == "SCALE_UP":
        # If the LLM found a 'Flash Sale' or 'High Impact' event
        if context.impact_level in ["HIGH", "MODERATE"]:
            decision = "SCALE_UP"
            reasoning = f"PREEMPTIVE: {context.event_name} detected in {context.target_region}. {context.description}"
    
    # Check for Over-provisioning (Cost Optimization)
    elif health.qps < 100 and health.concurrency < 50:
        decision = "SCALE_DOWN"
        reasoning = "Low traffic detected. Scaling down to save costs."

    # 4. Generate the Final Report
    report = f"""
    ### SRE Automation Report
    **Final Decision:** {decision}
    **Reasoning:** {reasoning}
    
    **Metrics Evaluated:**
    * QPS: {health.qps}
    * Error Rate: {health.error_rate}
    * Concurrency: {health.concurrency}
    
    **Business Context:**
    * Event: {context.event_name if context else 'None'}
    * Impact: {context.impact_level if context else 'N/A'}
    """

    return {
        "decision": decision,
        "report": report
    }