from langgraph.graph import StateGraph, END
from src.models.state_models import MainState
from src.nodes.extraction_node import Meta_data_extraction_Node
from src.nodes.analytics_node import statistical_calculations_Node
from src.nodes.system_health_node import system_health_node
from src.nodes.context_node import context_node
from src.nodes.decision_node import decision_node            # Jo hum banane wale hain

def create_workflow():
    workflow = StateGraph(MainState)

    # Nodes define karo
    workflow.add_node("extraction", Meta_data_extraction_Node)
    workflow.add_node("analytics", statistical_calculations_Node)
    workflow.add_node("health", system_health_node)
    workflow.add_node("context", context_node)
    workflow.add_node("decision", decision_node)

    # Entry point
    workflow.set_entry_point("extraction")

    # Parallel Flow (Extraction -> Analytics & Health)
    workflow.add_edge("extraction", "analytics")
    workflow.add_edge("extraction", "health")
    workflow.add_edge("extraction", "context")

    # Join Point (Analytics & Health -> Decision)
    workflow.add_edge("analytics", "decision")
    workflow.add_edge("health", "decision")
    workflow.add_edge("context", "decision")

    # End
    workflow.add_edge("decision", END)

    return workflow.compile()