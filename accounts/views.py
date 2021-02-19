from django.shortcuts import render
from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from .models import *
from .choice import *


def user_register(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		email = request.POST.get('email')
		password = request.POST.get('password')

		#userdetail saved in django User model
		user = User.objects.create_user(username=username, email=email, password=password)
		user.is_active = True
		user.save()
		
		#userdetail saved in UserRegister model
		newuserinfo = UserRegister(user=user, userstatus=1)
		newuserinfo.save()
		
		#Check exist or not 
		user = authenticate(username=username, password=password)
		if user:
			login(request, user)
		return HttpResponseRedirect("/")
	else:
		return render(request, 'accounts/user_register.html')



def user_login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		try:
			cus = User.objects.get(username=username)
		except:
			try:
				cus = User.objects.get(email=email)
			except:
				return HttpResponseRedirect("/accounts/signin/?msg=Username is not correct.Please fill correct one.")
		user = authenticate(username=cus.username, password=password)
		if user:
			login(request, user)
			return HttpResponseRedirect("/")
		else:
			return HttpResponseRedirect("/accounts/signin/?msg=Password is not correct.Please fill correct one.")
	else:
		return render(request, 'accounts/login.html')





def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/")