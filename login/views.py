from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# The following decorator ensures that the user has to be logged in to access the 'index' view,
# and if not, they are redirected to the 'login' page.
@login_required(login_url='login')
def index(request):
    # Renders the 'index.html' template when the user is logged in.
    return render(request, 'index.html')

# User Signup

def Signup(request):
    if request.method == 'POST':
        # Retrieve user registration information from the form.
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pwd = request.POST.get('password')
        cpwd = request.POST.get('confirmPassword')

        # Check if the password and confirmPassword match.
        
        if pwd != cpwd:
            return HttpResponse("Your password and confirmPassword do not match!")
        else:
            my_user = User.objects.create_user(uname, email, pwd)
            my_user.save()
            # Redirect to the 'login' page after successful registration.
            return redirect('login')

    # Renders the 'signup.html' template for GET requests.
    return render(request, 'signup.html')

# User Login
def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        passd = request.POST.get('password')

        # Authenticate the user using Django's authentication system.
        user = authenticate(request, username=username, password=passd)

        # log in the user and redirect to the 'index' page.
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            # If authentication fails, display an error message.
            return HttpResponse("Username & Password is incorrect!")

    # Renders the 'login.html' template for GET requests.
    return render(request, 'login.html')

# user Logout
def LogoutPage(request):
    # Log out the currently logged-in user and redirect to the 'login' page.
    logout(request)
    return redirect('login')
