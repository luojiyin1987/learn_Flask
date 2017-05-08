# coding=utf-8
import os
from flask import Flask
from flasj import request
from flask_uploads import UploadSet
from flask_uploads import configure_uploads
from flask_uploads import IMAGES
from flask_uploads import patch_request_class

app = Flask(__name__)
app.config['UPLOADED_PHOTOS_DEST'] = os.getcwd()

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)

html = '''
    <!DOCTYPE html>
    <title>Upload</title>
    <h1>图片上传</h1>
    <form method=post enctype=multipart/form-data>
        <input type=file name=photo>
        <input type=submit value=上传>
    </form>
    '''


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST' and 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        file_url = photos.url(filename)
        return html + '<br><img src=' + file_url + '>'
    return html


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
