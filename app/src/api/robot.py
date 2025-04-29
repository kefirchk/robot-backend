from fastapi import APIRouter

router = APIRouter(prefix="/robot", tags=["Robot"])


@router.get("/test")
async def test():
    return 200


@router.websocket("/control")
async def control():
    pass
