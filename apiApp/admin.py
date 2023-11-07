from django.contrib import admin
from django.db.models import CharField
from django.db.models.functions import Length
from apiApp.models import *
# Register your models here.
admin.site.register(user_data)
CharField.register_lookup(Length, 'length')