from flask import Flask, request, render_template, send_file, redirect, url_for
import pandas as pd
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        cleaned_filepath = clean_data(filepath)
        return send_file(cleaned_filepath, as_attachment=True)

def clean_data(filepath):
    if filepath.endswith('.csv'):
        df = pd.read_csv(filepath)
    elif filepath.endswith('.xlsx'):
        df = pd.read_excel(filepath)
    else:
        raise ValueError("Unsupported file format")

    # Perform cleaning operations
    df.fillna(method='ffill', inplace=True)
    df.drop_duplicates(inplace=True)
    
    cleaned_filepath = os.path.join(app.config['UPLOAD_FOLDER'], 'cleaned_' + os.path.basename(filepath))
    if filepath.endswith('.csv'):
        df.to_csv(cleaned_filepath, index=False)
    elif filepath.endswith('.xlsx'):
        df.to_excel(cleaned_filepath, index=False)
    
    return cleaned_filepath

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)