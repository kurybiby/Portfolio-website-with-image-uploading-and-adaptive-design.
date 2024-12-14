# from flask import Flask, render_template, request, redirect, url_for
# import os
# from werkzeug.utils import secure_filename

# app = Flask(__name__)


# UPLOAD_FOLDER = 'static/uploads/'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS




# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         if 'file' not in request.files:
#             return redirect(request.url)
#         file = request.files['file']
#         if file and allowed_file(file.filename):
#             filename = secure_filename(file.filename)
#             file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#             return redirect(url_for('index'))
#     images = os.listdir(app.config['UPLOAD_FOLDER'])
#     return render_template('index.html', images=images)

# if __name__ == '__main__':
#     app.run(debug=True)




# from flask import Flask, render_template, request, redirect, url_for
# import os
# from werkzeug.utils import secure_filename

# app = Flask(__name__)


# UPLOAD_FOLDER = 'static/uploads/'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# # Главная страница
# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         if 'file' not in request.files:
#             return redirect(request.url)
#         file = request.files['file']
#         if file and allowed_file(file.filename):
#             filename = secure_filename(file.filename)
#             file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#             return redirect(url_for('index'))
#     images = os.listdir(app.config['UPLOAD_FOLDER'])
#     return render_template('index.html', images=images)

# if __name__ == '__main__':
#     app.run(debug=True)

# @app.route('/resume', methods=['POST'])
# def create_resume():
#     resume_text = request.form.get('resume_text', '')
#     # Здесь можно сохранить текст резюме в файл или базу данных
#     with open('static/resume.txt', 'w', encoding='utf-8') as file:
#         file.write(resume_text)
#     return render_template('resume.html', resume_text=resume_text)


# if __name__ == '__main__':
#     app.run(debug=True)



# from flask import Flask, render_template, request, redirect, url_for
# import os
# from werkzeug.utils import secure_filename

# app = Flask(__name__)

# UPLOAD_FOLDER = 'static/uploads/'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# # Убедитесь, что папка существует
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# # Главная страница
# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         if 'file' not in request.files:
#             return redirect(request.url)
#         file = request.files['file']
#         if file and allowed_file(file.filename):
#             filename = secure_filename(file.filename)
#             file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#             return redirect(url_for('index'))
#     images = os.listdir(app.config['UPLOAD_FOLDER'])
#     return render_template('index.html', images=images)

# # Маршрут для создания резюме
# @app.route('/resume', methods=['POST'])
# def create_resume():
#     resume_text = request.form.get('resume_text', '')
#     # Сохранение текста резюме
#     with open('static/resume.txt', 'w', encoding='utf-8') as file:
#         file.write(resume_text)
#     return render_template('resume.html', resume_text=resume_text)

# if __name__ == '__main__':
#     app.run(debug=True)


# from werkzeug.utils import secure_filename
# from flask import Flask, render_template, request, redirect, url_for
# import os

# app = Flask(__name__)

# UPLOAD_FOLDER = 'static/uploads/'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# # Переменная для хранения текста резюме
# resume_text = ""

# # Убедитесь, что папка существует
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     global resume_text
#     if request.method == 'POST':
#         if 'file' in request.files:
#             # Загрузка изображения
#             file = request.files['file']
#             if file and allowed_file(file.filename):
#                 filename = secure_filename(file.filename)
#                 file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#                 return redirect(url_for('index'))
#         elif 'resume_text' in request.form:
#             # Сохранение текста резюме
#             resume_text = request.form.get('resume_text', '')
#             return redirect(url_for('index'))
    
#     # Загрузка списка изображений
#     images = os.listdir(app.config['UPLOAD_FOLDER'])
#     return render_template('index.html', images=images, resume_text=resume_text)

# if __name__ == '__main__':
#     app.run(debug=True)


from werkzeug.utils import secure_filename
from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# Переменная для хранения данных резюме
resume_data = {
    "name": "",
    "birth_date": "",
    "qualification": "",
    "experience": "",
    "additional_info": ""
}

# Убедитесь, что папка существует
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    global resume_data
    if request.method == 'POST':
        # Обработка сохранения резюме
        if 'name' in request.form:
            resume_data = {
                "name": request.form.get('name', ''),
                "birth_date": request.form.get('birth_date', ''),
                "qualification": request.form.get('qualification', ''),
                "experience": request.form.get('experience', ''),
                "additional_info": request.form.get('additional_info', '')
            }
            return redirect(url_for('index'))
        
        # Обработка загрузки изображения
        if 'file' in request.files:
            file = request.files['file']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                return redirect(url_for('index'))
    
    images = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('index.html', images=images, resume_data=resume_data)

if __name__ == '__main__':
    app.run(debug=True)
