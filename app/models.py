from django.db import models


class UserInfo(models.Model):
    userId = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    phoneNum = models.CharField(max_length=20)
    address = models.TextField()
    avatarSprte = models.TextField()
    signUpDate = models.TextField()

    def __str__(self):
        return self.name


class CurrencyInfo(models.Model):
    userId = models.CharField(max_length=20)
    gold = models.IntegerField()
    water = models.IntegerField()
    ferilize = models.IntegerField()

    def __str__(self):
        return self.userId


class PlantInfo(models.Model):
    userId = models.CharField(max_length=20)
    fieldID = models.TextField()
    plantngTime = models.TextField()
    currentWaterngCount = models.IntegerField()
    currentFerilizeCount = models.IntegerField()
    lastWaterTime = models.TextField()
    lastFerilizeTine = models.TextField()

    def __str__(self):
        return self.userId


class IrrIgationInfo(models.Model):
    userId = models.CharField(max_length=20)
    waterNum = models.IntegerField()
    lastWaterSpownTime = models.TextField()

    def __str__(self):
        return self.userId


class EcologyInfo(models.Model):
    userId = models.CharField(max_length=20)
    weedsNum = models.IntegerField()
    offlineTime = models.TextField()

    def __str__(self):
        return self.userId


class PlantingHistory(models.Model):
    userId = models.CharField(max_length=20)
    fieldID = models.TextField()
    plantingTime = models.TextField()
    harvestTime = models.TextField()
    reward  = models.TextField()

    def __str__(self):
        return self.userId


class Questionnaire(models.Model):
    userId = models.CharField(max_length=20)
    date = models.TextField()
    topicAndOptions = models.TextField()
    choose = models.TextField()

    def __str__(self):
        return self.userId


class Daily(models.Model):
    userId = models.CharField(max_length=20)
    date = models.TextField()
    pumpGetTime = models.TextField()
    fertilizeGetTimes = models.IntegerField()

    def __str__(self):
        return self.userId


class Other(models.Model):
    userId = models.CharField(max_length=20)
    watchedArticlesId = models.TextField()

    def __str__(self):
        return self.userId

