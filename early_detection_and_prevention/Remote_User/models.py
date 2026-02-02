from django.db import models

# Create your models here.
from django.db.models import CASCADE


class ClientRegister_Model(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=10)
    phoneno = models.CharField(max_length=10)
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    gender= models.CharField(max_length=30)
    address= models.CharField(max_length=30)


class detect_malicious_user(models.Model):

    Fid= models.CharField(max_length=3000)
    Age= models.CharField(max_length=3000)
    Gender= models.CharField(max_length=3000)
    Street= models.CharField(max_length=3000)
    City= models.CharField(max_length=3000)
    Latitude= models.CharField(max_length=3000)
    Longitude= models.CharField(max_length=3000)
    Community= models.CharField(max_length=3000)
    Followers= models.CharField(max_length=3000)
    Retweets= models.CharField(max_length=3000)
    Likes= models.CharField(max_length=3000)
    Unlikes= models.CharField(max_length=3000)
    Prediction= models.CharField(max_length=3000)


class detection_accuracy(models.Model):

    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)

class detection_ratio(models.Model):

    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)



