from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
# Create your views here.

def custom_login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('staff_dashboard')
            else:
                return redirect('user_dashboard')
        else:
            messages.error(request, 'Error')
    return render(request, 'users/login.html')

def custom_logout_view(request):
    logout(request)
    return redirect('login')

class SignupView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/signup.html'

@login_required
@user_passes_test(lambda u: u.is_staff, login_url='/login/')
def staff_dashboard(request):
    return render(request, 'users/staff_dashboard.html')

@login_required
@user_passes_test(lambda u: not u.is_staff, login_url='/login/')
def user_dashboard(request):
    return render(request, 'users/user_dashboard.html')
