from wtforms.validators import InputRequired
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField


class SearchForm(FlaskForm):
    url = StringField('url',validators=[InputRequired()])
    submit = SubmitField('download video')