from flask import Flask, request, render_template
import numpy as np
import pickle
from tensorflow.keras.models import load_model
from sklearn.preprocessing import LabelEncoder
enoder = LabelEncoder()

model = load_model('model.joblib')
app = Flask(__name__)

@app.route('/')
def ma():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def index():
    if request.method == 'POST':
        d = {"Male":1,"Female":0}
        age = int(request.form['age'])
        gender = d[request.form['gender']]
        
        subscription_length = int(request.form['subscriptionLength'])
        monthly_bill = int(request.form['monthlyBill'])
        total_usage = int(request.form['totalUsage'])

        # Perform your churn prediction or desired processing here
        # Replace the following lines with your actual prediction logic
        prediction_result = model.predict(age,gender,subscription_length,monthly_bill)

    return prediction_result

if __name__ == '__main__':
    app.run(debug=True)
