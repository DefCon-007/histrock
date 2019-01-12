from django.db import models


class Stock(models.Model):
    symbol = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=100)


class StockHistoricData(models.Model) :
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, default=None, related_name="historicData")
    open = models.FloatField()
    close =  models.FloatField()
    low =  models.FloatField()
    high =  models.FloatField()
    volume = models.FloatField()
    date = models.DateField()

    class Meta :
        ordering = ["date"]



# Create your models here.