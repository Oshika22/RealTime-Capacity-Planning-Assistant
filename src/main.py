import logging
import sys
import os

# Add the project root to sys.path so imports work flawlessly
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.models.state_models import MainState
from src.nodes.extraction_node import Meta_data_extraction_Node
from src.nodes.analytics_node import statistical_calculations_Node
from src.graph import create_workflow

# Setup professional logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

def run_pipeline():
    # 1. Mocking the Prometheus JSON response
    mock_prometheus_json = """
    {
        "status": "success",
        "data": {
            "result": [
                {"metric": {"__name__": "cpu_utilization", "instance": "web-server-01"}, "values": [[1741671000, "0.85"]]},
                {"metric": {"__name__": "memory_usage", "instance": "web-server-01"}, "values": [[1741671000, "4096.0"]]},
                {"metric": {"__name__": "temperature", "instance": "web-server-01"}, "values": [[1741671000, "65.5"]]},
                {"metric": {"__name__": "process_count", "instance": "web-server-01"}, "values": [[1741671000, "120.0"]]}
            ]
        }
    }
    """

    # 2. Initializing State
    state: MainState = {
        "category": "ecommerce",
        "jsonFile": mock_prometheus_json,
        "metaData": None,
        "statMatrices": [],
        "statData": "",
        "context": [],
        "decision": "Pending",
        "report": ""
    }

    app = create_workflow()
    
    # Run karo
    final_state = app.invoke(state)
    print("decision", final_state['decision'])

if __name__ == "__main__":
    run_pipeline()