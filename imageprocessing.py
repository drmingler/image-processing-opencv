import os
import random
import string
from ImageProcessing.joiner import stich

import cv2
from flask import Flask, render_template, request, url_for, redirect
from werkzeug.utils import secure_filename
from ImageProcessing.cartoonise import cartoonise
import time

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app = Flask(__name__, template_folder=os.path.abspath('templates'))


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        file = request.files.get('file')
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(os.path.abspath('imageProcessing'), filename))
            image = cartoonise(os.path.join(os.path.abspath('imageProcessing'), filename))
            concatstr = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(5))
            imagename = "cartoon" + concatstr + '.jpg'
            cv2.imwrite(f'static/{imagename}', image)
            cartoon = os.path.join(('static'), imagename)
            # return render_template("result.html", image=cartoon)
            return render_template("results.html", image=cartoon)

    return render_template("upload.html")
    #return render_template("imageprocess.html")


@app.route('/multiple', methods=['GET', 'POST'])
def multiple():
    try:
        if request.method == "POST":
            for image in request.files.getlist('file'):
                image.save(os.path.join(os.path.abspath('imageProcessing'), image.filename))
                print(image)
            files=request.files.getlist('file')
            print(files[0].filename)
            print(files[1].filename)

            image1=os.path.join(os.path.abspath('imageProcessing'), files[0].filename)
            image2=os.path.join(os.path.abspath('imageProcessing'), files[1].filename)
            # image1=str(files[0].filename)
            # image2 = str(files[1].filename)

            image = stich(image1, image2)

            concatstr = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(5))
            imagename = "Panorama" + concatstr + '.jpg'
            cv2.imwrite(f'static/{imagename}', image)
            Panorama = os.path.join(('static'), imagename)
            return render_template("results.html", image=Panorama)
    except:
        return('''<h1>Invalid Image Format</h1''')

    else:
        return render_template("multiple.html")
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
