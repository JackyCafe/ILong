"""ILong URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

import app
from app.views import PlantInfoAPIView, IrrIgationInfoAPIView, QuestionAPIView, \
    UserInfoAPIView, CurrencyInfoAPIView, EcologyInfoAPIView, \
    PlantHistoryAPIView, DailyAPIView, OtherAPIView

urlpatterns = [
    path(r'userinfo/', UserInfoAPIView.as_view()),
    path(r'currencyinfo/', CurrencyInfoAPIView.as_view()),
    path(r'plantinfo/', PlantInfoAPIView.as_view()),
    path(r'irrigationinfo/', IrrIgationInfoAPIView.as_view()),
    path(r'ecologyinfo/', EcologyInfoAPIView.as_view()),
    path(r'plantHistory/', PlantHistoryAPIView.as_view()),
    path(r'question/', QuestionAPIView.as_view()),
    path(r'daily/', DailyAPIView.as_view()),
    path(r'other/', OtherAPIView.as_view()),

]