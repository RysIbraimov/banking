from django.contrib import admin
from .models import Client,Credit,Account

admin.site.register(Credit)
admin.site.register(Client)
admin.site.register(Account)

# Register your models here.
