from flask import Flask,request,jsonify,render_template
import logging
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)

import pickle
import numpy as np

app=Flask(__name__)
model=pickle.load(open("classifier.pkl","rb"))

@app.route("/")
def home():
    return render_template("main.html")


@app.route("/predict",methods=['POST','GET'])
def predict():
    float_features=[float(x) for x in request.form.values()]
    features=[np.array(float_features)]
    import sys

    print(features,  file=sys.stderr)

    prediction = model.predict(features)

    return render_template("result.html",prediction_text="It is {}".format(prediction))

if __name__=="__main__":
    app.run(debug=True)
 
