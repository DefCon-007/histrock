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
        stock = Stock.objects.get(symbol=sym)
        return stock
    except Stock.DoesNotExist as e:
        return None
