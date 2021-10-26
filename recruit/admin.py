from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from recruit.models import *


# class UserAdmin(BaseUserAdmin):
#
#

# Register your models here.
# admin.site.register(StdUserTb)
admin.site.register(StdDocTb)
admin.site.register(StdRecruitTb)
admin.site.register(TcrUserTb)
admin.site.register(ScoreTb)
