from flask import Flask, request, session
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.secret_key = "Esto es un secreto secretoso"

csrf = CSRFProtect(app)


