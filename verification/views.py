from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ProfileVerificationForm
from .models import ProfileVerification
from django.core.exceptions import PermissionDenied

@login_required
def submit_verification(request):
    # Try to retrieve an existing verification for the user
    try:
        verification = request.user.verification
    except ProfileVerification.DoesNotExist:
        verification = None

    if request.method == 'POST':
        form = ProfileVerificationForm(request.POST, request.FILES, instance=verification)
        if form.is_valid():
            ver = form.save(commit=False)
            ver.user = request.user
            ver.save()
            # Optionally, send an email notification to admins for review
            return redirect('verification_detail')
    else:
        form = ProfileVerificationForm(instance=verification)
    return render(request, 'verification/submit_verification.html', {'form': form})

@login_required
def verification_detail(request):
    # Show the current verification status and uploaded files
    verification = get_object_or_404(ProfileVerification, user=request.user)
    return render(request, 'verification/verification_detail.html', {'verification': verification})

def staff_required(view_func):
    """A simple decorator to allow only staff users."""
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_staff:
            raise PermissionDenied("You do not have permission to access this page.")
        return view_func(request, *args, **kwargs)
    return _wrapped_view

@staff_required
def verify_profile(request, user_id):
    verification = get_object_or_404(ProfileVerification, user_id=user_id)
    if request.method == 'POST':
        # Mark the profile as verified
        verification.verified = True
        verification.save()
        # Change redirect here if you don't have 'verification_list'
        return redirect('verification_detail')  # or redirect('verification_list') if you create that view
    return render(request, 'verification/verify_profile.html', {'verification': verification})
