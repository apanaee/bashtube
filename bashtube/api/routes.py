import os
import requests
import math
import pytube
from flask import Blueprint, jsonify, request, abort
from itsdangerous import TimedJSONWebSignatureSerializer as Serial
api = Blueprint('api', __name__)


@api.route('/singles/', methods=['POST','GET'])
# @cache.cached(500)
def single_videos():
    if request.method == 'POST':
        url = request.form["url"]
        if "list" in url:
            return jsonify(error="Only single videos are allowed in this section. So please goto the Playlist section")
        if "v" not in url:
            return jsonify(error="Youtube link you inserted is incorrect")
        data = processing_single(url)
        return data
    abort(status=403)


def processing_single(url, expire=10000):
    """    :param expire: default value
          :param url
    """
    s = Serial(os.environ.get('SECRET_KEY'), expire)
    try:
        res = pytube.YouTube(url)
        videos = res.streams.filter(file_extension="mp4", progressive=True).order_by('resolution').asc().all()
        meta = []

        for v in videos:
            mb1 = math.pow(10, 6)
            mb_size = math.ceil(v.filesize / mb1)
            mime_type = v.mime_type

            encrypt_url = s.dumps({'url': v.url, 'mime_type': mime_type,'title':res.title}).decode('utf-8')
            _ = {'url': encrypt_url, 'resolution': v.resolution, 'size': mb_size}
            meta.append(_)

        return jsonify(
            meta=meta,
            title=res.title,
            thumbnail_url=res.thumbnail_url,
            length=math.ceil(int(res.length) / 60),
            descp=res.description,
            views=res.views,
            rating=res.rating,
            restricted=res.age_restricted,
        )
    except Exception as e:
        if "regex" in e.__str__():
            return jsonify(error="Youtube Url doesnt not match any known format")
        elif "unavailable" in e.__str__():
            return jsonify(error="No Youtube video found. Please check URL")
        else:
            return jsonify(error=e.__str__())


@api.route("/playlist",methods=['GET','POST'])
def playlist():
    if request.method =='POST':
        url = request.form["url"]
        if url is not None:
            if "&list" not in url and "?v" not in url:
                return jsonify(error="You have inserted a wrong playlist url")
            playlist = processing_playlist(url)
            return playlist
    abort(status=403)


def processing_playlist(url,expires=1000000):
    """    :param expires: default value
              :param url
        """

    s = Serial(os.environ.get('SECRET_KEY'), expires)
    try:
        res = pytube.Playlist(url)
        res.populate_video_urls()
        meta = []
        for video_url in res.video_urls:
            res = pytube.YouTube(video_url)
            videos = res.streams.filter(file_extension="mp4", progressive=True, res="720p").order_by('resolution').asc().all()

            for v in videos:
                mb1 = math.pow(10, 6)
                mb_size = math.ceil(v.filesize / mb1)
                mime_type = v.mime_type

                encrypt_url = s.dumps({'url': v.url, 'mime_type': mime_type, 'title': res.title}).decode('utf-8')
                _ = {
                    'url': encrypt_url,
                    'url_un':v.url,
                    'resolution': v.resolution,
                    'size': mb_size,
                    'title': res.title,
                    'thumbnail_url': res.thumbnail_url,
                    'length': math.ceil(int(res.length) / 60),
                    'descp': res.description,
                    'views': res.views,
                    'rating': res.rating,
                    'restricted': res.age_restricted,}
                meta.append(_)
        return jsonify(meta=meta)

    except Exception as e:
        return jsonify(error=e.__str__())
    # for v in videos.video_urls:


