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

# def cart(request):