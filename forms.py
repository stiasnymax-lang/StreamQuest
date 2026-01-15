from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, PasswordField, HiddenField
from wtforms.validators import InputRequired, Length

class CreateGroupForm(FlaskForm): 
    name = StringField(validators=[InputRequired(), Length(min=2)])  
    password = PasswordField(validators=[InputRequired(), Length(min=3)])
    submit = SubmitField('Create')
    user_id = HiddenField() 

class ProfileForm(FlaskForm):
    user_id = HiddenField()

class RegisterForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=4, max=20)])
    password = PasswordField(validators=[InputRequired(), Length(min=3, max=20)])
    email = StringField(validators=[InputRequired(), Length(min=6, max=20)])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=4, max=20)])
    password = PasswordField(validators=[InputRequired(), Length(min=3, max=20)])
    submit = SubmitField('Login')
