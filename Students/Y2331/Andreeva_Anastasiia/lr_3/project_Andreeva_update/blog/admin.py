from django.contrib import admin

from .models import Owner, Car, Owning, Driver_license
admin.site.register(Owner)
admin.site.register(Car)
admin.site.register(Owning)
admin.site.register(Driver_license)