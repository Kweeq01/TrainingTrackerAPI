# Схемы ответов Pydantic (входные и выходные данные API)

from pydantic import BaseModel

class SWorkoutBase(BaseModel):
    pass

class SWorkoutAdd(SWorkoutBase):
    pass

class SWorkout(SWorkoutBase):
    pass