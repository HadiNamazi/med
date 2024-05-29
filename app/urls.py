from django.urls import path
from . import views

urlpatterns = [
    path('add-patient/', views.add_patient, name='add-patient'),
    path('add-hospital/', views.add_hospital, name='add-hospital'),
    path('login/', views.login_view, name='login-url'),

]
