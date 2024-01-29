from django.contrib import admin
from .models import User,profile,address
# Register your models here.
admin.site.register((User,profile,address))