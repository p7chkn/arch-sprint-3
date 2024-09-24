from fastapi import FastAPI
import uvicorn
from presentation.api.routers.log import router as log_router

app = FastAPI(
    title="Device control service",
    version="1.0.0",
)
app.include_router(log_router, prefix="", tags=["telemetry_logs"])

def run_app():
    uvicorn.run(app, host="0.0.0.0")
