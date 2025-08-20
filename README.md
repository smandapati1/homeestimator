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

