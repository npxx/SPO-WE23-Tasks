from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    return render(request, 'index.html')

from .models import User

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = User(username=username)
        user.set_password(password)
        user.save()

        return redirect('index')

    return render(request, 'signup.html')

import bcrypt

def print_bcrypt_hash(password):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    print(hashed_password.decode('utf-8'))

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.get(username=username)

        if user is not None:
            if bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                print(f"User {username} successfully authenticated.")
                return render(request,'dashboard.html')
        else:
            print(f"Authentication failed for user {username}.")

        #Just for debugging purposes

        password_hash = user.password
        print(password_hash)
        print(f"Username entered : {username}, Password: {password}")
        print_bcrypt_hash(password)

    return render(request, 'login.html')

from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')
