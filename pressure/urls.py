from django.urls import path
from pressure import views

app_name = 'pressure'

urlpatterns = [
    path('home/', views.home, name='home'),
]
