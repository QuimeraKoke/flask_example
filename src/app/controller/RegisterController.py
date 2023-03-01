from flask import render_template, redirect
import bcrypt

from app.forms.RegisterForm import LenderRegisterForm, BorrowerRegisterForm
from app.models.Announcement import Announcement
from app.models.User import User
from app.utils import BORROWER_ID, LENDER_ID


def register_controller(req, session):
    return render_template("register.html", lender_form=LenderRegisterForm(), borrower_form=BorrowerRegisterForm())


def register_borrower_api_controller(req, session):
    form = BorrowerRegisterForm(req.form)
    if form.validate():
        encrypted_password = bcrypt.hashpw(form.password.data.encode('utf8'), bcrypt.gensalt(14))
        user_data = {
            'first_name': form.first_name.data,
            'last_name': form.last_name.data,
            'email': form.email.data,
            'user_type': BORROWER_ID,
            'password': encrypted_password,
            'balance': 0,
        }
        user_id = User.create(user_data)
        borrow_data = {
            'user_id': user_id,
            'title': form.project_title.data,
            'description' : form.project_description.data,
            'amount': form.money.data
        }
        Announcement.create_announcement(borrow_data)
        return redirect("/")
    return render_template("register.html", lender_form=LenderRegisterForm(), borrower_form=form)


def register_lender_api_controller(req, session):
    form = LenderRegisterForm(req.form)
    if form.validate():
        encrypted_password = bcrypt.hashpw(form.password.data.encode('utf8'), bcrypt.gensalt(14))
        user_data = {
            'first_name': form.first_name.data,
            'last_name': form.last_name.data,
            'email': form.email.data,
            'user_type': LENDER_ID,
            'password': encrypted_password,
            'balance': form.money.data
        }
        user_id = User.create(user_data)
        return redirect("/")
    return render_template("register.html", lender_form=form, borrower_form=BorrowerRegisterForm())
