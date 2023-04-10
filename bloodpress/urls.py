from . import views
from django.urls import path, include

urlpatterns = [
    path('survey/', views.survey, name='survey'),
    path('results/', views.results, name='results'),
    path('thank_you/', views.thank_you, name='thank_you'),
]
