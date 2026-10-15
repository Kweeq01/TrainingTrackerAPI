# sqlalchemy-модели - описание таблиц бд в виде python классов

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import VARCHAR, ForeignKey, Enum, Numeric, Date
from enums import CalendarDay
from decimal import Decimal
from datetime import date

class Base(DeclarativeBase):
    pass

class ExerciseModel(Base):
    __tablename__ = "exercise"

    exercise_id: Mapped[int] = mapped_column(primary_key=True)
    exercise_name: Mapped[str] = mapped_column(VARCHAR(50))
    description: Mapped[str | None] = mapped_column(VARCHAR(100), nullable=True)

    training_sets: Mapped[list["SetModel"]] = relationship(back_populates="exercise")

class PlanModel(Base):
    __tablename__ = "plan"

    plan_id: Mapped[int] = mapped_column(primary_key=True)
    plan_name: Mapped[str] = mapped_column(VARCHAR(50))
    description: Mapped[str | None] = mapped_column(VARCHAR(100), nullable=True)

    days: Mapped[list["DayModel"]] = relationship(back_populates="plan")

class DayModel(Base):
    __tablename__ = "day"

    day_id: Mapped[int] = mapped_column(primary_key=True)
    plan_id: Mapped[int] = mapped_column(ForeignKey("plan.plan_id"))
    name_training_day: Mapped[str] = mapped_column(VARCHAR(50))
    calendar_day: Mapped[CalendarDay] = mapped_column(Enum(CalendarDay))

    plan: Mapped["PlanModel"] = relationship(back_populates="days")
    training_sets: Mapped[list["SetModel"]] = relationship(back_populates="day")
    sessions: Mapped[list["SessionModel"]] = relationship(back_populates="day")

class SetModel(Base):
    __tablename__ = "training_set"

    set_id: Mapped[int] = mapped_column(primary_key=True)
    exercise_id: Mapped[int] = mapped_column(ForeignKey("exercise.exercise_id"))
    day_id: Mapped[int] = mapped_column(ForeignKey("day.day_id"))
    sets_count: Mapped[int]
    reps_count: Mapped[int]
    weight: Mapped[Decimal] = mapped_column(Numeric(6, 3))

    exercise: Mapped["ExerciseModel"] = relationship(back_populates="training_sets")
    day: Mapped["DayModel"] = relationship(back_populates="training_sets")
    completed_sets: Mapped[list["CompletedSetModel"]] = relationship(back_populates="training_set")

class SessionModel(Base):
    __tablename__ = "session"

    session_id: Mapped[int] = mapped_column(primary_key=True)
    day_id: Mapped[int] = mapped_column(ForeignKey("day.day_id"))
    session_date: Mapped[date] = mapped_column(Date)
    notes: Mapped[str | None] = mapped_column(VARCHAR(150), nullable=True)

    day: Mapped["DayModel"] = relationship(back_populates="sessions")
    completed_sets: Mapped[list["CompletedSetModel"]] = relationship(back_populates="session")

class CompletedSetModel(Base):
    __tablename__ = "completed_set" 

    completed_set_id: Mapped[int] = mapped_column(primary_key=True)
    session_id: Mapped[int] = mapped_column(ForeignKey("session.session_id"))
    set_id: Mapped[int] = mapped_column(ForeignKey("training_set.set_id"))
    set_number: Mapped[int]
    completed_reps: Mapped[int]
    completed_weight: Mapped[Decimal] = mapped_column(Numeric(6, 3))
    notes: Mapped[str | None] = mapped_column(VARCHAR(150), nullable=True)

    session: Mapped["SessionModel"] = relationship(back_populates="completed_sets")
    training_set: Mapped["SetModel"] = relationship(back_populates="completed_sets")