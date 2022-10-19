from flask import Flask, render_template, url_for, request
import pickle
import numpy as np
app = Flask(__name__)


knn2 = pickle.load(open('model.sav', 'rb'))
 


@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html")



@app.route('/result',methods=['POST', 'GET'])
def result():
    f1 = float(request.form['SepalLength'])
    f2 = float(request.form['SepalWidth'])
    f3 = float(request.form['PetalLength'])
    f4 = float(request.form['PetalWidth'])

    tst=np.array([[f1,f2,f3,f4]])
    rst=knn2.predict(tst)
    return render_template('index.html', name = format(rst))
    




if __name__ == "__main__":
    app.run(debug=True)