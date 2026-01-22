from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, PasswordField, HiddenField
from wtforms.validators import InputRequired, Length

class CreateGroupForm(FlaskForm): 
    name = StringField(validators=[InputRequired(), Length(min=2)])  
    password = PasswordField(validators=[InputRequired(), Length(min=3)])
    user_id = HiddenField()
    submit = SubmitField('Create')

class RegisterForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=4, max=20)])
    password = PasswordField(validators=[InputRequired(), Length(min=3, max=20)])
    email = StringField(validators=[InputRequired(), Length(min=6, max=20)])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=4, max=20)])
    password = PasswordField(validators=[InputRequired(), Length(min=3, max=20)])
    submit = SubmitField('Login')

class JoinGroupForm(FlaskForm):
    password = PasswordField(validators=[InputRequired(), Length(min=3)])
    submit = SubmitField('Join Group')

class GroupForm(FlaskForm):
    challenge_id = HiddenField()
    start_session = SubmitField('Start Session')
    add_challenge = SubmitField('Add Challenge')
    delete_challenge = SubmitField('Delete Challenge')
    set_active = SubmitField('Set Active')
    completed_challenge = SubmitField('Completed Challenge')
    leave_group = SubmitField('Leave Group') #fehlt
    delete_group = SubmitField('Delete Group') #fehlt
    remove_member = SubmitField('Remove Member') #fehlt
    submit = SubmitField('Search') #fehlt

class ChallengeForm(FlaskForm):
    title = StringField(validators=[InputRequired(), Length(min=2)])
    description = StringField(validators=[InputRequired(), Length(min=5)])
    difficulty = StringField(validators=[InputRequired()])
    game_name = StringField(validators=[InputRequired(), Length(min=2)])
    time_needed = StringField(validators=[InputRequired()])

class GroupsSearchForm(FlaskForm):
    submit = SubmitField('Search') #fehlt
    
# class ProfileForm(FlaskForm):
# class PricingForm(FlaskForm):