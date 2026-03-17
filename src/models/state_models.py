from typing import List, Dict, Optional, TypedDict, Annotated
import operator
from pydantic import BaseModel, Field

class StatMatrices(BaseModel):
    timestamp: int
    # We use a dict to hold all metrics from your dataset 
    # (cpu_utilization, memory_usage, temperature, etc.)
    metrics: Dict[str, float] = Field(
        default_factory=dict, 
        description="Key-value pairs of all extracted metrics"
    )

class MetaData(BaseModel):
    metric_name: str = Field(description="Primary metric identifier")
    instance: str = Field(description="The server instance ID")
    job: str = Field(description="The job name")
    # For extra Prometheus labels like 'mode', 'device', 'mountpoint'
    labels: Dict[str, str] = Field(default_factory=dict)

class SystemHealth(BaseModel):
    dau: int = 0
    qps: float = 0.0
    storage_used_gb: float = 0.0
    error_rate: float = 0.0
    response_time_ms: float = 0.0
    concurrency: int = 0


from pydantic import BaseModel, Field

class Context(BaseModel):
    event_name: str = Field(description="The specific event or reason (e.g., 'Result Day', 'Flash Sale') that will impact infrastructure load.")
    target_region: str = Field(description="The geographical region affected (e.g., 'INDIA', 'GLOBAL', 'APAC'). Scaling only triggers if this matches our server region.")
    impact_level: str = Field(description="Expected impact severity: 'LOW', 'MODERATE', or 'HIGH'.")
    suggested_action: str = Field(description="The recommended may be required scaling action: 'SCALE_UP', 'SCALE_DOWN', or 'MAINTAIN_CURRENT'.")
  

    
class MainState(TypedDict):
    category: str 
    jsonFile: str          # Raw Prometheus JSON input
    metaData: MetaData      # Extracted labels and server info
    statMatrices: Annotated[List[StatMatrices], operator.add]  # Time-series list of all metrics
    statData: str          # Trend analysis (e.g., "CPU increasing, Temp stable")
    SystemHealth: Annotated[List[SystemHealth], operator.add]
    context: Annotated[List[Context], operator.add]     # External business context (Tavily search result)
    decision: str          # Final scaling action (Scale Up/Down/None)
    report: str            # Final Markdown summary for the SRE team