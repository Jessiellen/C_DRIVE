from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout

def index_view(request):
    return render(request, 'index.html')

def home_view(request):
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
                    return redirect('index')  
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
                return redirect('home') 
    else:
        form = UserCreationForm()
    return render(request, 'auth/signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index')  

# def search_view(request):
#     if 'q' in request.GET:
#         query = request.GET['q']
#         return render(request, 'search_results.html', {'query': query})
#     else:
#         return render(request, 'search_form.html')
