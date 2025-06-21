from functools import wraps
from flask_login import current_user
from flask import redirect, url_for

def admin_required(func):
    @wraps(func)
    def admin_view(*args, **kwargs):
        if not current_user.is_authenticated:
            return redirect("/")
        if current_user.is_authenticated and not current_user.is_admin():
            return redirect("/")
        return func(*args, **kwargs)
    return admin_view