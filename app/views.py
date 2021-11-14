from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import UserInfo, CurrencyInfo, PlantInfo, IrrIgationInfo, EcologyInfo, PlantingHistory, Questionnaire, \
    Daily, Other
from app.serializers import UserInfoSerializers, CurrencyInfoSerializers, PlantInfoSerializers, \
    IrrIgationInfoSerializers, EcologyInfoSerializers, PlantingHistorySerializers, QuestionnaireSerializers, \
    DailySerializers, OtherSerializers

'''UserInfo   '''


class UserInfoAPIView(APIView):
    serializer_class = UserInfoSerializers

    def get_queryset(self):
        queryset = UserInfo.objects.all()
        userId = self.request.query_params.get('userId', None)
        if userId:
            queryset = queryset.filter(userId=userId)
        return queryset

    # get 方法
    def get(self, request, *args, **kwargs):
        try:
            id = request.query_params["id"]
            if id != None:
                userinfo = UserInfo.objects.get(id=id)
                serializer = UserInfoSerializers(userinfo)
        except:
            userinfo = self.get_queryset()
            serializer = UserInfoSerializers(userinfo, many=True)
        return Response(serializer.data)

    # Post 方法
    def post(self, request, *args, **kwargs):
        user_data = request.data
        new_user = UserInfo.objects.create(userId=user_data["userId"]
                                           , name=user_data["name"]
                                           , phoneNum=user_data["phoneNum"]
                                           , address=user_data["address"]
                                           , avatarSprte=user_data["avatarSprte"]
                                           , signUpDate=user_data["signUpDate"])
        new_user.save()
        serializer = UserInfoSerializers(new_user)
        return Response(serializer.data)

    # Put 方法
    def put(self, request, *args, **kwargs):
        userId = request.query_params["userId"]
        user_object = UserInfo.objects.get(userId=userId)
        data = request.data
        user_object.userId = data["userId"]
        user_object.name = data["name"]
        user_object.phoneNum = data["phoneNum"]
        user_object.address = data["address"]
        user_object.avatarSprte = data["avatarSprte"]
        user_object.signUpDate = data["signUpDate"]
        print(user_object)
        user_object.save()
        serializer = UserInfoSerializers(user_object)
        return Response(serializer.data)

    # delete
    def delete(self, request, *args, **kwargs):
        userId = request.query_params["userId"]
        user_object = UserInfo.objects.filter(userId=userId)
        user_object.delete()
        serializer = UserInfoSerializers(user_object)
        return Response("data have been deleted!!")


class CurrencyInfoAPIView(APIView):
    def get_queryset(self):
        queryset = CurrencyInfo.objects.all()
        userId = self.request.query_params.get('userId', None)
        if userId:
            queryset = queryset.filter(userId=userId)
        return queryset

    # get 方法
    def get(self, request, *args, **kwargs):
        try:
            id = request.query_params["id"]
            if id != None:
                cueerncyInfo = CurrencyInfo.objects.get(id=id)
                serializer = CurrencyInfoSerializers(cueerncyInfo)
        except:
            cueerncyInfo = self.get_queryset()
            serializer = CurrencyInfoSerializers(cueerncyInfo, many=True)
        return Response(serializer.data)

    # Post 方法
    def post(self, request, *args, **kwargs):
        currencyInfo_data = request.data
        new_currency_info = CurrencyInfo.objects.create(userId=currencyInfo_data["userId"]
                                                        , gold=currencyInfo_data["gold"]
                                                        , water=currencyInfo_data["water"]
                                                        , ferilize=currencyInfo_data["ferilize"]
                                                        )
        new_currency_info.save()
        serializer = CurrencyInfoSerializers(new_currency_info)
        return Response(serializer.data)

    # Put
    def put(self, request, *args, **kwargs):
        userId = request.query_params["userId"]
        user_object = CurrencyInfo.objects.get(userId=userId)
        data = request.data
        user_object.userId = data["userId"]
        user_object.gold = data["gold"]
        user_object.water = data["water"]
        user_object.ferilize = data["ferilize"]
        user_object.save()
        serializer = CurrencyInfoSerializers(user_object)
        return Response(serializer.data)

    # delete
    def delete(self, request, *args, **kwargs):
        userId = request.query_params["userId"]
        user_object = CurrencyInfo.objects.filter(userId=userId)
        user_object.delete()
        serializer = CurrencyInfoSerializers(user_object)
        return Response("data have been deleted!!")


