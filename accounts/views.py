# accounts/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm

def custom_login_view(request):
    """
    A simple custom login view. Adjust it to your needs.
    """
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Redirect after login. You can also use `request.GET.get('next')`.
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/custom_login.html', {'form': form})

# accounts/views.py

from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = "accounts/custom_login.html"  # Our custom login template
