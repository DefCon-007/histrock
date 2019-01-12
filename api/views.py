from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from src import database as db
from src.serializer import StockHistoricDataSerializer, StockSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Avg, Max, Min

# Create your views here.
@csrf_exempt
@api_view(["GET"])
def getStockData(request) :
    """
    Date format must be YYYY-MM-DD
    :param request:
    :return:
    """
    if request.method == 'GET':
        stockSymbol = request.query_params.get("stockSymbol", None)
        startDate = request.query_params.get("start", None)
        endDate = request.query_params.get("end", None)
        stock = db.getStockBySymbol(stockSymbol)

        if stock :
            stockData = db.getStockDataByStockAndDate(stock=stock, start=startDate, end=endDate)
            maxMinDate = (stockData.aggregate(Max('date'), Min('date')))
            print(maxMinDate)
            serializedStockData = StockSerializer(stock)
            serializedStockHistoricData = StockHistoricDataSerializer(stockData, many=True)
            return Response({"stock": serializedStockData.data, "historicData": serializedStockHistoricData.data, "maxDate" : maxMinDate["date__max"]})
        else :
            #Invalid stock symbol sent
            return Response("Invalid Stock Symbol", status=status.HTTP_404_NOT_FOUND)

