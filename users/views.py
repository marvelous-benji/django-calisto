from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required

def register(request):
	if request.method == 'POST':
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account created for {username}')
			form.save()
			return redirect('user_login')
	else:
		form = UserRegistrationForm()
	return render(request, 'users/register.html', {'form':form})
	
@login_required	
def profile(request):
	return render(request, 'users/profile.html')
