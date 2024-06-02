from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login-page'),
    path('', views.index, name='index'),
    path('form/add-patient/', views.add_patient, name='add-patient'),
    path('form/1/', views.form1, name='form1'),
    path('form/2/', views.form2, name='form2'),
    path('form/3/', views.form3, name='form3'),
    path('report/patient-base/', views.patient_base_report, name='patient-base-report'),

]
