from fileinput import filename
from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    url_for,
    current_app,
    request,
)
from flask_login import login_user, logout_user, login_required, current_user


from .forms import RegistrationForm, LoginForm
from .models import User
from ...extensions import login_manager, bcrypt

auth = Blueprint("auth", __name__, static_folder="static", template_folder="templates")


# ===================Register and Login===================
@login_manager.user_loader
def load_user(email):
    user = current_app.db["users"].find_one({"username": email})

    return User(
        _id=str(user["_id"]),
        username=user["username"],
        email=user["email"],
        avatar=user["avatar"],
    )


@auth.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("home.index"))

    title = "Register"

    form = RegistrationForm()

    if form.validate_on_submit():

        username = form.username.data
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode(
            "utf-8"
        )
        email = form.email.data

        user = {
            "username": username,
            "email": email,
            "password": hashed_password,
            "avatar": url_for("static", filename="images/default_avatar.jpg"),
        }

        try:
            current_app.db["users"].insert_one(user)
            flash(
                f"Account {username} successfully created, you can try to login",
                "success",
            )
            return redirect(url_for("auth.login"))
        except Exception as e:
            flash(f"Error occured {e}", "danger")

    return render_template("register.html", title=title, form=form)


@auth.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home.index"))

    title = "Login"

    form = LoginForm()

    if form.validate_on_submit():

        email = form.email.data
        password = form.password.data

        if current_app.db["users"].count_documents({"email": email}) == 0:
            flash(
                f"email {email} has not been registered yet, try registering it",
                "danger",
            )
            return redirect(url_for("auth.register"))

        user_in_db = current_app.db["users"].find_one({"email": email})

        if bcrypt.check_password_hash(user_in_db["password"], password):
            user_obj = User(
                _id=str(user_in_db["_id"]),
                username=user_in_db["username"],
                email=user_in_db["email"],
                avatar=user_in_db["avatar"],
            )
            login_user(user_obj, remember=form.remember.data)
            flash("Logged in successfully!", category="success")
            next_page = request.args.get("next")

            return redirect(next_page) if next_page else redirect(url_for("home.index"))
        else:
            flash("Wrong username or password!", category="danger")

    return render_template("login.html", title=title, form=form)


@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home.index"))


# ===================<END> Register and Login===================


@auth.route("/profile")
@login_required
def profile():
    username = current_user.username
    title = f"Profile {username}"
    return render_template("profile.html", title=title)
