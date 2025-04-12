from testing  import test
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def main():
    return render_template('index.html')
@app.route("/details.html")
def details():
    return render_template('details.html')

@app.route("/result.html", methods=['POST'])
def process():
    age = int(request.form['age'])
    weight=int(request.form['weight'])
    height=int(request.form['height'])
    duration=int(request.form['duration'])
    heartRate=int(request.form['heartRate'])
    bodyTemp=int(request.form['bodyTemp'])
    gender=request.form['gender']
    val = test(age,weight,height,duration,heartRate,bodyTemp,gender)
    return render_template('result.html', val=val)
@app.route('/index.html', methods=['POST'])
def index():
    return render_template('index.html')


app.run(debug=False)
