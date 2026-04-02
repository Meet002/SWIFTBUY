from django.http import JsonResponse
from django.shortcuts import render, redirect

from home.models import ClothingProduct, users
from django.contrib import messages
from home.models import Contact

# Create your views here.

def index(request):
    user_id = request.session.get('user_id')
    context = {}
    
    if user_id:
        # One clean call to the database
        user = users.objects.filter(id=user_id).first()
        if user:
            context['current_user'] = user

    return render(request, 'index.html', context)

def login_view(request):
    if request.method == 'POST':
        u_email = request.POST.get('email')
        u_pass = request.POST.get('password')

        user = users.objects.filter(email=u_email, password=u_pass).first()

        if user:
            request.session['user_id'] = user.id
            request.session['username'] = user.username

            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('home')
        else:
            messages.error(request, "Invalid email or password!")
            return redirect('login')

    return render(request, 'login.html')

def logout_view(request):
    # FIX: Actually clear the session so the user is "forgotten"
    request.session.flush()
    messages.info(request, "You have been logged out.")
    return redirect('login')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact_data = {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message
        }
        # FIX: Use the correct model name and create a new contact entry
        Contact.objects.create(**contact_data)
        messages.success(request, "Your message has been sent!")
        return redirect('contact')
    return render(request, 'contact.html')

def products(request): 
    products = ClothingProduct.objects.all()
    return render(request, 'products.html', {'products': products})

def testimonials(request):
    return render(request, 'testimonials.html')

def signup(request):
    if request.method == 'POST':
        # Handle signup logic here
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmPassword')

        # Basic Validation
        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect('signup')

        # Check if user already exists
        if users.objects.filter(username=username).exists():
            messages.error(request, "Username already taken!")
            return redirect('signup')

        signup_data = {
            'username': username,
            'email': email,
            'password': password,
            'confirmPassword': confirm_password
        }

        users.objects.create(**signup_data)
        messages.success(request, "Signup successful!")
        return redirect('login')
    return render(request, 'signup.html')


def product_detail(request, product_id):
    product = ClothingProduct.objects.get(id=product_id)
    return render(request, 'product_detail.html', {'product': product})
