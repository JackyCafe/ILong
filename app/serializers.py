from rest_framework import serializers

from app.models import UserInfo, CurrencyInfo, PlantInfo, IrrIgationInfo, EcologyInfo, PlantingHistory, Questionnaire, \
    Daily, Other


class UserInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = '__all__'



class CurrencyInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = CurrencyInfo
        fields = '__all__'


class PlantInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = PlantInfo
        fields = '__all__'


class IrrIgationInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = IrrIgationInfo
        fields = '__all__'


class EcologyInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = EcologyInfo
        fields = '__all__'


class PlantingHistorySerializers(serializers.ModelSerializer):
    class Meta:
        model = PlantingHistory
        fields = '__all__'


class QuestionnaireSerializers(serializers.ModelSerializer):
    class Meta:
        model = Questionnaire
        fields = '__all__'


class DailySerializers(serializers.ModelSerializer):
    class Meta:
        model = Daily
        fields = '__all__'


class OtherSerializers(serializers.ModelSerializer):
    class Meta:
        model = Other
        fields = '__all__'
