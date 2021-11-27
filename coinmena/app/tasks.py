from app.utils import get_dataFrom_alphavantage
from coinmena import celery_app


@celery_app.task(name='app.tasks.fetch_exchange_rate')
def fetch_exchange_price():
    message = get_dataFrom_alphavantage()
    print(message)
