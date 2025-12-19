from django.urls import path
from . import views


urlpatterns = [
    path('init/', views.init, name='init'),
    path('populate/', views.populate, name='populate'),
    path('display/', views.display, name='display'),
    path('clear_table/', views.clear_table, name='clear_table'),
]
