from django.shortcuts import render
from .forms import RegisterForm

# Create your views here.
from django.shortcuts import render, redirect

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in
            login(request, user)
            return redirect('home')  # Redirect to a desired page after successful registration
    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html', {'form': form})
