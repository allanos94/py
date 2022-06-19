from django.contrib import admin
from api import models

admin.site.register(models.UserAccess)
admin.site.register(models.Team)
admin.site.register(models.Player)
admin.site.register(models.Staff)
