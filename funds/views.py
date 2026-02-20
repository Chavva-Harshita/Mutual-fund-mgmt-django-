
from .models import MutualFund


from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def fund_list(request):
    return render(request, 'funds/fund_list.html')

def compare(request):
    return render(request, 'funds/compare.html')