from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponseBadRequest
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib import messages
from . forms import *
from . models import *
from django.db.models import Count

# Create your views here.

def index(request):
    category = Category.objects.all().order_by('id')
    trolley = Shopcart.objects.filter(user__username=request.user.username, paid=False)
    product = Product.objects.all().order_by('id')
    goods = Paginator(product, 10)
    mygoods = request.GET.get('page')
    mygoods_good = goods.get_page(mygoods)

    subtotal = 0
    vat = 0
    total = 0

    for cart in trolley:
        subtotal += cart.price * cart.quantity

    vat = 0.075 * subtotal

    total = subtotal + vat

    context = {
        'category': category,
        # 'categories':categories,
        'mygoods_good':mygoods_good,
        'trolley':trolley,
        'total':total,
    }
    return render(request, 'index.html', context)

def categories(request, slug):
    categories = Product.objects.filter(category__slug=slug)
    trolley = Shopcart.objects.filter(user__username=request.user.username, paid=False)
    goods = Paginator(categories, 8)
    mygoodies = request.GET.get('page')
    mycat_goodies = goods.get_page(mygoodies)
    context= {
        'mycat_goodies':mycat_goodies,
        'categories':categories,
        'trolley':trolley,
    }
    # return redirect('categories')
    return render(request, 'category.html', context)

def product_details(request, slug):
    profile = Profile.objects.filter(user__username=request.user.username)
    product = get_object_or_404(Product.objects.annotate(num_reviews = Count('reviews')), slug=slug)
    form = ReviewsForm()
    if request.method == "POST":
        form = ReviewsForm(request.POST)
        if form.is_valid():
            reviews = form.save(commit = False)
            reviews.product = product
            if request.user.is_authenticated:
                review.user = request.user
            reviews.save()
            messages.success(request, "Thank you for patronizing us!...")
            return redirect("product_details", slug=product.slug)
        else:
            messages.error(request, form.errors)
            form = ReviewsForm()
            return redirect('product_details')
    context = {
        'product':product,
        'form': form,
        'profile': profile,
    }
    return render(request, "details.html", context)

def modal_details(request, slug):
    product = get_object_or_404(Product, slug=slug)
    context = {
        'product':product,
    }
    return redirect('index', slug=slug)

def userLogin(request):
    context = {'show_modal': False}

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome to 24/7 wardrobe, {user.username}")
            return redirect('index')
        else:
            context['show_modal'] = True  # Set 'show_modal' to True if authentication fails
    else:
        if 'next' in request.GET:
            context['show_modal'] = True  # Set 'show_modal' to True if 'next' parameter is present

    # Render the login page with the context
    return redirect('index')


def userReg(request):
    form = SignupForm()
    if request.method == "POST":
        address = request.POST["address"]
        city = request.POST["city"]
        state = request.POST["state"]
        pix = request.POST["pix"]
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            newprofile = Profile(user=user)
            newprofile.first_name = user.first_name
            newprofile.last_name = user.last_name
            newprofile.email = user.email
            newprofile.address = address
            newprofile.state = state
            newprofile.city = city
            newprofile.pix = pix 
            newprofile.save()
            print("registered")
            messages.success(request, f"Welcome to 24/7 wardrobe, {user.username}!..Please sign in your account to see more on 247/Wradrobe")
            return redirect("profile")
        else:
            print("not registered")
            messages.error(request, form.errors)
            return redirect("userReg")
    return redirect("userReg")


@login_required(login_url='index')
def userSignout(request):
    logout(request)
    return redirect('index') 

@login_required(login_url="index")
def profile(request):
    profile = Profile.objects.get(user__username=request.user.username)
    trolley = Shopcart.objects.filter(user__username=request.user.username, paid=False)

    subtotal = 0
    vat = 0
    total = 0

    for cart in trolley:
        subtotal += cart.price * cart.quantity

    vat = 0.075 * subtotal

    total = subtotal + vat

    context = {
        'trolley':trolley,
        'profile': profile,
        'subtotal':subtotal,
        'total':total,
        'vat':vat,
    }
    return render(request, "profile.html", context)

@login_required(login_url="index")
def profile_update(request):
    profile = Profile.objects.get(user__username=request.user.username)
    update = ProfileUpdateForm(instance= request.user.profile)
    if request.method == 'POST':
        update = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if update.is_valid():
            update.save()
            messages.success(request, "Profile Updated successfully!...")
            return redirect("profile")
        else:
            messages.error(request, update.errors)
            return redirect("profile_update")
    return redirect('profile')

