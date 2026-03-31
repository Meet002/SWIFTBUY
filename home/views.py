from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def login_view(request):
    # Handle login logic here
    return render(request, 'login.html')

def logout_view(request):
    # Handle logout logic here
    return render(request, 'logout.html')

