from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Database connection
def get_db_connection():
    conn = sqlite3.connect('opticrops.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

# Prediction form page
@app.route('/prediction')
def prediction():
    return render_template('prediction.html')

# Handle form submission
@app.route('/predict', methods=['POST'])
def predict():
    nitrogen = request.form['nitrogen']
    phosphorous = request.form['phosphorous']
    potassium = request.form['potassium']
    temperature = request.form['temperature']
    humidity = request.form['humidity']
    ph = request.form['ph']
    rainfall = request.form['rainfall']
    season = request.form['season']

    # Placeholder ML logic
    crop = "Wheat"
    confidence = "85%"  # placeholder
    fertilizer = "Urea (Placeholder)"
    irrigation = "Drip Irrigation (Placeholder)"

    # Save to DB
    conn = get_db_connection()
    conn.execute("INSERT INTO predictions (nitrogen, phosphorous, potassium, temperature, humidity, ph, rainfall, season, crop) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                 (nitrogen, phosphorous, potassium, temperature, humidity, ph, rainfall, season, crop))
    conn.commit()
    conn.close()

    return render_template('result.html', crop=crop, confidence=confidence, fertilizer=fertilizer, irrigation=irrigation)

if __name__ == '__main__':
    app.run(debug=True)
