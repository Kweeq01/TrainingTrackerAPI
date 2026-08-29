from models import workouts
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

async def create_plan(db: AsyncSession, plan_name: str, description: str) -> workouts.PlanModel:
    new_plan = workouts.PlanModel(plan_name=plan_name, description=description)

    db.add(new_plan)
    await db.commit()
    await db.refresh(new_plan)
    return new_plan

async def get_plan_by_id(db: AsyncSession, plan_id: int) -> workouts.PlanModel | None:
    plan = await db.get(workouts.PlanModel, plan_id)
    return plan

async def get_all_plans(db: AsyncSession) -> workouts.PlanModel:
    query = select(workouts.PlanModel)
    plans = (await db.scalars(query)).all()
    return plans

async def delete_plan(db: AsyncSession, plan_id: int) -> bool:
    plan = await db.get(workouts.PlanModel, plan_id)

    if plan:
        await db.delete(plan)
        await db.commit()
        return True
    else:
        return False