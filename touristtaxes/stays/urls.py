from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='stays'),
    path('validated-all/', views.validate_all, name='stays--validate-all'),
    path('post/', views.post, name='stays--post'),
]
