from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html', name='Jerry')

@app.route("/yum")
def yumpage():
    return render_template('yum.html', name = "Hello, World yum yum!!!")
    
    
if __name__ == "__main__":
    app.run(debug=True)
    