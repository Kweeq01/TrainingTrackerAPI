from models import workouts
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from decimal import Decimal

async def create_completed_set(db: AsyncSession, completed_reps: int, completed_weight: Decimal, notes: str, session_id: int, training_set_id: int, completed_set_number: int) -> workouts.CompletedSetModel | None:
    training_set = await db.get(workouts.TrainingSetModel, training_set_id)
    session = await db.get(workouts.SessionModel, session_id)

    if training_set is None or session is None:
        return None

    new_completed_set = workouts.CompletedSetModel(completed_reps=completed_reps, completed_weight=completed_weight, notes=notes, session_id=session_id, training_set_id=training_set_id, completed_set_number=completed_set_number)

    db.add(new_completed_set)
    await db.commit()
    await db.refresh(new_completed_set)
    return new_completed_set

async def get_completed_set_by_id(db: AsyncSession, completed_set_id: int) -> workouts.CompletedSetModel | None:
    completed_set = await db.get(workouts.CompletedSetModel, completed_set_id)
    return completed_set

async def get_all_completed_sets(db: AsyncSession) -> list[workouts.CompletedSetModel]:
    query = select(workouts.CompletedSetModel)
    completed_sets = (await db.scalars(query)).all()
    return completed_sets

async def delete_completed_set(db: AsyncSession, completed_set_id: int) -> bool:
    completed_set = await db.get(workouts.CompletedSetModel, completed_set_id)

    if completed_set:
        await db.delete(completed_set)
        await db.commit()
        return True
    else:
        return False