@login_required(login_url="userLogin")
def shopcart(request, id):
    if request.method == "POST":
        quantity = request.POST.get("quantity", 1)  # Set a default quantity of 1 if not provided
        product_id = request.POST.get("product_id")
        size = request.POST.get("size")
        color = request.POST.get("color")

        # Ensure product_id is not empty before attempting to fetch the product
        if product_id:
            product = Product.objects.get(pk=product_id)
            order_num = Profile.objects.get(user__username=request.user.username)
            cart_no = order_num.id

            cart = Shopcart.objects.filter(user__username=request.user.username, paid=False)
            if cart:
                basket = Shopcart.objects.filter(user__username=request.user.username, product_id=product.id, paid=False).first()
                if basket:
                    basket.quantity += int(quantity)
                    basket.amount = basket.quantity * basket.price
                    basket.save()
                    messages.success(request, f"{product.name} has been added to the cart successfully!")
                    return redirect('index')
                else:
                    new_basket = Shopcart()
                    new_basket.user = request.user
                    new_basket.product = product
                    new_basket.name = product.name
                    new_basket.price = product.stockPrice
                    new_basket.quantity = int(quantity)
                    new_basket.order_no = cart_no
                    new_basket.paid = False
                    new_basket.size = size
                    new_basket.color = color
                    new_basket.amount = product.stockPrice * int(quantity)
                    new_basket.save()
                    messages.success(request, f"{product.name} has been added to the cart successfully!")
                    return redirect('index')
            else:
                new_basket = Shopcart()
                new_basket.user = request.user
                new_basket.product = product
                new_basket.name = product.name
                new_basket.price = product.stockPrice
                new_basket.quantity = int(quantity)
                new_basket.order_no = cart_no
                new_basket.paid = False
                new_basket.size = size
                new_basket.color = color
                new_basket.amount = product.stockPrice * int(quantity)
                new_basket.save()
                messages.success(request, f"{product.name} has been added to the cart successfully!")
                return redirect('index')
        else:
            # Handle the case where product_id is not provided or empty
            messages.error(request, "Invalid product selection.")
            return redirect('index')
    return redirect('index')


@login_required(login_url="index")
def cart(request):
    profile = Profile.objects.get(user__username=request.user.username)
    trolley = Shopcart.objects.filter(user__username=request.user.username, paid=False)

    subtotal = 0
    vat = 0
    total = 0

    for cart in trolley:
        subtotal += cart.price * cart.quantity

    vat = 0.075 * subtotal

    total = subtotal + vat

    context = {
        'trolley':trolley,
        'profile': profile,
        'subtotal':subtotal,
        'total':total,
        'vat':vat,
    }
    return render(request, 'index.html', context)


def delete_cart(request):
    if request.method == 'POST':
        items_id = request.POST["items_id"]
        cartdelete = Shopcart.objects.get(pk=items_id)
        cartdelete.delete()
        messages.success(request, "Successfully Deleted")
        return redirect('index')
    else:
        messages.error(request, "There was an issue trying to delete cart. Check if you are authenticated.")
        return redirect("index")
    return redirect('index')

def delallcart(request):
    if request.method == "POST":
        allcart_id = request.POST.get("allcart")  # Get the 'allcart' value from the POST data
        try:
            delcart = Shopcart.objects.get(pk=allcart_id)
            delcart.shopcartitem_set.all().delete()
            messages.success(request, "Cart deleted")
        except Shopcart.DoesNotExist:
            messages.error(request, "Cart not found")
    return redirect('index')

# def delallcart(request):
#     if request.method == "POST":
#         # You may need to identify the cart based on user-specific information, like a session or cookie
#         # For example, if you're using session-based carts:
#         cart_id = request.session.get("cart_id")

#         if cart_id:
#             try:
#                 cart = Shopcart.objects.get(pk=cart_id)
#                 cart.shopcartitem_set.all().delete()
#                 messages.success(request, "Cart deleted")
#             except Shopcart.DoesNotExist:
#                 messages.error(request, "Cart not found")
#         else:
#             messages.error(request, "Cart not found")

#     return redirect('index')

# def delallcart(request):
#     if request.method == "POST":
#         allcart_id = request.POST.get("allcart")

#         try:
#             delcart = Shopcart.objects.get(pk=allcart_id)
#             delcart.shopcartitem_set.all().delete()
#             messages.success(request, "Cart deleted")
#         except Shopcart.DoesNotExist:
#             messages.error(request, "Cart not found")

#     return redirect('index')






























































# @login_required(login_url="index")
# def cart(request):
#     if request.method == "POST":
#         quantity = int(request.POST["quantity"])
#         product_id = request.POST["product_id"]
#         size = request.POST["size"]
#         color = request.POST["color"]
#         product = Product.objects.get(pk=product_id)
#         order_num = Profile.objects.get(user__username =request.user.username)
#         cart_no = order_num.id

#         cart = Shopcart.objects.filter(user__username=request.user.username, paid= False)
#         if cart:
#             basket = Shopcart.objects.filter(user__username=request.user.username, product_id=product.id, paid=False).first()
#             if basket:
#                 basket.quantity += quantity
#                 basket.amount = basket.quantity * basket.price
#                 basket.save()
#                 messages.success(request, f"{product.name} has been added to cart successfully!..")
#                 return redirect('index')
#             else:
#                 new_basket = Shopcart()
#                 new_basket.user = request.user
#                 new_basket.product = product
#                 new_basket.name = product.name 
#                 new_basket.price = product.stockPrice
#                 new_basket.quantity = int(quantity)
#                 new_basket.order_no = cart_no
#                 new_basket.paid = False
#                 new_basket.size = size
#                 new_basket.color = color
#                 new_basket.amount = product.stockPrice * quantity
#                 new_basket.save()
#                 messages.success(request, f"{product.name} has been added to cart successfully!..")
#                 return redirect('index')
#         else:
#             new_basket = Shopcart()
#             new_basket.user = request.user
#             new_basket.product = product
#             new_basket.name = product.name 
#             new_basket.price = product.stockPrice
#             new_basket.quantity = int(quantity)
#             new_basket.order_no = cart_no
#             new_basket.paid = False
#             new_basket.size = size
#             new_basket.color = color
#             new_basket.amount = product.stockPrice * quantity
#             new_basket.save()
#             messages.success(request, f"{product.name} has been added to cart successfully!..")
#             return redirect('index')
#         return redirect('index')
# @login_required(login_url='index')