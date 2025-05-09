from flask_wtf import FlaskForm
from wtforms import BooleanField, IntegerField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    student_id = IntegerField('Student ID', validators=[DataRequired(), Length(max=8)])
    password = PasswordField('Password', validators=[DataRequired()])
    register = BooleanField("Register")

class RegisterProjectForm(FlaskForm):
    student_id_1 = StringField('Student UWA ID 1', validators=[DataRequired(), Length(max=8)])
    student_id_2 = StringField('Student UWA ID 2', validators=[DataRequired(), Length(max=8)])
    student_id_3 = StringField('Student UWA ID 3', validators=[DataRequired(), Length(max=8)])
    student_id_4 = StringField('Student UWA ID 4', validators=[DataRequired(), Length(max=8)])
    submit = SubmitField('Submit')