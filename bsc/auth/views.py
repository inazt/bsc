from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages

from bsc.auth.forms import AuthLoginForm

def auth_login(request):
    if (request.POST):
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            if user.is_active:
                login(request, user)
                # Redirect.

    f = AuthLoginForm()
    ctx = RequestContext(request, {'form': f.as_table()})
    return render_to_response('auth/login_form.html', ctx)

