from flask import Flask, render_template, request, flash
import pandas as pd
import pickle
import os

app = Flask(__name__)
app.secret_key = "opticrop_secret_key"

MODEL_PATH = "model/model.pkl"

model = None

# -----------------------------
# Load ML Model
# -----------------------------
try:
    if os.path.exists(MODEL_PATH):
        with open(MODEL_PATH, "rb") as file:
            model = pickle.load(file)
        print("Model Loaded Successfully")
    else:
        print("Model file not found.")
except Exception as e:
    print("Error loading model:", e)


# -----------------------------
# Home
# -----------------------------
@app.route("/")
def home():
    return render_template("index.html")


# -----------------------------
# About
# -----------------------------
@app.route("/about")
def about():
    return render_template("about.html")


# -----------------------------
# Contact
# -----------------------------
@app.route("/contact")
def contact():
    return render_template("contact.html")


# -----------------------------
# Prediction Page
# -----------------------------
@app.route("/prediction")
def prediction():
    return render_template("prediction.html")


# -----------------------------
# Prediction Logic
# -----------------------------
@app.route("/predict", methods=["POST"])
def predict():

    if model is None:
        flash("Machine Learning model not found.", "danger")
        return render_template("prediction.html")

    try:

        N = float(request.form["N"])
        P = float(request.form["P"])
        K = float(request.form["K"])
        temperature = float(request.form["temperature"])
        humidity = float(request.form["humidity"])
        ph = float(request.form["ph"])
        rainfall = float(request.form["rainfall"])

        input_data = pd.DataFrame(
            [[
                N,
                P,
                K,
                temperature,
                humidity,
                ph,
                rainfall
            ]],
            columns=[
                "N",
                "P",
                "K",
                "temperature",
                "humidity",
                "ph",
                "rainfall"
            ]
        )

        crop = model.predict(input_data)[0]

        return render_template(
            "result.html",
            crop=crop,
            nitrogen=N,
            phosphorous=P,
            potassium=K,
            temperature=temperature,
            humidity=humidity,
            ph=ph,
            rainfall=rainfall
        )

    except Exception as e:
        flash(str(e), "danger")
        return render_template("prediction.html")


# -----------------------------
# 404 Error
# -----------------------------
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


# -----------------------------
# Main
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)