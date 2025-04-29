from .auth import router as auth_router
from .robot import router as robot_router

routers = [
    auth_router,
    robot_router,
]
