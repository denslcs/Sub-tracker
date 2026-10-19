# Sub-tracker

Sub-tracker - REST API для учёта пользовательских подписок, разработанное на Python с использованием FastAPI.

## Описание проекта
Приложение для слежки за личными подписками на разные сервисы, ведется учет времени, стоимость и общий подсчет расходов на подписки за месяц.

## Технологии
Python
FastAPI
Uvicorn
SQLAlchemy
SQLite
Pydantic

## Структура проекта

Sub-tracker/
└── backend/
    ├── .venv/
    ├── app/
    │   ├── main.py
    │   ├── config.py
    │   ├── database.py
    │   ├── security
    │           ├── deps.py
    │           ├── jwt.py
    │           └── passwords.py
    │   └── api/
    │       ├── auth/
    │           ├── models.py
    │           ├── router.py
    │           └── schemas.py
    │       └── subs/
    │           ├── models.py
    │           ├── router.py
    │           ├── schemas.py
    │           └── service.py
    │
    ├── tests/                      
    │   └── test_subscription_dates.py  
    │
    ├── requirements.txt
    └── sub.db
