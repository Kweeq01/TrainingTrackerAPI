# Точка входа - все создания и подключения 

from fastapi import FastAPI
from routers.workout import router as workout_router

app = FastAPI()
app.include_router(workout_router)