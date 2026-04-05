"""Alert model — immutable raw alert event linked to an incident."""

import enum
import uuid
from datetime import datetime

# [REDACTED: sensitive DB imports]

class AlertSeverity(enum.StrEnum):
    WARNING = "warning"
    CRITICAL = "critical"

class TriggerSource(enum.StrEnum):
    EXPERT_SYSTEM = "expert_system"
    GRU_MODEL = "gru_model"
    AUTOENCODER_MODEL = "autoencoder_model"

class Alert:
    """Represents a single hazard detection event."""
    __tablename__ = "alerts"

    id: str  # UUID
    node_id: str  # e.g., PJY-1-1-1
    timestamp: datetime
    severity: AlertSeverity
    trigger_source: TriggerSource
    trigger_reading: str  # JSON representation of the reading that fired the alert
    unsynced_readings_snapshot: str  # Contextual readings around the alert time
