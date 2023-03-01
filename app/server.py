from flask import Flask, request, session
from flask_wtf.csrf import CSRFProtect


from app.controller.BorrowerController import borrower_controller
from app.controller.LenderController import lender_controller, lend_api_controller
from app.controller.LoginController import login_controller, login_api_controller
from app.controller.RegisterController import register_controller, register_api_controller


app = Flask(__name__)
app.secret_key = "Esto es un secreto secretoso"

csrf = CSRFProtect(app)


@app.route("/")
def login():
    return login_controller(request, session)


@app.route("/register")
def register():
    return register_controller(request, session)


@app.route("/lender")
def register():
    return lender_controller(request, session)


@app.route("/borrower")
def register():
    return borrower_controller(request, session)


# API

@app.route("/api/login", methods=['POST'])
def register():
    return login_api_controller(request, session)


@app.route("/api/register", methods=['POST'])
def register():
    return register_api_controller(request, session)


@app.route("/api/lend", methods=['POST'])
def register():
    return lend_api_controller(request, session)


if __name__ == "__main__":
    app.run(debug=True)
