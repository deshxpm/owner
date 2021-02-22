from django.contrib import admin

from .models import *


class UserRegisterAdmin(admin.ModelAdmin):
	list_display = ('user_email', 'userstatus', 'userrole')
	list_filter = ('userstatus', 'userrole') 

	def user_email(self, obj):
		return obj.user.email


admin.site.register(UserRegister, UserRegisterAdmin)