from django.shortcuts import render
from .models import Login
from .forms import LoginForm
# Create your views here.

def index(request):
    if request.method == "POST":
        # Username = request.POST.get('username')
        # Password = request.POST.get('password')
        # a = Login(username =Username, password=Password)
        a = LoginForm(request.POST)
        a.save()
        
    return render(request, "login/index.html" , {'fo' : LoginForm})