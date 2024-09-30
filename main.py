from flask import Flask, request, render_template, send_file, jsonify
import requests
import pandas as pd
from tqdm import tqdm
import io

app = Flask(__name__)

def check_redirect(url):
    try:
        response = requests.get(url, allow_redirects=False)
        if 300 <= response.status_code < 400:
            return "Yes", response.headers['Location']
        else:
            return "No", None
    except requests.RequestException as e:
        return "Error", str(e)

def process_urls(urls):
    data = []
    for url in tqdm(urls, desc="Processing URLs", unit="url"):
        redirect_status, redirected_to = check_redirect(url)
        data.append([url, redirect_status, redirected_to])
    df = pd.DataFrame(data, columns=['Main URL', 'Redirect Status', 'Redirected To URL'])
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False)
    output.seek(0)
    return output

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_single_url', methods=['POST'])
def check_single_url():
    url = request.form.get('url')
    if url:
        redirect_status, redirected_to = check_redirect(url)
        return jsonify({
            'Main URL': url,
            'Redirect Status': redirect_status,
            'Redirected To URL': redirected_to
        })
    return jsonify({'error': 'No URL provided'}), 400

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file:
        urls = file.read().decode('utf-8').splitlines()
        output = process_urls(urls)
        return send_file(output, as_attachment=True, download_name='output.xlsx', mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

if __name__ == "__main__":
    app.run(debug=True)
