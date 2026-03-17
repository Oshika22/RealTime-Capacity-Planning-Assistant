import logging
import json
from src.models.state_models import MainState, SystemHealth

logger = logging.getLogger(__name__)

# derived from the formulas and std matrics from gfg : https://www.geeksforgeeks.org/system-design/capacity-estimation-in-systems-design/
def derive_health_metrics(raw_data: str) -> SystemHealth:
    """
    Parses Prometheus JSON to calculate dynamic metrics.
    """
    data = json.loads(raw_data)
    results = data.get('data', {}).get('result', [])
    
    # Example logic: Totaling process_count to derive a fake 'concurrency'
    # In a real SRE scenario, you would perform PromQL-like calculations here
    total_processes = 0
    for item in results:
        metric_name = item.get('metric', {}).get('__name__', '')
        val = float(item.get('values', [[0, 0]])[0][1])
        
        if metric_name == 'process_count':
            total_processes += val
            
    # Dynamic calculation simulation
    return SystemHealth(
        dau=int(total_processes * 100),       # Scaled based on process count
        qps=float(total_processes * 10.5),    # Derived load
        error_rate=0.01 if total_processes < 200 else 0.08, # High process = higher risk
        response_time_ms=50.0 + (total_processes * 0.5),
        storage_used_gb=10.0,
        concurrency=int(total_processes)
    )

def system_health_node(state: MainState):
    logger.info("Analyzing System Health (Dynamic Calculation Path)...")
    
    raw_data = state.get('jsonFile')
    if not raw_data:
        return {}

    # Calculate metrics dynamically
    health_metrics = derive_health_metrics(raw_data)
    
    return {"SystemHealth": [health_metrics]}