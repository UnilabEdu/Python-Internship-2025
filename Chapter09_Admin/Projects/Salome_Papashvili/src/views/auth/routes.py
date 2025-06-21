from uuid import uuid4
from os import path
from flask import Blueprint, render_template, redirect, request, flash, get_flashed_messages
from src.views.auth.forms import RegisterForm, LoginForm
from src.config import Config
from src.models import User
from flask_login import login_user, logout_user, current_user, login_required

auth_blueprint = Blueprint("auth", __name__)
@auth_blueprint.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        file = form.profile_image.data
        _, extension = path.splitext(file.filename)
        filename = f"{uuid4()}{extension}"
        file.save(path.join(Config.UPLOAD_PATH, filename))
        new_user = User(username=form.username.data, password=form.password.data, profile_image=filename)
        new_user.create()
        return redirect("/login")
    else:
        print(form.errors)
    return render_template("auth/register.html", form=form)


@auth_blueprint.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter(User.username == form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            next = request.args.get("next")
            if next:
                return redirect(next)
            flash("Success!", "success")
            return redirect("/")
        else:
            flash("Username or password is incorrect", "danger")
    return render_template("auth/login.html", form=form)


@auth_blueprint.route("/logout")
def logout():
    logout_user()
    return redirect("/login")

@auth_blueprint.route("/profile")
@login_required
def view_profile():
    return render_template("auth/view_profile.html")