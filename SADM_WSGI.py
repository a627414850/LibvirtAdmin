from app import create_app, db
from app.models import User

flask_app = create_app()

@flask_app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User}