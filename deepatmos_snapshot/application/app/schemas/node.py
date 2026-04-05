"""Node schemas."""

from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel

from app.models.node import NodeStatus


class NodeCapabilities(BaseModel):
    """Schema for hardware capabilities of a node."""
    # [REDACTED: specific hardware sensor flags]
    has_dht22: bool = False
    has_mq_array: bool = False
    has_pms5003: bool = False


class NodeCreate(BaseModel):
    """Schema for creating a new node."""
    tunnel_code: str
    # [REDACTED: sensitive spatial fields]
    location_description: str | None = None
    capabilities: NodeCapabilities = NodeCapabilities()


class NodeUpdate(BaseModel):
    """Schema for updating an existing node."""
    location_description: str | None = None
    capabilities: NodeCapabilities | None = None


class NodeResponse(BaseModel):
    """API response schema for node details."""
    id: str
    tunnel_code: str
    # [REDACTED: sensitive spatial fields]
    location_description: str | None = None
    capabilities: NodeCapabilities = NodeCapabilities()
    enabled: bool
    last_seen: datetime | None = None
    status: NodeStatus

    model_config = {"from_attributes": True}


class NodeMapItem(BaseModel):
    """Optimized schema for map rendering."""
    id: str
    # [REDACTED: sensitive identification fields]
    latitude: float | None = None
    longitude: float | None = None
    status: NodeStatus
    alert_severity: str | None = None
