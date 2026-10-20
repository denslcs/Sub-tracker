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

## Структура проекта

```text
Sub-tracker/
│
├── backend/
│   ├── app/
│   │   ├── main.py                # точка входа FastAPI
│   │   ├── config.py              # настройки приложения
│   │   ├── database.py            # engine, SessionLocal, Base, get_db
│   │   │
│   │   ├── security/
│   │   │   ├── deps.py            # получение текущего пользователя
│   │   │   ├── jwt.py             # создание и декодирование JWT
│   │   │   └── passwords.py       # хеширование и проверка паролей
│   │   │
│   │   └── api/
│   │       ├── auth/
│   │       │   ├── models.py      # модель пользователя
│   │       │   ├── router.py      # эндпоинты регистрации, логина, профиля
│   │       │   └── schemas.py     # схемы Pydantic для auth
│   │       │
│   │       └── subs/
│   │           ├── models.py      # модель подписки
│   │           ├── router.py      # CRUD-эндпоинты подписок
│   │           ├── schemas.py     # схемы Pydantic для подписок
│   │           └── service.py     # бизнес-логика работы с датами подписок
│   │
│   ├── tests/
│   │   └── test_subscription_dates.py   # тесты логики дат подписок
│   │
│   ├── requirements.txt
│   └── sub.db
│
└── README.md
```
