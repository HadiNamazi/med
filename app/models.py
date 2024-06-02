from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        return self.create_user(username, password, **extra_fields)

    def get_by_natural_key(self, username):
        return self.get(username=username)

class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=50, unique=True)
    REQUIRED_FIELDS = ['password']
    USERNAME_FIELD = 'username'
    objects = UserManager()

class Patient(models.Model):
    cid = models.AutoField(primary_key=True, editable=True)
    name = models.CharField(max_length=50)
    national_code = models.CharField(max_length=10) #should be validated
    phone_num = models.CharField(max_length=14)
    mobile_phone_num = models.CharField(max_length=11)
    hospital = models.CharField(max_length=50) #hospital names should be revised
    image = models.ImageField(upload_to ='uploads/') #the quality should be controlled
    address = models.TextField()
    deleted = models.BooleanField(default=0)

class Form1(models.Model):
    data = models.JSONField()

class Form2(models.Model):
    data = models.JSONField()

class Form3(models.Model):
    data = models.JSONField()