import requests
from django.conf import settings

from app.models import ForexRate


def get_dataFrom_alphavantage():
    api_key = settings.API_KEY
    url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=USD' \
          '&apikey=' + api_key
    r = requests.get(url)
    data = r.json()
    if 'Realtime Currency Exchange Rate' in data:
        exchange_info = data['Realtime Currency Exchange Rate']
        forex_data = {'from_curr_code': exchange_info['1. From_Currency Code'],
                      'from_curr_name': exchange_info['2. From_Currency Name'],
                      'to_curr_code': exchange_info['3. To_Currency Code'],
                      'to_curr_name': exchange_info['4. To_Currency Name'],
                      'exchange_rate': exchange_info['5. Exchange Rate'],
                      'last_updated': exchange_info['6. Last Refreshed'],
                      'time_zone': exchange_info['7. Time Zone'],
                      'bid_price': exchange_info['8. Bid Price'],
                      'ask_price': exchange_info['9. Ask Price']}
        obj = ForexRate(**forex_data)
        obj.save()
    if 'Note' in data:
        return data['Note']
    if 'Error Message' in data:
        return data['Error Message']
