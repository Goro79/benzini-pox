from django.shortcuts import redirect, render
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm

def custom_login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('chat_room', room_id='123')  # or your chosen page
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/custom_login.html', {'form': form})
