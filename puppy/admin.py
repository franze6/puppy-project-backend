from django.contrib import admin

# Register your models here.
from .models import Person, Address

admin.site.register({Person, Address})