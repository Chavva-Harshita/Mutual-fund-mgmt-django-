from django.shortcuts import render
from .models import MutualFund

def home(request):
    funds = MutualFund.objects.all()
    return render(request, 'funds/home.html', {'funds': funds})
