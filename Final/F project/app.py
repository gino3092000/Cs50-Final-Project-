from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title='Nutritional Biomarker Laboratory', description='A detailed description here')

@app.route('/meet')
def meet():
    return render_template('meet.html', page_title='Meet the Team')

@app.route('/assay')
def assay():
    return render_template('assay.html', page_title='Assay Methods')

@app.route('/contact')
def contact():
    return render_template('contact.html', page_title='Contact Us!')

