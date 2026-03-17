import json
import logging
from src.models.state_models import MainState, MetaData, StatMatrices

logger = logging.getLogger(__name__)

def Meta_data_extraction_Node(state: MainState) -> MainState:
    """
    Parses raw Prometheus JSON and ensures all state keys are populated.
    """
    try:
        raw_data = json.loads(state['jsonFile'])
        results = raw_data.get('data', {}).get('result', [])
        
        if not results:
            logger.error("No metrics found in Prometheus JSON!")
            return state

        # 1. Extract MetaData from the first result
        metric_info = results[0].get('metric', {})
        meta_data = MetaData(
            metric_name=metric_info.get('__name__', 'unknown'),
            instance=metric_info.get('instance', 'unknown'),
            job=metric_info.get('job', 'unknown'),
            labels=metric_info
        )

        # 2. Extract Values into StatMatrices
        stat_matrices = []
        for item in results:
            metric_name = item.get('metric', {}).get('__name__', 'value')
            # Extract the second element of the list [timestamp, value]
            value = float(item.get('values', [['0', '0']])[0][1])
            timestamp = int(item.get('values', [[0, 0]])[0][0])
            
            stat_matrices.append(StatMatrices(
                timestamp=timestamp,
                metrics={metric_name: value}
            ))

        # 3. Explicitly update the dictionary keys
        state['metaData'] = meta_data
        state['statMatrices'] = stat_matrices
        
        logger.info(f"Successfully extracted {len(stat_matrices)} data points for {meta_data.instance}")
        return state

    except Exception as e:
        logger.error(f"Extraction failed: {str(e)}")
        raise e