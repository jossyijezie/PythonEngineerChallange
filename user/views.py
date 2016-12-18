from django.shortcuts import render
from django.contrib.auth.models import User

from django.shortcuts import render, redirect
from .forms import RegisterForm
# Create your views here.
def index(request):
	return render(request, 'index.html')
	# return HttpResponse("Hello, World. You're at the polls index")

def user_list(request):
	users = User.objects.filter(is_superuser=False)
	return render(request, 'userlist.html', {'users': users})

def user_form(request):
	registerFrom = RegisterForm(auto_id=False)
	if request.method == "GET":
		return render(request, 'user_form.html', {'registerform': registerFrom})
	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
		else:
			return render(request, 'user_form.html', {'registerform': registerFrom})
		return redirect('/')
