from django.conf import settings

from homeapp.models import Profile


def get_profile():
    return Profile.objects.get(user__username=settings.USER_NAME)


def profile(request):
    try:
        p = get_profile()
        return {
            'profile': p
        }
    except:
        return {
            'profile': None
        }
