from fastapi import APIRouter, HTTPException
from database import SessionDep
from schemas import workout
from repository.completed_set import create_completed_set, get_completed_set_by_id, get_all_completed_sets, delete_completed_set

router = APIRouter(
    prefix="/completed-sets",
    tags=["Completed sets"]
)

@router.post("", response_model=workout.SCompletedSet)
async def add_completed_set(db: SessionDep, completed_set: workout.SCompletedSetAdd):
    forming_completed_set =  await create_completed_set(db, completed_set.completed_reps, completed_set.completed_weight, completed_set.notes, completed_set.session_id, completed_set.training_set_id, completed_set.completed_set_number)

    if forming_completed_set is None:
        raise HTTPException(status_code=404, detail="Training set or session not found")
    return forming_completed_set

@router.get("/{completed_set_id}", response_model=workout.SCompletedSet)
async def get_completed_set(db: SessionDep, completed_set_id: int):
    completed_set = await get_completed_set_by_id(db, completed_set_id)

    if completed_set is None:
        raise HTTPException(status_code=404, detail="Completed set not found")
    return completed_set

@router.get("", response_model=list[workout.SCompletedSet])
async def get_completed_sets(db: SessionDep):
    return await get_all_completed_sets(db)

@router.delete("/{completed_set_id}")
async def remove_completed_set(db: SessionDep, completed_set_id: int):
    deleted = await delete_completed_set(db, completed_set_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Completed set not found")
    return {"detail": "Completed set deleted"}