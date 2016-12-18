from django.shortcuts import render
from django.contrib.auth.models import User

from django.shortcuts import render
from .forms import RegisterForm
# Create your views here.
def index(request):
	return render(request, 'index.html')
	# return HttpResponse("Hello, World. You're at the polls index")

def user_list(request):
	users = User.objects.all()
	return render(request, 'userlist.html', {'users': users})

def user_form(request):
	registerFrom = RegisterForm(auto_id=False)
	return render(request, 'user_form.html', {'registerform': registerFrom})
	pass