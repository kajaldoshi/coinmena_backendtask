from django.conf.urls import url

from app.views import Quotes

urlpatterns = [
    url('v1/quotes', Quotes.as_view(), name='quotes')
]