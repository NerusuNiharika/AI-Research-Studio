from fastapi import APIRouter

from api.research import router as research_router
from api.auth import router as auth_router
from api.profile import router as profile_router

router = APIRouter()

# Authentication
router.include_router(auth_router)

# Research
router.include_router(research_router)

# Profile
router.include_router(profile_router)