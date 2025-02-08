from django.urls import path
from .views import ListBook

urlpatterns = [
    path("", ListBook.as_view()),
]
