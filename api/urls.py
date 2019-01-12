from django.urls import path

from . import views


urlpatterns = [
    path('stockdata', views.getStockData, name='stockdata'),
    ]