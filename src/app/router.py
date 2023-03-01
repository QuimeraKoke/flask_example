from flask import request, session
from app import app

from app.controller.BorrowerController import borrower_controller
from app.controller.LenderController import lender_controller, lend_api_controller
from app.controller.LoginController import login_controller, login_api_controller, logout_controller
from app.controller.RegisterController import register_controller, register_borrower_api_controller, \
    register_lender_api_controller


@app.route("/")
def login():
    return login_controller(request, session)


@app.route("/register")
def register():
    return register_controller(request, session)


@app.route("/lender")
def lender():
    return lender_controller(request, session)


@app.route("/borrower")
def borrower():
    return borrower_controller(request, session)

@app.route("/logout")
def logout():
    return logout_controller(request, session)


# API

@app.route("/api/login", methods=['POST'])
def login_api():
    return login_api_controller(request, session)


@app.route("/api/lender/register", methods=['POST'])
def lender_register():
    return register_lender_api_controller(request, session)

@app.route("/api/borrower/register", methods=['POST'])
def borrower_register():
    return register_borrower_api_controller(request, session)


@app.route("/api/lend", methods=['POST'])
def lend_api():
    return lend_api_controller(request, session)
