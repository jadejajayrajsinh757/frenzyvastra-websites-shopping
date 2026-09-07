from django.views.generic import TemplateView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .models import Product
from .forms import SignupForm, LoginForm


class AboutPageView(TemplateView):
    template_name = "about.html"


def mens_page(request):
    products = Product.objects.filter(is_active=True)
    return render(request, 'mens.html', {'products': products})


class WomensPageView(TemplateView):
    template_name = "womens.html"


def login_page(request):
    if request.user.is_authenticated:
        return redirect('seller_dashboard')
    form = LoginForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('about')
        else:
            form.add_error(None, 'Invalid username or password')
    return render(request, 'login.html', {'form': form})


def signup_page(request):
    if request.user.is_authenticated:
        return redirect('seller_dashboard')
    form = SignupForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        return redirect('login')
    return render(request, 'signup.html', {'form': form})


def logout_page(request):
    logout(request)
    return redirect('login')


def seller_dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'seller_dashboard.html')


def seller_add_product(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        product = Product()
        product.product_title = request.POST['product_title']
        product.product_price = request.POST['product_price']
        product.product_description = request.POST['product_description']
        product.available_qty = request.POST['available_qty']
        product.product_img = request.FILES['product_img']
        product.save()
        return redirect('seller_products')
    return render(request, 'seller_add_product.html')


def seller_products(request):
    if not request.user.is_authenticated:
        return redirect('login')
    products = Product.objects.all()
    return render(request, 'seller_products.html', {'products': products})


def seller_update_product(request, product_id):
    if not request.user.is_authenticated:
        return redirect('login')
    product = get_object_or_404(Product, product_id=product_id)
    if request.method == 'POST':
        product.product_title = request.POST['product_title']
        product.product_price = request.POST['product_price']
        product.product_description = request.POST['product_description']
        product.available_qty = request.POST['available_qty']
        product.is_active = 'is_active' in request.POST
        if 'product_img' in request.FILES:
            product.product_img = request.FILES['product_img']
        product.save()
        return redirect('seller_products')
    return render(request, 'seller_update_product.html', {'product': product})
