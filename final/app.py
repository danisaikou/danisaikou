from flask import Flask, flash, redirect, render_template, request, session, url_for, abort, g
import sqlite3
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

#Set a secret key
app.config['SECRET_KEY'] = 'your secret key'

# Connect the database
connection = sqlite3.connect('inventory.db')
cur = connection.cursor()

def get_db_connection():
    conn = sqlite3.connect('inventory.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/newtown/", methods=["GET", "POST"])
def newtown():
    conn = get_db_connection()
    Size = request.form.get("Size", "%")
    rows = conn.execute("SELECT * FROM ShopType INNER JOIN Items ON Items.ShopTypeID = ShopType.ID WHERE Size = ?", (Size,))
    return render_template("newtown.html", inventory=rows)

print("Success")
