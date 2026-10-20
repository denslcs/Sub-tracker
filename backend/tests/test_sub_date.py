
from datetime import date

from app.api.subs.models import SubModel
import app.api.subs.service as service


# Функция для подмены сегодняшней даты
def set_test_date(monkeypatch, test_date):
    class FakeDate(date):
        @classmethod
        def today(cls):
            return test_date

    monkeypatch.setattr(service, "date", FakeDate)


# Тест 1. Автопродление включено
def test_auto_renew(monkeypatch):
    set_test_date(monkeypatch, date(2026, 10, 20))

    sub = SubModel(
        name="Spotify",
        price=350,
        auto_renew=True,
        next_payment_date=date(2026, 10, 15),
        is_active=True,
        user_id=1
    )

    service.update_subscription_status(sub)

    assert sub.next_payment_date == date(2026, 11, 15)
    assert sub.is_active is True


# Тест 2. Автопродление выключено
def test_no_auto_renew(monkeypatch):
    set_test_date(monkeypatch, date(2026, 10, 20))

    sub = SubModel(
        name="Netflix",
        price=500,
        auto_renew=False,
        next_payment_date=date(2026, 10, 15),
        is_active=True,
        user_id=1
    )

    service.update_subscription_status(sub)

    assert sub.is_active is False
    assert sub.next_payment_date == date(2026, 10, 15)


# Тест 3. Дата платежа ещё не наступила
def test_future_payment(monkeypatch):
    set_test_date(monkeypatch, date(2026, 10, 20))

    sub = SubModel(
        name="YouTube",
        price=299,
        auto_renew=True,
        next_payment_date=date(2026, 11, 15),
        is_active=True,
        user_id=1
    )

    service.update_subscription_status(sub)

    assert sub.next_payment_date == date(2026, 11, 15)
    assert sub.is_active is True


# Тест 4. Пропущено несколько месяцев
def test_overdue_months(monkeypatch):
    set_test_date(monkeypatch, date(2026, 10, 20))

    sub = SubModel(
        name="Yandex",
        price=199,
        auto_renew=True,
        next_payment_date=date(2026, 7, 10),
        is_active=True,
        user_id=1
    )

    service.update_subscription_status(sub)

    assert sub.next_payment_date == date(2026, 11, 10)
    assert sub.is_active is True
