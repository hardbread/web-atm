from functools import wraps
from django.shortcuts import redirect


def auth_required(func):
    @wraps(func)
    def with_auth_required(*args, **kwargs):
        if not args[0].session.get('is_authorized', False):
            return redirect('index')
        return func(*args, **kwargs)
    return with_auth_required


def is_auth(func):
    @wraps(func)
    def with_is_auth(*args, **kwargs):
        if args[0].session.get('is_authorized', False):
            return redirect('operations')
        return func(*args, **kwargs)
    return with_is_auth