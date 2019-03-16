from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . forms import UserRegistrationForm 

def signUpForm(request):
    if request.method == 'POST':
        f = UserRegistrationForm(request.POST)
        if f.is_valid():
            username= f.cleaned_data.get('username')
            f.save()
            messages.success(request, 'Account created successfully')
            return redirect('login')
 
    else:
        f = UserRegistrationForm()
 
    return render(request, 'np_users/register.html', {'form': f})
    
@login_required   
def profile(request):
    return render(request,'np_users/profile.html')

    