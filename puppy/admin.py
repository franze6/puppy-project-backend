from django.contrib import admin

# Register your models here.
from .models import Person, Address, Career, Company, Project, Passport, Messenger

admin.site.register({Person, Address, Career, Company, Project, Passport, Messenger})