from models import workouts
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from decimal import Decimal

async def create_training_set(db: AsyncSession, day_id: int, exercise_id: int, reps_count: int, sets_count: int, weight: Decimal) -> workouts.TrainingSetModel | None:
    day = await db.get(workouts.DayModel, day_id)
    exercise = await db.get(workouts.ExerciseModel, exercise_id)

    if day is None or exercise is None:
        return None

    new_training_set = workouts.TrainingSetModel(day_id=day_id, exercise_id=exercise_id, reps_count=reps_count, sets_count=sets_count, weight=weight)

    db.add(new_training_set)
    await db.commit()
    await db.refresh(new_training_set)
    return new_training_set

async def get_training_set_by_id(db: AsyncSession, training_set_id: int) -> workouts.TrainingSetModel | None:
    training_set = await db.get(workouts.TrainingSetModel, training_set_id)
    return training_set

async def get_all_training_sets(db: AsyncSession) -> list[workouts.TrainingSetModel]:
    query = select(workouts.TrainingSetModel)
    training_sets = (await db.scalars(query)).all()
    return training_sets

async def delete_training_set(db: AsyncSession, training_set_id: int) -> bool:
    training_set = await db.get(workouts.TrainingSetModel, training_set_id)

    if training_set:
        await db.delete(training_set)
        await db.commit()
        return True
    else:
        return False