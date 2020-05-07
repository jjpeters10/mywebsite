from flask import Flask, render_template, send_file

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/Resume')
def show_resume():
    return send_file('static/images/Resume_Hardware.pdf', attachment_filename='Resume.pdf')


@app.route('/Portfolio')
def show_portfolio():
    return send_file('static/images/Project_Portfolio_Hardware.pdf', attachment_filename='Project_Portfolio.pdf')

if __name__=='__main__':
    app.run(debug = True)
