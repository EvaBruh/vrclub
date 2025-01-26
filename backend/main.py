import secrets

import uvicorn
from fastapi import FastAPI

from core.database import engine
from sqladmin import Admin
from admin_models import register_views  # Импорт здесь!

app = FastAPI()
admin = Admin(app, engine)  # Запуск админки

# 3. Регистрируем компоненты в админке
register_views(admin)


@app.get("/debug/")
def debug():
    return "debug"


if "__name__" == "__main__":
    uvicorn.run("main:app", reload=True)
