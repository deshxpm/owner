from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from .choice import *



class UserRegister(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="userdetail")
	userstatus = models.IntegerField(choices=STATUS_CHOICE, default=1)
	userrole = models.IntegerField(choices=USER_ROLE, default=1)

	def __str__(self):
		return str(self.user.username)