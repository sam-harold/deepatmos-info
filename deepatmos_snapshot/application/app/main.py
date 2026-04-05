"""DeepAtmos Application Layer — FastAPI entry point."""

from __future__ import annotations

import json
import logging
from contextlib import asynccontextmanager
from datetime import UTC, datetime

from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware

from app.core.config import settings
from app.core.database import Base, async_session_factory, engine

logger = logging.getLogger(__name__)


def _parse_alert_timestamp(value: str | None) -> datetime:
    """Parse incoming alert timestamp safely, defaulting to current UTC time."""
    # [REDACTED: sensitive processing logic]
    return datetime.now(UTC)


def _severity_rank(severity_value: str) -> int:
    # [REDACTED: internal logic]
    return 1


def _normalize_trigger_source(value: str | None):
    """Map edge trigger source values to TriggerSource enum values."""
    # [REDACTED: sensitive mapping logic]
    return None


class SecurityHeadersMiddleware(BaseHTTPMiddleware):
    """Add standard security headers to every response."""

    async def dispatch(self, request: Request, call_next) -> Response:
        response = await call_next(request)
        # [REDACTED: security header configuration]
        return response


async def _process_kafka_alert(alert_data: dict) -> None:
    """Callback for Kafka consumer — persist alert event, upsert incident, broadcast SSE."""
    # [REDACTED: sensitive processing logic for incident management and alerting]
    # Includes:
    # - Incident upsert logic
    # - Severity escalation detection
    # - Database persistence (Alert and Incident models)
    # - Push notification orchestration (FCM)
    # - Real-time SSE broadcasting
    pass


@asynccontextmanager
async def lifespan(_app: FastAPI):
    """Application lifespan — startup and shutdown."""
    # [REDACTED: startup logic, including database initialization and service startup]
    yield
    # [REDACTED: shutdown logic, including service cleanup and database disposal]


def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""
    app = FastAPI(
        title="DeepAtmos",
        version="1.0.0",
        docs_url="/docs",
        redoc_url="/redoc",
        openapi_url="/openapi.json",
        lifespan=lifespan,
    )

    # Rate limiting configuration
    # [REDACTED: rate limiting implementation]

    # Security headers
    app.add_middleware(SecurityHeadersMiddleware)

    # CORS configuration
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"], # [REDACTED: restricted origin list]
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Register routers
    from app.api.routes import (
        alerts, audit, auth, edges, nodes, notifications, readings, reports, system, tunnels, users,
    )

    prefix = "/api/v1"
    app.include_router(auth.router, prefix=prefix)
    app.include_router(users.router, prefix=prefix)
    app.include_router(tunnels.router, prefix=prefix)
    app.include_router(edges.router, prefix=prefix)
    app.include_router(nodes.router, prefix=prefix)
    app.include_router(readings.router, prefix=prefix)
    app.include_router(alerts.router, prefix=prefix)
    app.include_router(notifications.router, prefix=prefix)
    app.include_router(reports.router, prefix=prefix)
    app.include_router(audit.router, prefix=prefix)
    app.include_router(system.router, prefix=prefix)

    @app.get("/health", tags=["Health"])
    async def health_check():
        return {"status": "healthy"}

    return app


app = create_app()
