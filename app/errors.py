from flask import render_template
from app import flask_app as app, db
@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('error.html', err_msg = "An unexpected error has occurred"), 500
@app.errorhandler(404)
def not_found_error(error):
    db.session.rollback()
    return render_template('error.html', err_msg = "The resource you requested was not available"), 404