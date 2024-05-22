from fastapi import FastAPI, UploadFile, File

#from .dependencies import get_query_token, get_token_header
#from .internal import admin
from .routers import comparison
from .core.config import settings
from starlette.middleware.cors import CORSMiddleware

#app = FastAPI(dependencies=[Depends(get_query_token)])

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    version=settings.API_VERSION,
)

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            str(origin).strip("/") for origin in settings.BACKEND_CORS_ORIGINS
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


app.include_router(comparison.router,prefix=settings.API_V1_STR)


@app.get("/", summary="Root endpoint", description="This is the root endpoint of the API.")
async def root():
    return {"message": "Index"}