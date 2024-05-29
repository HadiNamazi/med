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

class Hospital(models.Model):
    name = models.CharField(max_length=50)

class Patient(models.Model):
    name = models.CharField(max_length=50)
    national_code = models.CharField(max_length=10) #should be validated
    phone_num = models.CharField(max_length=14)
    mobile_phone_num = models.CharField(max_length=11)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    image = models.ImageField(upload_to ='uploads/')
    address = models.TextField()

class PatientInfo(models.Model):
    # patient = models.OneToOneField()
    pass