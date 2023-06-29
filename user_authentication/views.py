from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from user_authentication.forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            print("User created")
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'user_authentication/register.html', {'form': form})




def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                print("User logged in")
                return redirect('home')  # Replace 'home' with your desired redirect URL
    else:
        form = AuthenticationForm()
    return render(request, 'user_authentication/login.html', {'form': form})