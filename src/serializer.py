from rest_framework import serializers
from api.models import StockHistoricData, Stock


class StockSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Stock
        fields = ('symbol', 'name')

class StockHistoricDataSerializer(serializers.ModelSerializer) :
    date = serializers.DateField(format="%Y-%m-%d")

    class Meta :
        model = StockHistoricData
        fields = ( 'open', 'close', 'high', 'low', 'volume', 'date')
