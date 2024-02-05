from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User



def login(request):
     if request.method == 'POST':
        # Assuming you have a form for username and password
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        authenticated_user = authenticate(request, username=username, password=password)

        if authenticated_user is not None and authenticated_user.is_authenticated:
            login(request, authenticated_user)
            return redirect('home.html')  # Redirect to the home page after successful login
        else:
            # Authentication failed, handle accordingly
            return render(request, 'index.html', {'error_message': 'Authentication failed'})

    # For GET requests, return a render response
     return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        # Get form data from the request
        username = request.POST.get('Username')
        email = request.POST.get('Email')
        password = request.POST.get('Password')

        try:
            # Perform user creation
            user = User.objects.create_user(username=username, email=email, password=password)

            # Log in the user
            authenticated_user = authenticate(request, username=username, password=password)

            if authenticated_user is not None and authenticated_user.is_authenticated:
                return redirect('submit')
            else:
                # Authentication failed, handle accordingly
                return render(request, 'signup.html', {'error_message': 'Authentication failed'})

        except Exception as e:
            # Handle exceptions, e.g., username or email already exists
            return render(request, 'signup.html', {'error_message': str(e)})
        # For GET requests, return a render response
    return render(request, 'signup.html')
        
def submit(request):
    return render(request, 'submit.html') 

def home(request):
    return render(request, 'home.html')

def voting(request):
    return render(request, 'voting.html')

