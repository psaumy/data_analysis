from django.contrib import admin

# Register your models here.
from .models import Passenger, ADR


class PassengerAdmin(admin.ModelAdmin):
    list_display = ('name', 'survived', 'gender', 'embarked',)

admin.site.register(Passenger, PassengerAdmin)



class ADRAdmin(admin.ModelAdmin):
    list_display = ('load','cyl1','cyl2','cyl3','mean','cov','rsr','unknwn')

admin.site.register(ADR, ADRAdmin)