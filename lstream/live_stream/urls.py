from django.urls import path
from . import views

urlpatterns = [
    path('', views.start_page, name='start_page'),
    path('urls/', views.ViewAPIStream.as_view(), name='api_stream'),
]