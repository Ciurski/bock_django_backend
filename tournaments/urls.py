from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from . import views


urlpatterns = [
        path('', views.ListContest.as_view()),
        path('<int:pk>/', views.DetailContest.as_view()),
        path('results/', views.ListResult.as_view()),
        path('result/<int:pk>/', views.DetailResult.as_view()),
]
