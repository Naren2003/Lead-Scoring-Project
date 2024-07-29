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

    # int_features = [int(x) for x in request.form.values()]
    l = request.form
    int_features = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    int_features[1] = float(l['Total time spent'])
    if(l['Lead Origin'] == 'Lead Add Form'):
        int_features[2] = 1
    if(l['Lead Source'] == 'Olark Chat'):
        int_features[3] = 1
    if(l['Do not Email'] == 'Yes'):
        int_features[4] = 1
    if(l['Last Activity'] == 'Email Bounced'):
        int_features[5] = 1
    elif(l['Last Activity'] == 'Olark Chat Conversation'):
        int_features[6] = 1
    elif(l['Last Activity'] == 'SMS Sent'):
        int_features[7] = 1
    if(l['Through Recommendation'] == 'Yes'):
        int_features[8] = 1
    if(l['Last Notable Activity'] == 'Email Bounced'):
        int_features[9] = 1
    elif(l['Last Notable Activity'] == 'Link Clicked'):
        int_features[10] = 1
    elif(l['Last Notable Activity'] == 'Email Opened'):
        int_features[11] = 1
    elif(l['Last Notable Activity'] == 'Had a Phone Conversation'):
        int_features[12] = 1
    elif(l['Last Notable Activity'] == 'Modified'):
        int_features[13] = 1
    elif(l['Last Notable Activity'] == 'Olark Chat Conversation'):
        int_features[14] = 1
    elif(l['Last Notable Activity'] == 'Page Visited on Website'):
        int_features[15] = 1
    final_features = []
    final_features = [np.array(int_features)]
    # final_features = []
    # final_features.append(int_features)
    # print(final_features)
    prediction =  model.predict(final_features)
    output = "No"
    if(prediction[0] >= 0.41):
        output = "Yes"
    return render_template('index.html',prediction_text = "Lead Conversion Status - {}".format(output))

if __name__ == "__main__":
    app.run(debug = True)