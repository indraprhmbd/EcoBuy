from fastapi import APIRouter

from app.api.v1.endpoints import impact, request, waste

api_router = APIRouter()

api_router.include_router(waste.router, prefix="/waste", tags=["waste"])
api_router.include_router(request.router, prefix="/request", tags=["request"])
api_router.include_router(impact.router, prefix="/impact", tags=["impact"])
