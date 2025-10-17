from django.contrib.auth import authenticate
from django.shortcuts import render
from django.views import View   # ✅ Correct import
from django.shortcuts import render,redirect
from users.forms import SignupForm

class Home(View):
    def get(self, request):
        return render(request, 'Home.html')

class Register(View):
    def get(self, request):
        form_instance = SignupForm()
        context = {'form': form_instance}
        return render(request, template_name='Register.html', context=context)

    def post(self, request):
        form_instance = SignupForm(request.POST)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('login')
        else:
            print('error')
            return render(request, template_name='register.html', context={'form': form_instance})

class Login(View):
    def post(self, request):
        form_instace=LoginForm(request.POST)
        if form_instace.is_valid():
            u=form_instace.cleaned_data['username']
            p = form_instace.cleaned_data['password']
            user = authenticate(username=u,password=p)
        if user and user.is_superuser==True:

             return render(request, 'login.html')

class Logout(View):
    def get(self, request):
        return render(request, 'logout.html')


class Adminhome(View):
    def get(self, request):
        return render(request, template_name='adminhome.html')

class Teacherhome(View):
    def get(self, request):
        return render(request, template_name='teacherhome.html')

class Studenthome(View):
    def get(self, request):
        return render(request, template_name='studenthome.html')
