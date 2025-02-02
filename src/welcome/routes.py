

from fastapi import APIRouter

from src.welcome.service import WelcomeService


welcome_router = APIRouter()
wl_service = WelcomeService()

@welcome_router.get('/')
async def welcome():
    res = await wl_service.test()
    return res