from django.contrib import admin
from .models import Region_Name, Team_Name, Team_Member

# Register your models here.


class Team_NameAdmin(admin.ModelAdmin):
    search_fields = ['name_team']
    list_display = ['name_team', 'region_member']
    list_filter = ['region_member']


class Team_MemberAdmin(admin.ModelAdmin):
    search_fields = ['member_name', 'member_team__name_team']
    list_display = ['member_name', 'position', 'member_team']
    list_filter = ['member_team']
    list_editable = ['position', 'member_team']


admin.site.register(Region_Name)
admin.site.register(Team_Name, Team_NameAdmin)
admin.site.register(Team_Member, Team_MemberAdmin)
