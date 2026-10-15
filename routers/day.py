from fastapi import APIRouter, HTTPException
from database import SessionDep
from schemas import workout
from repository.day import create_day, get_day_by_id, get_all_days, delete_day

router = APIRouter(
    prefix="/days",
    tags=["Days"]
)

@router.post("", response_model=workout.SDay)
async def add_day(day: workout.SDayAdd, db: SessionDep):
    return await create_day(db, day.plan_id, day.name_training_day, day.calendar_day)

@router.get("/{day_id}", response_model=workout.SDay)
async def get_day(db: SessionDep, day_id: int):
    day = await get_day_by_id(db, day_id)

    if day is None:
        raise HTTPException(status_code=404, detail="Day not found")
    return day

@router.get("", response_model=list[workout.SDay])
async def get_days(db: SessionDep):
    return await get_all_days(db)

@router.delete("/{day_id}")
async def remove_day(db: SessionDep, day_id: int):
    deleted = await delete_day(db, day_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Day not found")
    return {"detail": "Day deleted"}