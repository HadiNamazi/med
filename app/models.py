from django.db import models


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