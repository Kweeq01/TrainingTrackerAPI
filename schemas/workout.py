# Схемы ответов Pydantic (входные и выходные данные API)

from pydantic import BaseModel, ConfigDict, Field
from enums import CalendarDay
from decimal import Decimal
from datetime import date

class SExerciseAdd(BaseModel):
    exercise_name: str
    description: str | None = None

class SExercise(SExerciseAdd):
    exercise_id: int

    model_config = ConfigDict(from_attributes=True)


class SPlanAdd(BaseModel):
    plan_name: str
    description: str | None = None

class SPlan(SPlanAdd):
    plan_id: int

    model_config = ConfigDict(from_attributes=True)


class SDayAdd(BaseModel):
    plan_id: int
    name_training_day: str
    calendar_day: CalendarDay

class SDay(SDayAdd):
    day_id: int
    plan_id: int

    model_config = ConfigDict(from_attributes=True)


class SSetAdd(BaseModel):
    sets_count: int
    reps_count: int
    weight: Decimal

class SSet(SSetAdd):
    set_id: int
    exercise_id: int
    day_id: int

    model_config = ConfigDict(from_attributes=True)


class SSessionAdd(BaseModel):
    day_id: int
    session_date: date
    notes: str | None = None

class SSession(SSessionAdd):
    session_id: int
    day_id: int

    model_config = ConfigDict(from_attributes=True)


class SCompletedSetAdd(BaseModel):
    set_number: int
    completed_reps: int
    completed_weight: Decimal
    notes: str | None = None

class SCompletedSet(SCompletedSetAdd):
    completed_set_id: int
    session_id: int
    set_id: int

    model_config = ConfigDict(from_attributes=True)