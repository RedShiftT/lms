from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistrationForm

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/course/')
        else:
            messages.success(request, "Пароль неверный!")
            return render(request, 'accounts/auth.html', {'error': 'Invalid username or password.'})
    else:
        return render(request, 'accounts/auth.html')


def logout_view(request):
    logout(request)
    return redirect('login')


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
    else:
        form = RegistrationForm()
    return render(request, 'accounts/registration.html', {'form': form})
