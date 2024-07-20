from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

# Create your views here.
def signup (request):
   
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        email = request.POST['email']


        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                print('Username taken')
            elif User.objects.filter(email=email).exists():
                print('Email taken')

            else:
                user = User.objects.create_user(username=username, password=confirm_password, email=email, first_name=first_name, last_name=last_name)
                user.save();
                print('user created')
            
        else:
            print('Wrong Password')

        return redirect('/')
    else:
        return render(request, 'signup.html')