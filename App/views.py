from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from App.forms import LoginForm

def login(request):
  return render(request, 'login.html')
  
@login_required
def home(request):
  return render(request, 'home.html')

def index(request):
  form=LoginForm(request.POST)
  if form.is_valid():
    username=form.cleaned_data.get("Name")
    password=form.cleaned_data.get("Password")
    user=authenticate(username=username,password=password)
    login(request,user)
  return render(request,'facebook.html',{'form':form})