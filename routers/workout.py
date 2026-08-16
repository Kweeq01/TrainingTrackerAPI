# Эндпоинты (HTTP-слой)
# Принимают запрос, валидируют через schemas/, вызывают repository/, возвращают ответ.

from fastapi import APIRouter

router = APIRouter(
    prefix="/workouts",
    tags=["Workouts"]
)

@router.post("")
async def create_trainin_plan():
    return

@router.get("/{plan_id}")
async def get_one_training_plan():
    return

@router.get("")
async def get_all_trainings_plan():
    return

@router.delete("")
async def delete_training_plan():
    return