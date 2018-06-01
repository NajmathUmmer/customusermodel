from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
#from .forms import UserForm
from .models import CustomUser
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required



@login_required(login_url='/login')
def logout_user(request):
	logout(request)
	return render(request, 'users/login.html')



	
def login_user(request):
	if request.user.is_authenticated:
		return redirect('/')
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			u = CustomUser.objects.get(username=username)
			if user.is_active:
				login(request, user)
				return redirect('/')
			else:
				return render(request, 'users/login.html', {'error_message': 'Your account has been disabled'})
		else:
			return render(request, 'users/login.html', {'error_message': 'Invalid login'})
	return render(request, 'users/login.html')
@login_required(login_url='/login')
def home(request):
	user = request.user
	return render(request, 'users/home.html', {'user':user})