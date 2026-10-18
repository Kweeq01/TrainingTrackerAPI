from models import workouts
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from enums import CalendarDay

async def create_day(db: AsyncSession, plan_id: int, name_training_day: str, calendar_day: CalendarDay) -> workouts.DayModel | None:
    plan = await db.get(workouts.PlanModel, plan_id)

    if plan is None:
        return None

    new_day = workouts.DayModel(plan_id=plan_id, name_training_day=name_training_day, calendar_day=calendar_day)

    db.add(new_day)
    await db.commit()
    await db.refresh(new_day)
    return new_day

async def get_day_by_id(db: AsyncSession, day_id: int) -> workouts.DayModel | None:
    day = await db.get(workouts.DayModel, day_id)
    return day

async def get_all_days(db: AsyncSession) -> list[workouts.DayModel]:
    query = select(workouts.DayModel)
    days = (await db.scalars(query)).all()
    return days

async def delete_day(db: AsyncSession, day_id: int) -> bool:
    day = await db.get(workouts.DayModel, day_id)

    if day:
        await db.delete(day)
        await db.commit()
        return True
    else:
        return False