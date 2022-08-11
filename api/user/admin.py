from django.contrib import admin

from api.user.models import CustomUser

admin.site.register(CustomUser)