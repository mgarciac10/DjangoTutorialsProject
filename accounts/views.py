from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.
class SignupView(TemplateView):
    template_name = 'register/signup.html'

    def get(self, request):
        form = UserCreationForm()
        context = {}
        context['form'] = form
        context['title'] = 'Sign up'
        return render(request, self.template_name, context)
    
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            login(request, form.instance)
            return redirect('home')
        context = {}
        context['form'] = form
        context['title'] = 'Sign up'
        return render(request, self.template_name, context)

class LogoutView(TemplateView):
    def get(self, request):
        logout(request)
        return redirect('home')

class LoginView(TemplateView):
    template_name = 'login/login.html'

    def get(self, request):
        form = AuthenticationForm()
        context = {}
        context['title'] = 'Login'
        context['form'] = form
        return render(request, self.template_name, context)
    
    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        context = {}
        context['title'] = 'Login'
        context['form'] = form
        return render(request, self.template_name, context)