class PlantInfoAPIView(APIView):
    def get_queryset(self):
        queryset = PlantInfo.objects.all()
        userId = self.request.query_params.get('userId', None)
        if userId:
            queryset = queryset.filter(userId=userId)
        return queryset

    # get 方法
    def get(self, request, *args, **kwargs):
        try:
            id = request.query_params["id"]
            if id != None:
                plantInfo = PlantInfo.objects.get(id=id)
                serializer = PlantInfoSerializers(plantInfo)
        except:
            plantInfo = self.get_queryset()
            serializer = PlantInfoSerializers(plantInfo, many=True)
        return Response(serializer.data)

        # Post 方法

    def post(self, request, *args, **kwargs):
        plantInfo_data = request.data
        plant_info = PlantInfo.objects.create(userId=plantInfo_data["userId"]
                                              , fieldID=plantInfo_data["fieldID"]
                                              , plantngTime=plantInfo_data["plantngTime"]
                                              , currentWaterngCount=plantInfo_data["currentWaterngCount"]
                                              , currentFerilizeCount=plantInfo_data["currentFerilizeCount"]
                                              , lastWaterTime=plantInfo_data["lastWaterTime"]
                                              , lastFerilizeTine=plantInfo_data["lastFerilizeTine"]
                                              )
        plant_info.save()
        serializer = PlantInfoSerializers(plant_info)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        userId = request.query_params["userId"]
        user_object = PlantInfo.objects.get(userId=userId)
        data = request.data
        user_object.userId = data["userId"]
        user_object.fieldID = data["fieldID"]
        user_object.plantngTime = data["plantngTime"]
        user_object.currentWaterngCount = data["currentWaterngCount"]
        user_object.currentFerilizeCount = data["currentFerilizeCount"]
        user_object.lastWaterTime = data["lastWaterTime"]
        user_object.lastFerilizeTine = data["lastFerilizeTine"]
        user_object.save()
        serializer = PlantInfoSerializers(user_object)
        return Response(serializer.data)

        # delete

    def delete(self, request, *args, **kwargs):
        userId = request.query_params["userId"]
        user_object = PlantInfo.objects.filter(userId=userId)
        user_object.delete()
        serializer = PlantInfoSerializers(user_object)
        return Response("data have been deleted!!")


class IrrIgationInfoAPIView(APIView):

    def get_queryset(self):
        queryset = IrrIgationInfo.objects.all()
        userId = self.request.query_params.get('userId', None)
        if userId:
            queryset = queryset.filter(userId=userId)
        return queryset

        # get 方法

    def get(self, request, *args, **kwargs):
        try:
            id = request.query_params["id"]
            if id != None:
                irrIgationInfo = IrrIgationInfo.objects.get(id=id)
                serializer = IrrIgationInfoSerializers(irrIgationInfo)
        except:
            irrIgationInfo = self.get_queryset()
            serializer = IrrIgationInfoSerializers(irrIgationInfo, many=True)
        return Response(serializer.data)


        # Post 方法
    def post(self, request, *args, **kwargs):
        data = request.data
        irrigation_info = IrrIgationInfo.objects.create(userId=data["userId"]
                                              , waterNum=data["waterNum"]
                                              , lastWaterSpownTime=data["lastWaterSpownTime"]
                                              )
        irrigation_info.save()
        serializer = IrrIgationInfoSerializers(irrigation_info)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        userId = request.query_params["userId"]
        object = IrrIgationInfo.objects.get(userId=userId)
        data = request.data
        object.userId = data["userId"]
        object.waterNum = data["waterNum"]
        object.lastWaterSpownTime = data["lastWaterSpownTime"]
        object.save()
        serializer = IrrIgationInfoSerializers(object)
        return Response(serializer.data)

        # delete

    def delete(self, request, *args, **kwargs):
        userId = request.query_params["userId"]
        object = IrrIgationInfo.objects.filter(userId=userId)
        object.delete()
        serializer = IrrIgationInfoSerializers(object)
        return Response("data have been deleted!!")


