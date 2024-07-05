from django.urls import path
from .views import IPView

urlpatterns = [
    path('hello/', IPView.as_view(), name='hello'),
]