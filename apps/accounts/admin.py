from django.contrib import admin

from apps.accounts.models import Doctor, User

admin.site.register(User)
admin.site.register(Doctor)