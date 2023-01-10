from django.urls import path
from . import views
from .views import ListaPendientes

urlpatterns = [path('', ListaPendientes.as_view(), name='Pendientes')]
