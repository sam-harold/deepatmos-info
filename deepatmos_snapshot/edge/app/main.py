"""DeepAtmos Edge Layer — Entry Point."""

import asyncio
import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI

# [REDACTED: sensitive core and service imports]
# Includes: TCP server implementation, Kafka publisher, Cloud Sync service


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Edge server lifespan orchestration."""
    # Startup actions
    logger.info("Starting DeepAtmos Edge Server")
    
    # [REDACTED: local database initialization]
    
    # [REDACTED: sensitive service startup orchestration]
    # logic flow:
    # 1. Initialize local SQLite/Edge database
    # 2. Start Kafka producer for cloud communication
    # 3. Initialize and start TCP server for ESP32 connectivity
    # 4. Start background service for cloud synchronization (CloudSyncService)
    
    yield
    
    # Shutdown actions
    # [REDACTED: graceful shutdown logic for all services]


app = FastAPI(
    title="DeepAtmos Edge Node",
    description="Edge processing and routing for sensor components",
    docs_url=None, 
    redoc_url=None,
    lifespan=lifespan
)


@app.get("/health")
async def health_check():
    return {"status": "ok"}
