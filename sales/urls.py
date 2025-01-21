from django.urls import path
from .views import SalesView, SalesDetailView

urlpatterns = [
    path('', SalesView.as_view()),
    path('<int:pk>/', SalesDetailView.as_view())
]