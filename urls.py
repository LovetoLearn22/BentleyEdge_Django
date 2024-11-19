from django.urls import path
from .templates.edge import views

urlpatterns = [
    path('', views.article_list, name='article_list'),
]
