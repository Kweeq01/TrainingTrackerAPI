from models.workouts import Base

Base.registry.configure()
print("Модели ок, связи настроены корректно")