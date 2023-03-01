import bcrypt
from flask import render_template, redirect

from app.forms.LoginForm import LoginForm
from app.models.User import User
from app.utils import LENDER_ID


def login_controller(req, session):
    if ( 'user' in session):
        redirect_url = "/lender" if session['user_type'] == LENDER_ID else "/borrower"
        return redirect(redirect_url)
    return render_template("index.html", login_form=LoginForm())


def login_api_controller(req, session):
    form = LoginForm(req.form)
    if form.validate_on_submit():
        user = User.get(form.email.data)
        if bcrypt.checkpw(form.password.data.encode('utf8'), user.password.encode('utf8')):
            session['user'] = user.first_name + " " + user.last_name
            session['user_type'] = user.user_type
            print(user.user_type)
            redirect_url = "/lender" if user.user_type == LENDER_ID else "/borrower"
            return redirect(redirect_url)
    return render_template("index.html", login_form=form)


def logout_controller(req, session):
    session.clear()
    return redirect("/")
