from flask import render_template, redirect


def register_controller(req, session):
    return render_template("index.html")


def register_api_controller(req, session):
    return render_template("index.html")
