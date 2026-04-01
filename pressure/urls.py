from django.urls import path
from pressure import views

app_name = 'pressure'

urlpatterns = [
    path('', views.home, name='home'),
    path('list_result/', views.result_pressure, name='result'),
    path('add_result/', views.add_result, name='add_result'),
    path('update/<int:pk>/', views.update_result, name='update'),
]
