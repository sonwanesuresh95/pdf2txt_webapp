from flask import Flask, request, render_template

from pdfprocessor import PDFprocess

app = Flask(__name__)
app.debug = True
UPLOAD_FOLDER = './saved_file'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

P = PDFprocess()


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/extract', methods=['GET', 'POST'])
def extract():
    try:
        file = request.files['myfile']
        file.save('./saved_file/saved_file.pdf')
        url = './extracted_text/output.csv'
        text = P.extract_from_pdf()
        msg = P.wordcount(text)
        if msg == 'success':
            return render_template('output.html', url=url, text=text)
        else:
            return 'failed'
    except Exception as e:
        return str(e)


if __name__ == "__main__":
    app.run(port='9595')
