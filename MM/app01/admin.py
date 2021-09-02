from django.contrib import admin

# Register your models here.
from app01.models import Cities,Hotels

class CitiesAdmin(admin.ModelAdmin):
    pass

admin.site.register(Cities,CitiesAdmin)


class HotelsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Hotels,HotelsAdmin)