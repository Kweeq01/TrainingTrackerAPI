from models import workouts
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from datetime import date

async def create_session(db: AsyncSession, day_id: int, notes: str | None, session_date: date) -> workouts.SessionModel | None:
    day = await db.get(workouts.DayModel, day_id)

    if day is None:
        return None

    new_session = workouts.SessionModel(day_id=day_id, notes=notes, session_date=session_date)

    db.add(new_session)
    await db.commit()
    await db.refresh(new_session)
    return new_session

async def get_session_by_id(db: AsyncSession, session_id: int) -> workouts.SessionModel | None:
    session = await db.get(workouts.SessionModel, session_id)
    return session

async def get_all_sessions(db: AsyncSession) -> list[workouts.SessionModel]:
    query = select(workouts.SessionModel)
    sessions = (await db.scalars(query)).all()
    return sessions

async def delete_session(db: AsyncSession, session_id: int) -> bool:
    session = await db.get(workouts.SessionModel, session_id)

    if session:
        await db.delete(session)
        await db.commit()
        return True
    else:
        return False