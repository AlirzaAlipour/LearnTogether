from django.urls import path
from . import views
app_name = 'communications'

urlpatterns = [
    path('chat/<str:pk>/', views.join_chat, name='join_chat'),
]