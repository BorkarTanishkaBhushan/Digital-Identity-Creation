# import json
import pickle
from PIL import Image
from flask import Flask,flash,request,app,session,jsonify,url_for,render_template,redirect, Response
import os
from faceRecognition import gen_frames
from werkzeug.utils import secure_filename

app=Flask(__name__)

# image related
UPLOAD_FOLDER = 'static/uploads/'
app.secret_key = "secret key"
app.config['IMAGE_UPLOADS'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
     

# Analysis model
pickle.dump("Analysis.py", open('./models/analysis.pkl', 'wb'))
pickled_analysismodel=pickle.load(open('./models/analysis.pkl','rb')) #load

# # OCR model
# pickle.dump("img2txt.py", open('./models/ocr.pkl', 'wb'))
# pickled_ocrmodel = pickle.load(open('./models/ocr.pkl','rb')) #load

@app.route('/')
def home():
    return render_template('landingpage.html')


@app.route('/login', methods=['GET', 'POST']) 
def login():
    if request.method == 'POST':
        name = request.form.get('firstName')
        role = request.form.get('Role')
        
        return redirect('/dashboard')
    #     email = request.form['email']
    #     password = request.form['password']
    #     if login(email, password):
    #         return redirect(url_for('dashboard'))
    #     else:
    #         error = 'Invalid email or password. Please try again.'
    #         return render_template('login.html', error=error)
    return render_template('login.html')

@app.route('/dashboard_', methods=['POST','GET'])
def dashboard_():
    return render_template('dashboard_.html')


@app.route('/dashboard', methods=['POST','GET'])
def dashboard():
    # if request.method == "POST":
    #     # print(request.files)
    #     image = request.files['file']
    #     if image.filename == '':
    #         print("file name invalid")
    #         return request(request.url)
    #     filename = secure_filename(image.filename)
    #     basedir = os.path.abspath(os.path.dirname(__file__))
    #     image.save(os.path.join(basedir, app.config["IMAGE_UPLOADS"], filename))
    #     return render_template("dashboard.html", filename = filename)
    
    # if 'file' not in request.files:
    #     flash('No file part')
    #     return redirect(request.url)
    # file = request.files['file']
    # if file.filename == '':
    #     flash('No image selected for uploading')
    #     return redirect(request.url)
    # if file and allowed_file(file.filename):
    #     filename = file.filename
    #     file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    #     #print('upload_image filename: ' + filename)
    #     # flash('Image successfully uploaded and displayed below')
    #     id_type = request.form.get('file')
    #     return render_template('dashboard.html', filename=filename, id_type=file)
    # else:
    #     flash('Allowed image types are - png, jpg, jpeg, gif')
    #     return redirect(request.url)
    return render_template('dashboard.html')


@app.route('/yourdocs', methods=['POST','GET'])
def yourdocs():
    return render_template('yourdocs.html')


@app.route('/profile', methods=['POST','GET'])
def profile():
    frame_bytes = next(gen_frames())
    # Return the latest frame as a response with Content-Type 'image/jpeg'
    # return Response(frame_bytes, mimetype='image/jpeg')
    return render_template('profile.html', frame_bytes)


@app.route('/temp', methods=['POST','GET'])
def temp():
    return Response(gen_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/resultC', methods=['POST','GET'])
def resultC():
    return render_template("resultC.html")

@app.route('/resultF', methods=['POST','GET'])
def resultF():
    # imgfile = url_for('static', filename = '/Images'+ filename)
    # # if request.method == 'POST':
    # #     imgfile = request.files['id_card']
    # prediction = pickled_analysismodel.detectAadhar(imgfile)
    # if prediction==0:
    #   txt="yes it is correct doc."
    # else:
    #   txt="Fraud!"
    # return render_template('result.html',file = imgfile, features = txt)
    # return redirect(url_for('static', filename = '/Images'+ filename ), code = 301)
    return render_template("resultF.html")

# @app.route('/video_feed')
# def video_feed():
#     return Response(gen_frames(),
#                     mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/ocrdocupload.html')
def ocrdocupload():
    return render_template('ocrdocupload.html')

@app.route('/ocrdocuploadcopy.html')
def ocrdocuploadcopy():
    return render_template('ocrdocuploadcopy.html')

@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        file = request.files['image']
        if file:
            filename = file.filename
            file.save(os.path.join('static/uploads', filename))
            return redirect(url_for('view_image', filename=filename))
    return redirect(url_for('index'))

@app.route('/upload1', methods=['POST'])
def upload1():
    if request.method == 'POST':
        file = request.files['image']
        if file:
            filename = file.filename
            file.save(os.path.join('static/uploads', filename))
            return redirect(url_for('view_image', filename=filename))
    return redirect(url_for('index'))

@app.route('/view/<filename>')
def view_image(filename):
#     pickle.dump("img2txt.py", open('./models/ocr.pkl', 'wb'))
#     pickled_ocrmodel = pickle.load(open('./models/ocr.pkl','rb')) 
# # Call the extract method on the loaded object
#     result = pickled_ocrmodel.extract(filename)
#     # print(result)
    # return render_template('view.html', result=result)
    return render_template('view.html',  filename=filename)

@app.route('/viewcopy/<filename>')
def view_imagecopy(filename):
#     pickle.dump("img2txt.py", open('./models/ocr.pkl', 'wb'))
#     pickled_ocrmodel = pickle.load(open('./models/ocr.pkl','rb')) 
# # Call the extract method on the loaded object
#     result = pickled_ocrmodel.extract(filename)
#     # print(result)
    # return render_template('view.html', result=result)
    return render_template('viewcopy.html',  filename=filename)


if __name__=="__main__":
    app.run(debug=True)