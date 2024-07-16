import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd

app = Flask(__name__)
# model = pickle.load(open('model.pkl','rb'))
model = pd.read_pickle("model.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    # for rendering results on HTML GUI

    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction =  model.predict(final_features)
    output = "No"
    if(prediction[0] >= 0.41):
        output = "Yes"
    return render_template('index'.html,prediction_text = "Lead Conversion Status $ {}".format(output))

if __name__ == "__main__":
    app.run(debug = True)