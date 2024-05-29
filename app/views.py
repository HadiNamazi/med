from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import login
from . import models

PASSWORD = '***'

def index(req):
    if not req.user.is_authenticated:
        return redirect('login-page')

    return render(req, 'app/index.html', {})

def add_patient(req):
    if not req.user.is_authenticated:
        return redirect('login-page')

    return render(req, 'app/add_patient.html', {})

def add_hospital(req):
    if not req.user.is_authenticated:
        return redirect('login-page')
    
    return render(req, 'app/add_hospital.html', {})

def login_view(req):
    if req.user.is_authenticated:
        return redirect('index')

    if req.method == 'GET':
        return render(req, 'app/login_page.html', {})

    if req.method == 'POST':
        password = req.POST['password']
        user = models.CustomUser.objects.get(username='username')
        if password == PASSWORD:
            login(req, user)
            return redirect('index')
        return redirect('login-page')