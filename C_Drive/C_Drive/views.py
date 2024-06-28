from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

def index_view(request):
    return render(request, 'index.html')


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if user.is_staff:
                    return redirect('admin:index')
                else:
                    return redirect('home2')
    return render(request, 'auth/login.html', {'form': AuthenticationForm()})  

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            if user.is_staff:
                return redirect('admin:index')
            else:
                return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'auth/signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index')  


def drive_docs_view(request):
    user = request.user
    user_documents = YourModel.objects.filter(user_id=user.id)  
    return render(request, 'drive_docs/home.html', {'documents': user_documents})

def password_reset(request):
    if request.method == "GET":
        return render(request, 'auth/password_reset.html')
    elif request.method == "POST":
        username = request.POST.get('usernamereset')
        email = request.POST.get('emailreset')
        novasenha = request.POST.get('passwordreset')

        user = User.objects.filter(username=username, email=email).first()

        if user:
            user.password = make_password(novasenha)
            user.save()
            return redirect('login')  
        else:
            return render(request, 'formResetPassword.html', {'error': 'Usuário não encontrado'})

    return render(request, 'auth/password_reset.html')