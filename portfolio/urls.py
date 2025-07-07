from django.urls import path
from portfolio import views

urlpatterns = [
    path('', views.MainView.as_view(), name="home_page")
]