from django.urls import path
from . import views

urlpatterns = [
    path('', views.StayListView.as_view(), name='stays'),
]
