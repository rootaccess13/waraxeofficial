from decimal import Context
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_text
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from .tokens import account_activation_token
from django.template.loader import render_to_string
from django.core.mail import send_mail
from .forms import SignUpForm, LogInForm
from . tokens import account_activation_token
from django.contrib import messages
from django.contrib.auth.decorators import login_required as lr
from django.utils import timezone
def signup_view(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method  == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                user = form.save()
                user.refresh_from_db()
                user.profile.first_name = form.cleaned_data.get('first_name')
                user.profile.last_name = form.cleaned_data.get('last_name')
                user.profile.email = form.cleaned_data.get('email')
                user.is_active = False
                user.last_login = timezone.now()
                user.save()
                current_site = get_current_site(request)
                subject = 'Please Activate Your Account'

                message = render_to_string('accounts/activation_request.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
                })
                user.email_user(subject, message)
                return redirect('activation_sent')
        else:
            form = SignUpForm()
        return render(request, 'accounts/register.html', {'form': form})

def signin_view(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password1')
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                print(True)
                return redirect('index')
            else:
                return redirect('signin')
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('signin')

def activation_sent_view(request):
    return render(request, 'accounts/activation_sent.html')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.signup_confirmation = True
        user.last_login = timezone.now()
        user.save()
        login(request, user)
        return redirect('index')
    else:
        return render(request, 'accounts/activation_invalid.html')
