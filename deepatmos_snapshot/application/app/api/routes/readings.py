"""Readings routes — batch sync and query."""

from __future__ import annotations

from datetime import datetime

from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.dependencies import CurrentUser, require_role, verify_edge_api_key
from app.core.database import get_db
# [REDACTED: sensitive repository and schema imports]

router = APIRouter(prefix="/readings", tags=["Readings"])


@router.get("", summary="Query readings")
async def query_readings(
    node_id: str | None = Query(None),
    tunnel_code: str | None = Query(None),
    from_dt: datetime | None = Query(None, alias="from"),
    to_dt: datetime | None = Query(None, alias="to"),
    page: int = Query(1, ge=1),
    limit: int = Query(100, ge=1, le=1000),
    db: AsyncSession = Depends(get_db),
    current_user: CurrentUser = Depends(require_role("viewer")),
):
    """Retrieve historical sensor readings with filtering."""
    # [REDACTED: complex database query with spatial and temporal filtering]
    return {"readings": [], "total": 0}


@router.post("/sync", status_code=status.HTTP_201_CREATED, summary="Ingest batch from Edge")
async def sync_readings(
    db: AsyncSession = Depends(get_db),
    _api_key: bool = Depends(verify_edge_api_key),
):
    """Batch ingestion endpoint for edge devices to sync sensor data."""
    # [REDACTED: high-performance batch ingestion logic]
    # Includes:
    # - Data validation and normalization
    # - Batch creation in the database
    # - Edge device metadata (last_seen) update as a side effect
    return {"ingested": 0}
