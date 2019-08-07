import os

import requests
from flask import Blueprint, request, abort, render_template,url_for
from itsdangerous import TimedJSONWebSignatureSerializer as Serialiser,BadSignature

preview = Blueprint("preview",__name__,template_folder="templates")


def check_if_expired(url):
    try:
        s = Serialiser(os.environ.get('SECRET_KEY'))
        meta = s.loads(url)
        return meta
    except BadSignature:
        return None


@preview.route('/',methods=['GET','POST'])
def viewer():
    url = request.args.get('url')
    if url is None:
        abort(status=404)
    check = check_if_expired(url)
    if check is None:
        return f"""
        <h1>Link has expired</h1>
        <p> Your video link has expired <a href='{url_for("singlevideos.index")}'>Goto Home</a> </p>
                """
    url = check['url']
    mime = check['mime_type']
    title = check['title']
    return render_template('preview/preview.html', url=url, mime=mime, title=title)


