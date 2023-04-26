from flask import Flask, render_template, request, send_file
import ipfshttpclient

app = Flask(__name__)

client = ipfshttpclient.connect()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    res = client.add(file)
    return f"File uploaded successfully. CID: {res['Hash']}"

@app.route('/download/<cid>')
def download(cid):
    file_contents = client.cat(cid)
    return send_file(file_contents, attachment_filename=cid)

@app.route('/login')
def login(regno):
    pass

@app.route('/register')
def register(regno):
    pass

@app.route('/verify')
def verify(regno):
    pass

if __name__ == '__main__':
    app.run(debug=True)
