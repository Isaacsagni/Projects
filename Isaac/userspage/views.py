from django.shortcuts import render, redirect
from django.contrib import messages
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
                messages.info(request, 'Username taken')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email taken' )
                return redirect('signup')

            else:
                user = User.objects.create_user(username=username, password=confirm_password, email=email, first_name=first_name, last_name=last_name)
                user.save();
                print('user created')
            
        else:
            messages.info(request, 'Password Mismatch')
            return redirect('signup')

        return redirect('/')
    else:
        return render(request, 'signup.html')