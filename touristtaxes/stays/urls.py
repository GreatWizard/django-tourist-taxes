from django.urls import path
from . import views

urlpatterns = [
    path('', views.StayListView.as_view(), name='stays'),
    path('validated-all/', views.validate_all, name='stays--validate-all'),
]
