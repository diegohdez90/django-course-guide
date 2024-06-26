from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='challenges_index'),
    path('<int:month>', views.monthly_challenge_by_number_month, name='challenge_by_month_number'),
    path('<str:month>', views.monthly_challenge, name='monthly_challenge'),
]
