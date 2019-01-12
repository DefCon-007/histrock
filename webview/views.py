from django.shortcuts import render
from src import database as db

def index(request) :
    stockList = db.getAllSotcks()
    return render(request, "webview/index.html", {"stocks" : stockList})
# Create your views here.
