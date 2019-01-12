from api.models import StockHistoricData, Stock

def addStockRecord(stock, open, close, high, low, vol, date):
    data = StockHistoricData()
    data.stock = stock
    data.open = open
    data.close = close
    data.high = high
    data.low = low
    data.volume = vol
    data.date = date
    data.save()


def addNewStock(symbol, name="") :
    data = Stock()
    data.symbol = symbol
    data.name = name
    data.save()


def getStockBySymbol(sym) :
    """

    :param sym: <String> The symbol of the stock
    :return: <Stock> The Stock object if stock found else None
    """
    try :
        stock = Stock.objects.get(symbol__iexact=sym)
        return stock
    except Stock.DoesNotExist as e:
        return None


def getStockDataByStockAndDate(stock, start, end):
    """
    Returns a queryset matching provided stock, start date(inclusive), end date(exclusive)
    :param stock: <Stock>
    :param start: <datetime.datetime>, if None first instance of record is taken
    :param end: <datetime.datetime>, if None last stance of record is taken
    :return: <Queryset>
    """
    if start :
        if end :
            data = StockHistoricData.objects.filter(stock=stock, date__gte=start, date__lte=end)
        else :
            data = StockHistoricData.objects.filter(stock=stock, date__gte=start)
    elif end :
        data = StockHistoricData.objects.filter(stock=stock, date__lte=end)
    else :
        data = StockHistoricData.objects.filter(stock=stock)
    return data
