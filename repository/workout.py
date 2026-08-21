# Доступ к данным, функции и классы - логика работы с бд (CRUD)

from models import workouts
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

async def create_exercise(db: AsyncSession, exercise_name:str, description:str | None) -> workouts.ExerciseModel:
    new_exercise = workouts.ExerciseModel(exercise_name=exercise_name , description=description)

    db.add(new_exercise)
    await db.commit()
    await db.refresh(new_exercise)
    return new_exercise

async def get_exercise_by_id(db: AsyncSession, exercise_id:int) -> workouts.ExerciseModel | None:
    exercise = await db.get(workouts.ExerciseModel, exercise_id)
    return exercise

async def get_all_exercises(db: AsyncSession) -> list[workouts.ExerciseModel]:
    query = select(workouts.ExerciseModel)
    exercises = (await db.scalars(query)).all()
    return exercises

async def delete_exercise(db: AsyncSession, exercise_id:int) -> bool:
    exercise = await db.get(workouts.ExerciseModel, exercise_id)

    if exercise:
        await db.delete(exercise)
        await db.commit()
        return True
    else:
        return False
