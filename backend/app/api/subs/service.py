from datetime import date
from app.api.subs.models import SubModel
from dateutil.relativedelta import relativedelta

def update_subscription_status(sub: SubModel):
    today = date.today()

    if not sub.is_active:
        return

    if sub.next_payment_date > today:
        return

    if not sub.auto_renew:
        sub.is_active = False
        return

    while sub.next_payment_date <= today:
        sub.next_payment_date += relativedelta(months=1)