from flask import redirect, render_template, Blueprint, url_for, request, flash, get_flashed_messages
from MyPage.src.models import User
from flask_login import login_user, current_user, logout_user

from MyPage.src.views.auth.forms import RegisterForm, LoginForm
from MyPage.src.config import Config

auth_blueprint = Blueprint("auth", __name__)

@auth_blueprint.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User(name = form.username.data, password = form.password.data)
        new_user.create()
        return redirect(url_for("main.home"))
    return render_template("auth/register.html", form=form)



@auth_blueprint.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        found_user = User.query.filter(User.name == form.username.data).first()
        if found_user and found_user.check_password(form.password.data):
            login_user(found_user)
            next = request.args.get('next')
            if next:
                return redirect(next)

            return redirect(url_for("main.home"))
        else:
            flash("Credentials Wrong")

    return render_template("auth/login.html", form=form)


@auth_blueprint.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("main.home"))





