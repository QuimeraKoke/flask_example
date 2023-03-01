from flask import render_template, redirect


def lender_controller(req, session):
    return render_template("index.html")


def lend_api_controller(req, session):
    return render_template("index.html")
