# Точка входа - все создания и подключения 

from fastapi import FastAPI
from routers.exercise import router as exercise_router
from routers.plan import router as plan_router
from routers.day import router as day_router
from routers.session import router as session_router
from routers.training_set import router as training_set_router
from routers.completed_set import router as completed_set_router

app = FastAPI()

all_routers = [exercise_router, plan_router, day_router, session_router, training_set_router, completed_set_router]

for router in all_routers:
    app.include_router(router)
    