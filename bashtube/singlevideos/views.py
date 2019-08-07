from flask import Blueprint, render_template

from bashtube import cache

singlevideos = Blueprint('singlevideos',__name__,template_folder='templates')


@singlevideos.route('/')

def index():
    return render_template('singlevideos/single.html')


