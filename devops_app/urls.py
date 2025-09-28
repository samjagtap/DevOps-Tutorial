from django.urls import path
from .views import *


urlpatterns = [
    path('reporters/', ReporterListCreateView.as_view(), name='reporter-list-create'),
    path('reporters/<int:pk>/', ReporterRetrieveUpdateDestroyView.as_view(), name='reporter-detail'),
]
