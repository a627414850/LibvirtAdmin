from flask import render_template, request, jsonify
from app import db
from app.errors import bp
from werkzeug.http import HTTP_STATUS_CODES
from werkzeug.exceptions import HTTPException

@bp.app_errorhandler(HTTPException)
def generic_http_error(error):
    if not request.accept_mimetype['text/html']:
        return jsonify({
            'error':error.code,
            'message':HTTP_STATUS_CODES.get(error.code, 'Unknown Error')

        }), error.code
    return render_template('error.html', err_msg = "An unexpected error has occurred"), error.code

@bp.app_errorhandler(500)
def internal_error(error):
    db.session.rollback()
    if not request.accept_mimetype['text/html']:
        return generic_http_error(error)
    return render_template('error.html', err_msg = "An unexpected error has occurred"), 500

@bp.app_errorhandler(404)
def not_found_error(error):
    if not request.accept_mimetype['text/html']:
        return generic_http_error(error)
    return render_template('error.html', err_msg = "The resource you requested was not available"), 404

@bp.app_errorhandler(401)
def unauthorized_error(error):
    if not request.accept_mimetype['text/html']:
        return generic_http_error(error)
    return render_template('error.html', err_msg = "Unauthorized, please verify your login"), 401