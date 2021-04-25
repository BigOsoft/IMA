import os
import base64
import io
from PIL import Image
import urllib.request
import mammograms
import tuberculosis
import time
import json
from flask import Flask, request, redirect, jsonify, Response, render_template, url_for
from flask_cors import CORS
from werkzeug.utils import secure_filename
import flask_login


UPLOAD_FOLDER = 'sample_single_input/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
users = {'ima@mail.com': {'password': 'genius'}}  # mock db

app = Flask(__name__)
# cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
app.secret_key = "090078601"
CORS(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
login_manager = flask_login.LoginManager()
login_manager.init_app(app)

selected_view = "L-CC"


class User(flask_login.UserMixin):
    pass


@login_manager.user_loader
def user_loader(email):
    if email not in users:
        return

    user = User()
    user.id = email
    return user


@login_manager.request_loader
def request_loader(request):
    email = request.form.get('email')
    if email not in users:
        return

    user = User()
    user.id = email

    # DO NOT ever store passwords in plaintext and always compare password
    # hashes using constant-time comparison!
    user.is_authenticated = request.form['password'] == users[email]['password']

    return user


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
        # return '''
        #        <form action='login' method='POST'>
        #         <input type='text' name='email' id='email' placeholder='email'/>
        #         <input type='password' name='password' id='password' placeholder='password'/>
        #         <input type='submit' name='submit'/>
        #        </form>
        #        '''

    email = request.form['email']
    if request.form['password'] == users[email]['password']:
        user = User()
        user.id = email
        flask_login.login_user(user)
        return redirect(url_for('dashboard'))

    return 'Bad login'


@app.route('/dashboard')
@flask_login.login_required
def dashboard():
    # 'Logged in as: ' + flask_login.current_user.id
    return render_template('dashboard.html')


@app.route('/logout')
def logout():
    flask_login.logout_user()
    return 'Logged out'


@login_manager.unauthorized_handler
def unauthorized_handler():
    return 'Unauthorized'


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/file-upload', methods=['POST'])
@flask_login.login_required
def upload_file():
    # check if the post request has the file part
    if 'file' not in request.files:
        resp = jsonify({'error': 'No file part in the request'})
        resp.status_code = 400
        return resp
    file = request.files['file']
    if file.filename == '':
        resp = jsonify({'error': 'No file selected for uploading'})
        resp.status_code = 400
        return resp
    if file and allowed_file(file.filename):
        # filename = secure_filename(file.filename)
        selected_view = request.form.get("select-view")
        print(selected_view)
        filename = 'mammogram.png'
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        resp = jsonify({'success': 'File successfully uploaded'})
        resp.status_code = 201
        return resp
    else:
        resp = jsonify({'error': 'Allowed file types are png, jpg, jpeg'})
        resp.status_code = 400
        return resp


@app.route('/api/bc')  # API for Breast Cancer classification
@flask_login.login_required
def progress():
    def generate():
        x = 0
        x = x + 10
        yield "data:" + str(x) + "\n\n"
        cresp = mammograms.crop_mammogram(selected_view)
        if cresp:
            print(cresp)
            yield "data:" + cresp + "\n\n"
        time.sleep(2)
        x = x + 20
        yield "data:" + str(x) + "\n\n"
        mammograms.calc_optimal_centers()
        time.sleep(2)
        x = x + 30
        yield "data:" + str(x) + "\n\n"
        mammograms.generate_heatmap()
        x = x + 30
        yield "data:" + str(x) + "\n\n"
        resp = mammograms.classify_mammogram(selected_view)
        # resp = json.dumps({'benign': '0.12563996016979218', 'malignant': '0.014475742354989052'})
        time.sleep(2)
        x = 100
        yield "data:" + str(x) + "\n\n"
        yield "data:" + resp + "\n\n"

    return Response(generate(), mimetype='text/event-stream')


@app.route('/api/tb', methods=['POST'])  # API for Tuberculisis classification
@flask_login.login_required
def predict():
    message = request.get_json(force=True)
    encoded = message['image']
    decoded = base64.b64decode(encoded)
    image = Image.open(io.BytesIO(decoded))
    processed_image = tuberculosis.preprocess_image(
        image, target_size=(224, 224))

    prediction = tuberculosis.model.predict(processed_image).tolist()

    response = {
        'prediction': {
            'abnormal': prediction[0][0],
            'normal': prediction[0][1]

        }
    }
    return jsonify(response)

# Route for handling entry point


@app.route('/')
def index():
    if not flask_login.current_user.is_authenticated:
        return render_template('index.html')
    else:
        return render_template('dashboard.html')


@app.route('/tb')
@flask_login.login_required
def tb():
    return render_template('tb.html')


@app.route('/bc')
@flask_login.login_required
def bc():
    return render_template('bc.html')


if __name__ == "__main__":
    # app.run(host= '172.20.10.2')
    app.run(debug=True)
