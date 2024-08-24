from flask import Flask, render_template
from flask.helpers import send_from_directory
import pdfplumber

app = Flask(__name__)

# Rota principal
@app.route('/')
def index():
    return render_template('index.html')

# Rota para exibir o PDF
@app.route('/pdf')
def pdf_view():
    pdf_path = 'curriculo.pdf'
    try:
        with pdfplumber.open(pdf_path) as pdf:
            # Extrair o texto do PDF
            text = ''
            for page in pdf.pages:
                text += page.extract_text() + '\n'
            return render_template('pdf_view.html', content=text)
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)
