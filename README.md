# 🏠 HomeEstimator — ML-Powered House Price Estimator

HomeEstimator is a **Python + Flask** web app that estimates home values from user-entered features. It loads a pre-trained model from `./modelll/` and serves a clean HTML UI from `./templates/` with styles in `./theme/`.

---

## ✨ Features

- 🔢 **Model-driven predictions** — Load a serialized ML model (e.g., `house_price_model.pkl`) and return an estimated price.
- 🧑‍💻 **Simple web UI** — HTML form (Jinja2 templates) for input fields like bedrooms, bathrooms, sqft, etc.
- ⚙️ **Modular structure** — Separate folders for model, templates, and theme assets.
- 🚀 **Fast local setup** — One copy-paste to install and run.

---

## 🧱 Project Structure

homeestimator/
├─ app.py # Flask app entry point (routes + predict logic)
├─ requirements.txt # Python dependencies
├─ modelll/ # Trained model(s), e.g., house_price_model.pkl
├─ templates/ # Jinja2 HTML templates (forms/results)
└─ theme/ # CSS and static assets


> Note: The model directory name is `modelll` (three L’s). Ensure your code references the same path to avoid `FileNotFoundError`.

---

## ▶️ Quickstart

### Mac/Linux — one copy-paste
```bash
python -m venv venv && source venv/bin/activate \
&& pip install -r requirements.txt \
&& python app.py

Windows (PowerShell) — one copy-paste
python -m venv venv; .\venv\Scripts\Activate.ps1; `
pip install -r requirements.txt; `
python app.py


Now open: http://localhost:5000

🔧 Configuration

Python: 3.9+ recommended

Port: defaults to 5000 (update in app.py if desired)

Model path: place your pickle file at ./modelll/house_price_model.pkl (or update the path in app.py)

🧠 Model: Train or Plug-In

You can plug in an existing model (drop the .pkl in modelll/) or train a quick baseline and save it:

# train_and_save.py (example baseline — replace with your data/features)
import pandas as pd, numpy as np, joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# Example: load your dataset with columns like: ['bedrooms','bathrooms','sqft','year_built','zip','price']
df = pd.read_csv("data/housing.csv")

X = df[['bedrooms','bathrooms','sqft','year_built','zip']].fillna(0)
y = df['price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=300, random_state=42)
model.fit(X_train, y_train)

import os; os.makedirs("modelll", exist_ok=True)
joblib.dump(model, "modelll/house_price_model.pkl")

print("Saved model to modelll/house_price_model.pkl")


Run:

python train_and_save.py


Update app.py to load from modelll/house_price_model.pkl (if it doesn’t already).

🌐 How It Works (Typical Flow)

User opens / and fills in home features.

app.py validates and vectorizes inputs.

Model loaded from ./modelll/ predicts the price.

The result is rendered on a results page.

🧪 Local Testing Tips

Sanity check: Try small/large sqft to see estimates change.

Edge cases: Missing or non-numeric entries should be handled (add try/except + form validation).

Logging: Add print()/logging in app.py to debug inputs/predictions.

🚀 Deployment (Optional)

Render: Easiest path for Flask. Add a Procfile:

web: gunicorn app:app


And set a Build Command: pip install -r requirements.txt
Start Command: gunicorn app:app

Docker (if you add a Dockerfile):

FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]

🧰 Troubleshooting

FileNotFoundError: ... house_price_model.pkl
Ensure the file exists at ./modelll/house_price_model.pkl and that app.py points to the same path.
Also confirm the folder name is modelll (three L’s).

Port already in use
Stop other servers or change the port in app.py (e.g., app.run(port=5050)).

Module errors
Re-install deps: pip install -r requirements.txt (prefer a virtual env).
