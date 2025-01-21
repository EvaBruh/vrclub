# VR Club Pet-Project

![FastAPI](https://img.shields.io/badge/FastAPI-v0.103.1-blue?style=flat-square&logo=fastapi)  
**FastAPI**, **SQLAlchemy**, **Alembic**, **Pydantic**

---


## 🚀 Запуск
На основе моего шаблона https://github.com/EvaBruh/fastapi-template
1. Клонируем реп
2. poetry install --no-root
3. Проверяем в `PyCharm` `Settings` настройках проекта указанное виртуальное окружение ([подробнее в разделе установка Poetry](https://github.com/EvaBruh/fastapi-template))

## 📋  Описание
Проект под небольшой VR Club с админкой. 

### 🛠 Стек технологий:

- **[FastAPI](https://fastapi.tiangolo.com/):** Фреймворк для создания API.
- **[SQLAlchemy](https://www.sqlalchemy.org/):** ORM для работы с базой данных.
- **[Alembic](https://alembic.sqlalchemy.org/):** Инструмент для управления миграциями.
- **[Pydantic](https://docs.pydantic.dev/latest/api/base_model/):** Работа с типами и валидацией данных.
- **[Poetry](https://python-poetry.org/):** Управление зависимостями и виртуальными окружениями.
- **[Docker](https://www.docker.com/):** Контейнеризация приложения.
- **[Redis](https://redis.io/):** Опционально для кэширования.
- **[Ruff](https://docs.astral.sh/ruff/):** Линтер/Форматтер с настройками в pyproject.toml
- **[Black](https://black.readthedocs.io/en/stable/getting_started.html):** Форматтер с настройками в pyproject.toml
- Всё что нужно для работы с PostgreSQL, и aiosqlite (sync/async).
- Библиотеки для тестирования: pyTest, httpx.
- Подробнее в pyproject.toml
---

## 📂 Структура проекта

[Шаблон](https://github.com/EvaBruh/fastapi-template) имеет следующую структуру:

```plaintext
fastapi-template/
├── alembic/                  # Каталог миграций Alembic
│   ├── versions/             # Каталог с файлами миграций
│   ├── env.py                # Основной файл конфигурации Alembic
│   └── script.py.mako        # Шаблон для новых миграций
├── backend/
│   ├── __init__.py
│   ├── main.py               # Точка входа FastAPI
│   ├── api/                  # Каталог с API маршрутами
│   ├── core/                 # Конфигурации и основные утилиты
│   ├── models/               # SQLAlchemy модели
│   ├── repositories/         # Репозитории для работы с БД
│   ├── schemas/              # Pydantic схемы
│   ├── services/             # Бизнес-логика
│   └── tests/                # Тесты
├── frontend/                 # По желанию
├── nginx/                    # Под Nginx конфигурацию
├── .env                      # Переменные окружения
├── pyproject.toml            # Poetry конфигурация
├── ruff.toml                 # Ruff конфигурация


