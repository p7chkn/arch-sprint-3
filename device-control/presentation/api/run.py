from fastapi import FastAPI
import uvicorn
from presentation.api.routers.devices import router as device_router

app = FastAPI(
    title="Device control service",
    version="1.0.0",
)
app.include_router(device_router, prefix="", tags=["devices"])

def run_app():
    uvicorn.run(app,
                host="0.0.0.0")
