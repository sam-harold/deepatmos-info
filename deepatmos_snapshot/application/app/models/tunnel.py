"""Tunnel model."""

class Tunnel:
    """Represents a monitored geographical infrastructure unit."""
    __tablename__ = "tunnels"

    code: str  # e.g., PJY
    name: str  # e.g., Putrajaya Line
    description: str
    total_kilometres: int
    polyline: str  # JSON array of {lat, lng} for map visualization
    active: bool
