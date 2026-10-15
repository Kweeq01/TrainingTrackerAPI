# Точка входа - все создания и подключения 

from fastapi import FastAPI
from routers.exercise import router as exercise_router
from routers.plan import router as plan_router
from routers.day import router as day_router

app = FastAPI()

all_routers = [exercise_router, plan_router, day_router]

for router in all_routers:
    app.include_router(router)
    