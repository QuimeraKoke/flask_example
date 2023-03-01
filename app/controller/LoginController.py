from flask import render_template, redirect

from app.forms.LoginForm import LoginForm
from app.utils import LENDER_ID


def login_controller(req, session):
    if ('token' in session and 'user' in session):
        redirect_url = "/lender" if session['user_type'] == LENDER_ID else "/borrower"
        return redirect(redirect_url)
    return render_template("index.html", login_form=LoginForm())


def login_api_controller(req, session):
    form =  LoginForm(req.form)
    if (form.validate_on_submit()):
        #     Create Session
        session['user'] = user.name
        session['user_type'] = user.user_type_id
    return render_template("index.html")
