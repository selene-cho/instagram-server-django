from django.urls import path
from .views import Reviews

urlpatterns = [
    path("", Reviews.as_view())
]
