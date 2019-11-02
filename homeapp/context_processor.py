from django.conf import settings

from portfolio.models import Profile

try:
    def get_profile():
        return Profile.objects.get(user__username="rohan")


    def profile(request):
        p = get_profile()
        return {
            'profile': p
        }

except NotImplemented('DB not implemented'):
    def profile():
        return {
            'profile': None
        }