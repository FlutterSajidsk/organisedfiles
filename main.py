import os
import shutil
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

def organize_files(source_folder, target_folder):
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    files = os.listdir(source_folder)

    for filename in files:
        source_path = os.path.join(source_folder, filename)

        if os.path.isfile(source_path):
            extension = os.path.splitext(filename)[1][1:]  # Get the file extension
            
            if extension:  # Ignore files without extensions
                extension_folder = os.path.join(target_folder, extension)
                
                if not os.path.exists(extension_folder):
                    os.makedirs(extension_folder)
                
                destination_path = os.path.join(extension_folder, filename)
                
                if not os.path.exists(destination_path):
                    shutil.move(source_path, destination_path)
                    print(f"Moved {filename} to {extension_folder}")
                else:
                    print(f"File {filename} already exists in {extension_folder}")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        source_folder = request.form['source_folder']
        target_folder = request.form['target_folder']
        organize_files(source_folder, target_folder)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
