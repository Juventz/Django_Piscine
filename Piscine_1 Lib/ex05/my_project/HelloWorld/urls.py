from django.urls import path
from HelloWorld import views

urlpatterns = [
    path('helloworld/', views.hello_world, name='hello'),
]
