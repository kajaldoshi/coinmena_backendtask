from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import ForexRate
from app.utils import get_dataFrom_alphavantage


class Quotes(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request):
        obj = ForexRate.objects.all().order_by('-last_updated').first()
        if obj:
            rate = obj.exchange_rate
            return Response({'exchange_rate': rate})
        else:
            return Response({'message': 'No records exist in database'})

    def post(self, request):
        response = get_dataFrom_alphavantage()
        return Response({'message': response or 'Success'})
