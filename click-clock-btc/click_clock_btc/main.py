import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from starlette.requests import Request
from starlette.responses import Response
from api.router import BtcRouter

VERSION = "1.0.6"

app = FastAPI(
    title="BTC BACKEND",
    version=VERSION,
)

sub_app = FastAPI(
    version=VERSION,
    docs_url="/docs",
    openapi_url="/openapi.json",
)
sub_app.include_router(
    BtcRouter().get_router(), prefix="/btc_service", tags=["BTC"]
)

app.mount("/btc", sub_app)

@sub_app.exception_handler(Exception)
async def catch_exceptions_middleware(request: Request, err):
    base_error_message = f"Failed to execute: {request.method}: {request.url}"
    # Change here to LOGGER
    return JSONResponse(
        status_code=400, content={"message": f"{base_error_message}. Detail: {err}"}
    )

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
