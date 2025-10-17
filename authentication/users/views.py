from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from users.forms import SignupForm, LoginForm


# Home Page
class home(View):
    def get(self, request):
        return render(request, 'Home.html')


# Register View
class Register(View):
    def get(self, request):
        form_instance = SignupForm()
        return render(request, 'register.html', {'form': form_instance})

    def post(self, request):
        form_instance = SignupForm(request.POST)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('users:login')
        return render(request, 'register.html', {'form': form_instance})


# Login View
class UserLogin(View):
    def get(self, request):
        form_instance = LoginForm()
        return render(request, 'login.html', {'form': form_instance})

    def post(self, request):
        form_instance = LoginForm(request.POST)
        if form_instance.is_valid():
            u = form_instance.cleaned_data['username']
            p = form_instance.cleaned_data['password']
            user = authenticate(username=u, password=p)

            if user:
                login(request, user)
                return redirect('users:home')
            else:
                print("Invalid credentials")

        return render(request, 'login.html', {'form': form_instance})


# Logout View
class UserLogout(View):
    def get(self, request):
        logout(request)
        return redirect('users:login')
























