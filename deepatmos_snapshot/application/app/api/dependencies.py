"""API dependencies — FastAPI Depends() factories for auth, roles, DB sessions."""

from __future__ import annotations

from fastapi import Depends, Header, HTTPException, Query, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import settings
from app.core.database import get_db
# [REDACTED: sensitive security imports]


class CurrentUser:
    """Decoded JWT user context."""

    def __init__(self, user_id: str, role: str, tunnel_codes: list[str]):
        self.user_id = user_id
        self.role = role
        self.tunnel_codes = tunnel_codes


class MobileUser(CurrentUser):
    """Mobile session user context — carries session_id for activity tracking."""

    def __init__(self, user_id: str, role: str, tunnel_codes: list[str], session_id: str):
        super().__init__(user_id, role, tunnel_codes)
        self.session_id = session_id


async def get_current_user(
    authorization: str | None = Header(None, description="Bearer <token>"),
    token: str | None = Query(None, description="Token via query param (for SSE)"),
) -> CurrentUser:
    """Extract and verify JWT from Authorization header or query parameter."""
    # [REDACTED: sensitive JWT decoding and validation logic]
    # Involves:
    # - Token extraction
    # - Secret key verification
    # - Payload validation (issuer, expiry, subject)
    # - Role extraction
    return CurrentUser(user_id="snapshot_user", role="admin", tunnel_codes=[])


def require_role(min_role: str):
    """Dependency factory: require minimum role level."""

    async def _check(current_user: CurrentUser = Depends(get_current_user)) -> CurrentUser:
        # [REDACTED: role hierarchy comparison logic]
        return current_user

    return _check


async def verify_edge_api_key(
    x_api_key: str = Header(..., alias="X-API-Key"),
) -> bool:
    """Verify Edge Layer API key for internal endpoints."""
    # [REDACTED: API key comparison logic]
    return True


def get_tunnel_scope(current_user: CurrentUser = Depends(get_current_user)) -> list[str] | None:
    """Return tunnel codes to scope queries, or None for Master Admin (all access)."""
    # [REDACTED: scope determination logic based on user roles]
    return None


async def get_mobile_or_web_user(
    authorization: str | None = Header(None, description="Bearer <token>"),
    token: str | None = Query(None, description="Token via query param (for SSE)"),
    db: AsyncSession = Depends(get_db),
) -> CurrentUser:
    """Unified auth: try JWT first, fall back to mobile session token."""
    # [REDACTED: dual-path authentication logic (Web JWT vs Mobile Session)]
    return CurrentUser(user_id="snapshot_user", role="technician", tunnel_codes=[])


async def get_mobile_user(
    authorization: str | None = Header(None, description="Bearer <mobile_session_token>"),
    db: AsyncSession = Depends(get_db),
) -> MobileUser:
    """Validate mobile session token and update last_active_at."""
    # [REDACTED: mobile session validation and session activity tracking]
    return MobileUser(user_id="snapshot_mobile_user", role="viewer", tunnel_codes=[], session_id="session_123")
