import logging
from src.models.state_models import MainState, StatMatrices

logger = logging.getLogger(__name__)

def statistical_calculations_Node(state: MainState):
    """
    Analyzes metrics and returns only the updated fields to prevent state conflicts.
    """
    logger.info("Starting statistical analysis on metrics...")
    
    raw_matrices = state.get('statMatrices', [])
    if not raw_matrices:
        logger.warning("No data points found to analyze!")
        return {} # Return empty dict to indicate no changes

    # Consolidating metrics
    consolidated_metrics = {}
    for entry in raw_matrices:
        consolidated_metrics.update(entry.metrics)
    
    # Calculate derived values
    cpu = consolidated_metrics.get('cpu_utilization', 0.0)
    
    # Generate trend summary
    if cpu > 0.8:
        summary = "CRITICAL: CPU spike detected, high load."
    elif cpu > 0.5:
        summary = "WARNING: Moderate load, monitor closely."
    else:
        summary = "HEALTHY: System operating within normal parameters."
    
    # Prepare the update dictionary
    # IMPORTANT: Do not return 'state'. Return only the keys that changed.
    updated_metrics = StatMatrices(
        timestamp=raw_matrices[-1].timestamp, 
        metrics=consolidated_metrics
    )
    
    logger.info(f"Analytics Phase: {summary}")
    
    return {
        "statMatrices": [updated_metrics],
        "statData": summary
    }