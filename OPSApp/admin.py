from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from OPSApp.models import Student, User, Guide, Hod, pupload


class puploadAdmin(admin.ModelAdmin):
    list_display = ('id','ptitle','user')
    list_display_links = ('ptitle','user')

class gstatusAdmin(admin.ModelAdmin):
    list_display = ('id','user')

admin.site.register(Student)
admin.site.register(Guide)
admin.site.register(Hod)
admin.site.register(User, UserAdmin)
admin.site.register(pupload,puploadAdmin)
# admin.site.register(gustatus,gstatusAdmin)