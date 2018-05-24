from django.contrib import admin

# Register your models here.
from cars.models import Car

class CarAdmin(admin.ModelAdmin):
    list_display = ('no', 'plate_number', 'date', 'why', 'mode', 'accept')
    search_fields = ('plate_number',)

admin.site.register(Car, CarAdmin)