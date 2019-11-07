from flask import Flask, render_template

app = Flask(__name__, static_folder='/Users/julianpeters/OneDrive - Wentworth Institute of Technology/Personal/Website/mywebsite/')

@app.route('/')
def home():

    return render_template("index.html")

if __name__=='__main__':
    app.run(debug = True)
