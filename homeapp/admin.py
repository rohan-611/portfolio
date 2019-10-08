from django.contrib import admin
from homeapp.models import Contact, Testimonials

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ['__str__','responded',  'name']

    class Meta:
        modal = Contact

admin.site.register(Contact, ContactAdmin)
admin.site.register(Testimonials)