from fastapi import FastAPI
from .routers import tasks, schedules, routines, exercises, finances
from .database import engine, Base

# Inicializar o banco de dados
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Rotas principais
app.include_router(tasks.router)
app.include_router(schedules.router)
app.include_router(routines.router)
app.include_router(exercises.router)
app.include_router(finances.router)

@app.get("/")
def read_root():
    return {"message": "Personal Assistant API"}
