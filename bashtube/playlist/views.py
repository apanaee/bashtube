from flask import Blueprint, render_template
playlist = Blueprint('playlist', __name__, template_folder='templates')


@playlist.route('/')
def index():
    return render_template('playlist/playlist.html')
