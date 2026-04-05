"""Reading model — historical sensor data from Edge Layer batch sync."""

import uuid
from datetime import datetime

class Reading:
    """Represents a single sensor measurement point."""
    __tablename__ = "readings"

    id: str
    node_id: str
    timestamp: datetime
    
    # 9-metric sensor array
    temperature: float
    humidity: float
    carbon_dioxide: float
    carbon_monoxide: float
    methane: float
    oxygen: float
    pm2_5: float
    pm10: float
    aqi: int
