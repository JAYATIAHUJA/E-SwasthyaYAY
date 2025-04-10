from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import CustomLoginForm, CustomRegistrationForm
from django.contrib.auth.views import LoginView

# Create your views here.

class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = 'accounts/login.html'

def register(request):
    if request.method == 'POST':
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('main:index')
    else:
        form = CustomRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})
