from flask import render_template, redirect


def borrower_controller(req, session):
    return render_template("index.html")
