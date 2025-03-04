from django.urls import path
from .views import log

urlpatterns = [
    path('', log, name='log'),
]