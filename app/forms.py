from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class RegisterProjectForm(FlaskForm):
    student_id_1 = StringField('Student UWA ID 1', validators=[DataRequired(), Length(max=8)])
    student_id_2 = StringField('Student UWA ID 2', validators=[DataRequired(), Length(max=8)])
    student_id_3 = StringField('Student UWA ID 3', validators=[DataRequired(), Length(max=8)])
    student_id_4 = StringField('Student UWA ID 4', validators=[DataRequired(), Length(max=8)])
    submit = SubmitField('Submit')