class EcologyInfoAPIView(APIView):

    def get_queryset(self):
        queryset = EcologyInfo.objects.all()
        userId = self.request.query_params.get('userId', None)
        if userId:
            queryset = queryset.filter(userId=userId)
        return queryset

        # get 方法

    def get(self, request, *args, **kwargs):
        try:
            id = request.query_params["id"]
            if id != None:
                info = EcologyInfo.objects.get(id=id)
                serializer = EcologyInfoSerializers(info)
        except:
            info = self.get_queryset()
            serializer = EcologyInfoSerializers(info, many=True)
        return Response(serializer.data)


        # Post 方法
    def post(self, request, *args, **kwargs):
        data = request.data
        info = EcologyInfo.objects.create(userId=data["userId"]
                                              , weedsNum=data["weedsNum"]
                                              , offlineTime=data["offlineTime"]
                                              )
        info.save()
        serializer = EcologyInfoSerializers(info)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        userId = request.query_params["userId"]
        object = EcologyInfo.objects.get(userId=userId)
        data = request.data
        object.userId = data["userId"]
        object.weedsNum = data["weedsNum"]
        object.offlineTime = data["offlineTime"]
        object.save()
        serializer = EcologyInfoSerializers(object)
        return Response(serializer.data)

        # delete

    def delete(self, request, *args, **kwargs):
        userId = request.query_params["userId"]
        object = EcologyInfo.objects.filter(userId=userId)
        object.delete()
        serializer = EcologyInfoSerializers(object)
        return Response("data have been deleted!!")


class PlantHistoryAPIView(APIView):
    def get_queryset(self):
        queryset = PlantingHistory.objects.all()
        userId = self.request.query_params.get('userId', None)
        if userId:
            queryset = queryset.filter(userId=userId)
        return queryset

        # get 方法

    def get(self, request, *args, **kwargs):
        try:
            id = request.query_params["id"]
            if id != None:
                info = PlantingHistory.objects.get(id=id)
                serializer = PlantingHistorySerializers(info)
        except:
            info = self.get_queryset()
            serializer = PlantingHistorySerializers(info, many=True)
        return Response(serializer.data)

        # Post 方法

    def post(self, request, *args, **kwargs):
        data = request.data
        info = PlantingHistory.objects.create(userId=data["userId"]
                                          , fieldID=data["fieldID"]
                                          , plantingTime=data["plantingTime"]
                                          , harvestTime=data["harvestTime"]
                                          , reward=data["reward"]
                                          )
        info.save()
        serializer = PlantingHistorySerializers(info)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        userId = request.query_params["userId"]
        harvestTime = request.query_params['harvestTime']
        object = PlantingHistory.objects.get(userId=userId,harvestTime=harvestTime)
        data = request.data
        object.userId = data["userId"]
        object.fieldID = data["fieldID"]
        object.plantingTime = data["plantingTime"]
        object.harvestTime = data["harvestTime"]
        object.reward = data["reward"]
        object.save()
        serializer = PlantingHistorySerializers(object)
        return Response(serializer.data)

        # delete

    def delete(self, request, *args, **kwargs):
        userId = request.query_params["userId"]
        object = PlantingHistory.objects.filter(userId=userId)
        object.delete()
        serializer = PlantingHistorySerializers(object)
        return Response("data have been deleted!!")

