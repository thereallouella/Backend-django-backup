from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.utils.http import urlsafe_base64_decode


def activate(request, uid, token):
    User = get_user_model()
    try:
        # Decode the UID and check if the user exists
        uid = urlsafe_base64_decode(uid).decode()
        user = User.objects.get(pk=uid)

        # Check if the token is valid
        if default_token_generator.check_token(user, token):
            # Activate the user
            user.is_active = True
            user.save()
            return render(request, 'activate.html', {'activation_success': True})
        else:
            return render(request, 'activate.html', {'activation_success': False})
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        return render(request, 'activate.html', {'activation_success': False})
