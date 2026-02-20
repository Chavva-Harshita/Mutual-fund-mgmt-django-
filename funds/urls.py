from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('funds/', views.fund_list, name='fund_list'),
    path('compare/', views.compare, name='compare'),
]