'''QuestionAPIView'''
class QuestionAPIView(APIView):
    def get_queryset(self):
        queryset = Questionnaire.objects.all()
        userId = self.request.query_params.get('userId', None)
        if userId:
            queryset = queryset.filter(userId=userId)
        return queryset

    # get 方法
    def get(self, request, *args, **kwargs):
        try:
            id = request.query_params["id"]
            if id != None:
                info = Questionnaire.objects.get(id=id)
                serializer = QuestionnaireSerializers(info)
        except:
            info = self.get_queryset()
            serializer = QuestionnaireSerializers(info, many=True)
        return Response(serializer.data)

    # Post 方法
    def post(self, request, *args, **kwargs):
        data = request.data
        info = Questionnaire.objects.create(userId=data["userId"]
                                              , date=data["date"]
                                              , topicAndOptions=data["topicAndOptions"]
                                              , choose=data["choose"]
                                              )
        info.save()
        serializer = QuestionnaireSerializers(info)
        return Response(serializer.data)

    '''update'''
    def put(self, request, *args, **kwargs):
        userId = request.query_params["userId"]
        object = Questionnaire.objects.get(userId=userId)
        data = request.data
        object.userId = data["userId"]
        object.date = data["date"]
        object.topicAndOptions = data["topicAndOptions"]
        object.choose = data["choose"]
        object.save()
        serializer = QuestionnaireSerializers(object)
        return Response(serializer.data)

    # delete
    def delete(self, request, *args, **kwargs):
        userId = request.query_params["userId"]
        object = Questionnaire.objects.filter(userId=userId)
        object.delete()
        serializer = QuestionnaireSerializers(object)
        return Response("data have been deleted!!")


'''QuestionAPIView'''
class DailyAPIView(APIView):
    def get_queryset(self):
        queryset = Daily.objects.all()
        userId = self.request.query_params.get('userId', None)
        if userId:
            queryset = queryset.filter(userId=userId)
        return queryset

    # get 方法
    def get(self, request, *args, **kwargs):
        try:
            id = request.query_params["id"]
            if id != None:
                info = Daily.objects.get(id=id)
                serializer = DailySerializers(info)
        except:
            info = self.get_queryset()
            serializer = DailySerializers(info, many=True)
        return Response(serializer.data)

    # Post 方法
    def post(self, request, *args, **kwargs):
        data = request.data
        info = Daily.objects.create(userId=data["userId"]
                                              , date=data["date"]
                                              , pumpGetTime=data["pumpGetTime"]
                                              , fertilizeGetTimes=data["fertilizeGetTimes"]
                                              )
        info.save()
        serializer = DailySerializers(info)
        return Response(serializer.data)

    '''update'''
    def put(self, request, *args, **kwargs):
        userId = request.query_params["userId"]
        object = Daily.objects.get(userId=userId)
        data = request.data
        object.userId = data["userId"]
        object.date = data["date"]
        object.pumpGetTime = data["pumpGetTime"]
        object.fertilizeGetTimes = data["fertilizeGetTimes"]
        object.save()
        serializer = DailySerializers(object)
        return Response(serializer.data)

    # delete
    def delete(self, request, *args, **kwargs):
        userId = request.query_params["userId"]
        object = Daily.objects.filter(userId=userId)
        object.delete()
        serializer = DailySerializers(object)
        return Response("data have been deleted!!")


'''QuestionAPIView'''
class OtherAPIView(APIView):
    def get_queryset(self):
        queryset = Other.objects.all()
        userId = self.request.query_params.get('userId', None)
        if userId:
            queryset = queryset.filter(userId=userId)
        return queryset

    # get 方法
    def get(self, request, *args, **kwargs):
        try:
            id = request.query_params["id"]
            if id != None:
                info = Other.objects.get(id=id)
                serializer = OtherSerializers(info)
        except:
            info = self.get_queryset()
            serializer = OtherSerializers(info, many=True)
        return Response(serializer.data)

    # Post 方法
    def post(self, request, *args, **kwargs):
        data = request.data
        info = Other.objects.create(userId=data["userId"]
                                              , watchedArticlesId=data["watchedArticlesId"]
                                              )
        info.save()
        serializer = OtherSerializers(info)
        return Response(serializer.data)

    '''update'''
    def put(self, request, *args, **kwargs):
        userId = request.query_params["userId"]
        object = Other.objects.get(userId=userId)
        data = request.data
        object.userId = data["userId"]
        object.watchedArticlesId = data["watchedArticlesId"]
        object.save()
        serializer = OtherSerializers(object)
        return Response(serializer.data)

    # delete
    def delete(self, request, *args, **kwargs):
        userId = request.query_params["userId"]
        object = Other.objects.filter(userId=userId)
        object.delete()
        serializer = OtherSerializers(object)
        return Response("data have been deleted!!")



