"""FastAPI main module."""

# Default library imports
from logging import getLogger

# Third-party library imports
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

import uvicorn

# Project imports
from api.v1 import crud
from core.config import config

app = FastAPI(
    title=config.title
)

# Connect routers to paths.
app.include_router(
    crud.router, prefix="/api/v1/crud", tags=["crud"]
)

@app.on_event("startup")
async def startup():
    """Magic method to run something when server is starting."""
    pass


@app.on_event("shutdown")
async def shutdown():
    """Magic method to run something when server is shutting down.

    It closes connections with databases during shutdown.
    """
    pass


if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=config.app_port,
    )