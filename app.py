import os
import sys
from flask import Flask, render_template, request,flash,redirect
from werkzeug import secure_filename
import pathlib
from matching import lcs

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt'}
app= Flask(__name__)
app.secret_key = 'askjdhsuierbpoiasGAWGDJKHSFBABBSJHDJHJ'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/',endpoint='index')
def index():
    return render_template('index.html')
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
       if 'file'not in request.files:
           flash('No file part')
           return(redirect(request.url))
       file = request.files['file']
       if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
       if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return render_template('success.html')
@app.route('/match', endpoint='match',methods = ['GET', 'POST'])
def match():
    for path in pathlib.Path("uploads").iterdir():
        if path.is_file():
             Y = (open(path,"r").read())
    X = (open("fixed-sequence.txt","r").read())
    m = len(X)
    n = len(Y)
    result=lcs(X,Y,m,n)
    for path in pathlib.Path("uploads").iterdir():
        if path.is_file():
            os.remove(path)
    return render_template('output.html',data=result)

if __name__ == '__main__':
    app.run(debug = True)