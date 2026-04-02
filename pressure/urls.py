from django.urls import path
from pressure import views

app_name = 'pressure'

urlpatterns = [
    path('', views.home, name='home'),
    path('list_result/', views.result_pressure, name='result'),
    path('indicators/', views.add_result, name='indicators'),
    path('update/<int:pk>/', views.update_result, name='update'),
]
