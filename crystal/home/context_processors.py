from . models import *

def profile(request):
    user = request.user
    profile = None

    if user.is_authenticated:
        try:
            profile = Profile.objects.get(user=user)
        except Profile.DoesNotExist:
            profile = None

    return {
        'user': user,
        'profile': profile,
    }

def cartcount(request):
    reading = Shopcart.objects.filter(user__username= request.user.username, paid=False)
    cartcount = 0
    for item in reading:
        cartcount += item.quantity
    context ={
        'cartcount':cartcount,
    }
    return context

def category(request):
    category = Category.objects.all()
    context = {
        'category': category
    }
    return context

def shopcart(request):
    trolley = Shopcart.objects.filter(user__username=request.user.username)
    context ={
        'trolley':trolley,
    }
    return context

