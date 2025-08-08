from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login-page'),
    path('', views.index, name='index'),

    path('patients/', views.patients, name='patients'),
    path('patients/add-patient/', views.add_patient, name='add-patient'),
    path('patients/edit-patient/<str:cid>/', views.edit_patient, name='edit-patient'),
    path('patients/delete-patient/<str:cid>/', views.delete_patient, name='delete-patient'),

    path('form/1/', views.form1, name='form1'),
    path('form/2/', views.form2, name='form2'),
    path('form/3/', views.form3, name='form3'),

    path('report/patient-base/single-patient/', views.patient_base_report, name='single-patient-report'),
    path('report/patient-base/multi-patient/', views.multi_patient_report, name='multi-patient-report'),
    path('report/form-base/1/', views.form1_base_report, name='form1-base-report'),
    path('report/form-base/2/', views.form2_base_report, name='form2-base-report'),
    path('report/form-base/3/', views.form3_base_report, name='form3-base-report'),

    path('show-form/1/<str:id>/', views.show_form1, name='showform1'),
    path('show-form/2/<str:id>/', views.show_form2, name='showform2'),
    path('show-form/3/<str:id>/', views.show_form3, name='showform3'),
    
    path('edit-form/1/<str:id>/', views.edit_form1, name='editform1'),
    path('edit-form/2/<str:id>/', views.edit_form2, name='editform2'),
    path('edit-form/3/<str:id>/', views.edit_form3, name='editform3'),

    path('delete-form/1/<str:id>/', views.delete_form1, name='deleteform1'),
    path('delete-form/2/<str:id>/', views.delete_form2, name='deleteform2'),
    path('delete-form/3/<str:id>/', views.delete_form3, name='deleteform3'),

    path('excel-export-all/<str:formnum>/', views.excel_export_all, name='excel-export-all'),
    path('excel-export/<str:formnum>/<str:id>/', views.excel_export, name='excel-export'),
]
