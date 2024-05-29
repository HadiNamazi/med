from django.shortcuts import render

def add_patient(req):
    return render(req, 'app/add_patient.html', {})

def add_hospital(req):
    return render(req, 'app/add_hospital.html', {})

def login_view(req):
    return render(req, 'app/login_page.html', {})