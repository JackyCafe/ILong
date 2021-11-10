from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from app.models import UserInfo, CurrencyInfo, PlantInfo, IrrIgationInfo, EcologyInfo, PlantingHistory, Questionnaire, \
    Daily, Other
from app.serializers import UserInfoSerializers, CurrencyInfoSerializers, PlantInfoSerializers, \
    IrrIgationInfoSerializers, EcologyInfoSerializers, PlantingHistorySerializers, QuestionnaireSerializers, \
    DailySerializers, OtherSerializers


class UserInfoViewSet(viewsets.ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializers


class CurrencyInfoViewSet(viewsets.ModelViewSet):
    queryset = CurrencyInfo.objects.all()
    serializer_class = CurrencyInfoSerializers


class PlantInfoViewSet(viewsets.ModelViewSet):
    queryset = PlantInfo.objects.all()
    serializer_class = PlantInfoSerializers


class IrrIgationInfoViewSet(viewsets.ModelViewSet):
    queryset = IrrIgationInfo.objects.all()
    serializer_class = IrrIgationInfoSerializers


class EcologyInfoViewSet(viewsets.ModelViewSet):
    queryset = EcologyInfo.objects.all()
    serializer_class = EcologyInfoSerializers


class PlantingHistoryViewSet(viewsets.ModelViewSet):
    queryset = PlantingHistory.objects.all()
    serializer_class = PlantingHistorySerializers


class QuestionnaireViewSet(viewsets.ModelViewSet):
    queryset = Questionnaire.objects.all()
    serializer_class = QuestionnaireSerializers


class DailyViewSet(viewsets.ModelViewSet):
    queryset = Daily.objects.all()
    serializer_class = DailySerializers


class OtherViewSet(viewsets.ModelViewSet):
    queryset = Other.objects.all()
    serializer_class = OtherSerializers