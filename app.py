from flask import Flask, render_template, request, redirect, url_for, session
import pymysql
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Database Configuration (Using Environment Variables for Security)
DB_HOST = "beauty-salon-db.cr8k0suywf62.ap-south-1.rds.amazonaws.com"
DB_USER = "admin"
DB_PASSWORD = os.getenv("DB_PASSWORD", "Veeranji7777")
DB_NAME = "beauty_salon"

# Database Connection Function
def get_db_connection():
    return pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME)

@app.route('/')
def index():
    return "Welcome to the Beauty Salon Appointment Booking System!"

if __name__ == '__main__':
    app.run(debug=True)
