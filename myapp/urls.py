from django.urls import *
from . import views

urlpatterns = [
    path('home', views.home),
    path('worker/<int:id>', views.worker),
    path('manager/<int:id>', views.manager),
    path('director/<int:id>', views.director),
]