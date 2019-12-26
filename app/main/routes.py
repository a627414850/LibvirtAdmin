from flask import render_template, flash, redirect, request
from flask_login import login_required
from app.main import bp

@bp.route('/')
@bp.route('/index')
@login_required
def index():
    return render_template('base.html',view='')
    #return render_template('index.html',title='HOME:P2')

@bp.route('/iframeresource')
@login_required
def getResource():
    #if request.query_string == "registration":
    #    form = RegistrationForm()
    #    iframeBody = render_template('registration.html', form = form)
    return iframeBody