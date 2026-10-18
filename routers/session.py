from fastapi import APIRouter, HTTPException
from database import SessionDep
from schemas import workout
from repository.session import create_session, get_session_by_id, get_all_sessions, delete_session

router = APIRouter(
    prefix="/sessions",
    tags=["Sessions"]
)

@router.post("", response_model=workout.SSession)
async def add_session(session: workout.SSessionAdd, db: SessionDep):
    new_session = await create_session(db, session.day_id, session.notes, session.session_date)

    if new_session is None:
        raise HTTPException(status_code=404, detail="Day not found")
    return new_session

@router.get("/{session_id}", response_model=workout.SSession)
async def get_session(db: SessionDep, session_id: int):
    session = await get_session_by_id(db, session_id)

    if session is None:
        raise HTTPException(status_code=404, detail="Session not found")
    return session

@router.get("", response_model=list[workout.SSession])
async def get_sessions(db: SessionDep):
    return await get_all_sessions(db)

@router.delete("/{session_id}")
async def remove_sessions(db: SessionDep, session_id: int):
    deleted = await delete_session(db, session_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Session not found")
    return {"detail": "Session deleted"}