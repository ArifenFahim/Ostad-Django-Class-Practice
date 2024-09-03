from django.urls import path
from .import views

urlpatterns = [
    path('',views.task_lisk,name='task_list'),
    path('<int:pk>/', views.task_details,name='task_details')
]
