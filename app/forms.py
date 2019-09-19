from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField#, BooleanField
from wtforms.validators import DataRequired, EqualTo, ValidationError
from app.models import User

class LoginForm(FlaskForm):
    username = StringField('Username:', validators=[DataRequired()])
    password = PasswordField('Password:',validators=[DataRequired()])
    

class RegistrationForm(FlaskForm):
    username = StringField('Username:',validators=[DataRequired()])
    password = PasswordField('Password:',validators=[DataRequired()])
    password2 = PasswordField('Confirm Password:',validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Register')
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is None:
            raise ValidationError('Username already taken!')
        