from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def register(request):
    """Regsiter a new user"""
    # get request give blank form
    if request.method != 'POST':
        form = UserCreationForm()
    
    # process the form if submitted
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('learning_logs:index')
    
    # Display an blank or invalid form
    context= {'form': form }
    return render(request, 'registration/register.html', context)
        
    
    
    
        
    
