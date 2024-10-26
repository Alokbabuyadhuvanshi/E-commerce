from django.shortcuts import render,redirect
from .models import Product,Category
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, UpdateUserForm
from django import forms
from django.views.decorators.cache import never_cache

# Create your views here.
@never_cache
def home(request):
    products = Product.objects.all()
    return render(request, "home.html",{'products':products})

@never_cache
def product(request,pk):
    product = Product.objects.get(id=pk)
    return render(request, "product.html",{'product':product})

@never_cache
def category(request, foo):
    #replace the Hyphens with Spaces
    foo = foo.replace('-', ' ')
    #Grab the category from the url
    try:
        category = Category.objects.get(name = foo)
        products = Product.objects.filter(category = category)
        return render(request, 'category.html',{'products':products,'category':category})
    except:
        messages.success(request,("That Category Doesn't Exists..."))
        return redirect('home')


@never_cache
def about(request):
    return render(request, "about.html")

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You Have Been Logged In!"))
            return redirect('home')
        else:
            messages.success(request, ("Bad Credintials"))
            return redirect('login')
    else:
        return render(request, "login.html",{})

def logout_user(request):
    logout(request)
    messages.success(request, ("You have been logged out...Thanks for stopping by."))
    return redirect('home')
    

def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request, user)
            messages.success(request, ("You have Registered Successfully!! Welcome!"))
            return redirect('home')
        else:
            messages.success(request, ("Whoops! There was a problem in Registering, please try again..."))
            return redirect('register')

    return render(request, 'register.html', {'form':form})

def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        user_form = UpdateUserForm(request.POST or None,instance=current_user)

        if user_form.is_valid():
            user_form.save()

            login(request, current_user)
            messages.success(request, ("You have updated your profile successfully!!"))
            return redirect('home')
        return render(request, "update_user.html",{'user_form':user_form})
    else:
        messages.success(request, ("You Must Be Logged In!!"))
        return redirect('home')


def category_summary(request):
    categories = Category.objects.all()
    return render(request, 'category_summary.html', {'categories':categories})