from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

model = joblib.load('modelll/house_price_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    input_data = {
        'Gr Liv Area': float(request.form['GrLivArea']),
        'Bedroom AbvGr': int(request.form['BedroomAbvGr']),
        'Full Bath': int(request.form['FullBath']),
        'Garage Cars': int(request.form['GarageCars']),
        'Year Built': int(request.form['YearBuilt']),
        'Neighborhood': request.form['Neighborhood'],
        'House Style': request.form['HouseStyle'],
        'Overall Qual': int(request.form['OverallQual']),
    }

    df = pd.DataFrame([input_data])
    prediction = model.predict(df)[0]

    return render_template('index.html', prediction=f"${prediction:,.0f}")

if __name__ == '__main__':
    app.run(debug=True)