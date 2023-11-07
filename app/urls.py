from django.urls import path
from . import views

urlpatterns = [
    path('', views.dowelltest, name='dowelltest'),
]