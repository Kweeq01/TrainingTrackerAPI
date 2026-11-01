from fastapi import APIRouter, HTTPException
from database import SessionDep
from schemas import workout
from repository.training_set import create_training_set, get_training_set_by_id, get_all_training_sets, delete_training_set

router = APIRouter(
    prefix="/training-sets",
    tags=["Training sets"]
)

@router.post("", response_model=workout.STrainingSet)
async def add_training_set(training_set: workout.STrainingSetAdd, db:SessionDep):
    forming_training_set =  await create_training_set(db, training_set.day_id, training_set.exercise_id, training_set.reps_count, training_set.sets_count, training_set.weight)

    if forming_training_set is None:
        raise HTTPException(status_code=404, detail="Day or Exercise not found")
    return forming_training_set

@router.get("/{training_set_id}", response_model=workout.STrainingSet)
async def get_training_set(db: SessionDep, training_set_id: int):
    training_set = await get_training_set_by_id(db, training_set_id)

    if training_set is None:
        raise HTTPException(status_code=404, detail="Training set not found")
    return training_set

@router.get("", response_model=list[workout.STrainingSet])
async def get_training_sets(db: SessionDep):
    return await get_all_training_sets(db)

@router.delete("/{training_set_id}")
async def remove_training_set(db: SessionDep, training_set_id: int):
    deleted = await delete_training_set(db, training_set_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Training set not found")
    return {"detail": "Training set deleted"}