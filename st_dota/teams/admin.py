from django.contrib import admin
from .models import Region_Name, Team_Name, Team_Member

# Register your models here.

admin.site.register(Region_Name)
admin.site.register(Team_Name)
admin.site.register(Team_Member)
