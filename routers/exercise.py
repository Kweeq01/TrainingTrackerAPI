# Эндпоинты exercises (HTTP-слой)
# Принимают запрос, валидируют через schemas/, вызывают repository/, возвращают ответ.

from fastapi import APIRouter, HTTPException
from database import SessionDep
from schemas import workout
from repository.exercise import create_exercise, get_exercise_by_id, get_all_exercises, delete_exercise

router = APIRouter(
    prefix="/exercises",
    tags=["Exercises"]
)

@router.post("", response_model=workout.SExercise)
async def add_exercise(exercise: workout.SExerciseAdd, db: SessionDep):
    return await create_exercise(db, exercise.exercise_name, exercise.description)

@router.get("/{exercise_id}", response_model=workout.SExercise)
async def get_exercise(db: SessionDep, exercise_id: int):
    exercise =  await get_exercise_by_id(db, exercise_id)

    if exercise is None:
        raise HTTPException(status_code=404, detail="Exercise not found")
    return exercise

@router.get("", response_model=list[workout.SExercise])
async def get_exercises(db: SessionDep):
    return await get_all_exercises(db)

@router.delete("/{exercise_id}")
async def remove_exercise(db: SessionDep, exercise_id: int):
    deleted = await delete_exercise(db, exercise_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Exercise not found")
    return {"detail": "Exercise deleted"}