from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse
from . import views


def unauthenticateduser(view_func):

    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('status')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func

# allowed users decorator.


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None

            if request.user.groups.exists():
                group_unpacked = request.user.groups.all()

                for g in range(len(group_unpacked)):

                    group = group_unpacked[g].name

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return redirect('error_403')

        return wrapper_func
    return decorator
