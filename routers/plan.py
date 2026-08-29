# Эндпоинты plan (HTTP-слой)
# Принимают запрос, валидируют через schemas/, вызывают repository/, возвращают ответ.

from fastapi import APIRouter, HTTPException
from database import SessionDep
from schemas import workout
from repository.plan import create_plan, get_plan_by_id, delete_plan, get_all_plans

router = APIRouter(
    prefix="/plans",
    tags=["Plans"]
)

@router.post("", response_model=workout.SPlan)
async def add_plan(plan: workout.SPlanAdd, db: SessionDep):
    return await create_plan(db, plan.plan_name, plan.description)

@router.get("/{plan_id}", response_model=workout.SPlan)
async def get_plan(db: SessionDep, plan_id: int):
    plan = await get_plan_by_id(db, plan_id)

    if plan is None:
        raise HTTPException(status_code=404 , detail="Plan not found")
    return plan

@router.get("", response_model=list[workout.SPlan])
async def get_plans(db: SessionDep):
    return await get_all_plans(db)

@router.delete("/{plan_id}")
async def remove_plan(db: SessionDep, plan_id: int):
    deleted = await delete_plan(db, plan_id)

    if not deleted:
        raise HTTPException(status_code=404 , detail="Plan not found")
    return {"detail": "Plan deleted"}