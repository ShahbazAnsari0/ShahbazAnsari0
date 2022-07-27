from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render,redirect,render_to_response
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Login
from .models import Signup
from django.contrib.auth.models import User,auth
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'home.html')
def login(request):
    if request.method == 'POST':
        user = Signup.objects.get(username=request.POST['username'])

        if user.username==request.POST['username'] and user.password1 == request.POST['password1']:
            username = request.POST['username']
            password1 = request.POST['password1']
            user = Login()
            user.username = username
            user.password1 = password1
            user.save();
            return render(request, "profile.html")
        else:
            messages.error(request,"invalid")
            return render(request, "login.html")
    else:
        return render(request, "login.html")

def signup(request):
    if request.method == 'POST':
        username=request.POST['username']
        if Signup.objects.filter(username=username).exists():
            messages.add_message(request, messages.ERROR,'Username Already Exists!!!')
            return render(request,'signup.html')
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if not password1 == password2:
            messages.add_message(request, messages.ERROR, 'Passwords not matching.')

            return render(request,'signup.html')
        email = request.POST['email']
        gender=request.POST['gender']
        bday = request.POST['bday']
        number = request.POST['number']
        if not number.isdigit():
            messages.error(request, 'Wrong Contact no.')
            return render(request,'signup.html')
        address=request.POST['address']
        state=request.POST['state']
        city=request.POST['city']
        pin_code=request.POST['pin_code']


        user = Signup()
        user.username=username
        user.password1=password1
        user.password2 = password2
        user.email=email
        user.bday=bday
        user.gender=gender
        user.number=number
        user.address=address
        user.state=state
        user.city=city
        user.pin_code=pin_code
        user.save();
        print('success')
        data = Signup.objects.get(username=username)
        return render(request, "confirmation.html", {'data': data})
    else:
        return render(request,'signup.html')
def maps(request):
    return render(request,'maps.html')
def visitor(request):
    return render(request,'visitor.html')
def appointment(request):
    return render(request,'appointment.html')
def organ(request):
    return render(request,'organ.html')
def infrastructure(request):
    return render(request,'infrastructure.html')
def contact(request):
    return render(request,'contact.html')
def confirmation(request):
    data = Signup.objects.all()
    return render(request,"confirmation.html", {'data': data})

def achievement(request):
    return render(request,'achievement.html')
def overview(request):
    return render(request,'overview.html')
def logout(request):
    return render(request,'logout.html')
def profile(request):
    return render(request,'profile.html')

def home(request):
    return render(request,'home.html')
def slide(request):
    return render(request,'slide.html')