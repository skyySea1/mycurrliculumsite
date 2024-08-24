from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    pdf_url = "https://docs.google.com/document/d/1EGVTt-IK8SNm6nX4YoJCV2u88YqtiYW2crzzYDWiQ9U/pub?embedded=true"
    return render_template('index.html', pdf_url=pdf_url)

if __name__ == '__main__':
    app.run(debug=True)
