"""Node model — individual ESP32 devices."""

from __future__ import annotations

import enum
from datetime import datetime

from sqlalchemy import Boolean, DateTime, Enum, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class NodeStatus(enum.StrEnum):
    NORMAL = "normal"
    WARNING = "warning"
    CRITICAL = "critical"
    OFFLINE = "offline"
    DISABLED = "disabled"


class Node(Base):
    """Database model for an infrastructure node (sensor unit)."""
    __tablename__ = "nodes"

    id: Mapped[str] = mapped_column(String(50), primary_key=True)
    tunnel_code: Mapped[str] = mapped_column(
        String(20), ForeignKey("tunnels.code", ondelete="CASCADE"), nullable=False, index=True
    )
    # [REDACTED: sensitive spatial and identification fields]
    # Includes: kilometre, edge_id, node_number, latitude, longitude
    location_description: Mapped[str | None] = mapped_column(String(500), nullable=True)
    capabilities: Mapped[str | None] = mapped_column(Text, nullable=True)  # JSON logic description
    enabled: Mapped[bool] = mapped_column(Boolean, default=True)
    last_seen: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    status: Mapped[NodeStatus] = mapped_column(
        Enum(NodeStatus, native_enum=False, length=20), default=NodeStatus.NORMAL, nullable=False
    )

    # Relationships
    tunnel = relationship("Tunnel", back_populates="nodes")
    edge = relationship("Edge", back_populates="nodes")
