from django.contrib import admin
from .models import *
admin.site.register(Chat)
admin.site.register(Room)
admin.site.register(ChatHistory)