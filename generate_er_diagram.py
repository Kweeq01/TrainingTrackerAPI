from eralchemy2 import render_er
from models.workouts import Base

render_er(Base, "er_diagram.png")