import os
import sys
from flask import Flask, render_template, request,flash,redirect,url_for
from werkzeug import secure_filename
import pathlib
from matching import lcs

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt'}
ext=['a','t','g','c','u','']
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
   count=0
   if request.method == 'POST':
       if 'file'not in request.files:
           flash('Please upload correct file')
           return(redirect(url_for('index')))
       file = request.files['file']
       if file.filename == '':
            flash('Please upload another file')
            return redirect(url_for('index'))
       if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            if os.stat('uploads/'+filename).st_size!=0:
                with open('uploads/'+filename) as f:
                    for line in f:
                        for c in line:
                            if c.lower() in ext:
                                pass
                            else:
                                count+=1
                if count==0:
                    return render_template('success.html')
                else:
                    flash('Uploaded file is not a valid sequence')
                    for path in pathlib.Path("uploads").iterdir():
                        if path.is_file():
                            os.remove(path)
                    return redirect(url_for('index'))
            else:
               flash('Uploaded file is empty or type is wrong, please upload another file')
               for path in pathlib.Path("uploads").iterdir():
                        if path.is_file():
                            os.remove(path)
               return redirect(url_for('index'))



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