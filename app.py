from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html', name='Jerry')

@app.route("/yum")
def yumpage():
    return "Hello, World yum yum!!!"
    
if __name__ == "__main__":
    app.run(debug=True)
    