from flask import Flask, request
import sqlite3
import os

app = Flask(__name__)

@app.route("/login")
def login():
    username = request.args.get("username")
    password = request.args.get("password")

    conn = sqlite3.connect("users.db")

    # CHANGE: unsafe query construction (SQL Injection)
    sql = "SELECT * FROM users WHERE username = '%s' AND password = '%s'" % (username, password)
    conn.execute(sql)

    return "Logged in"

@app.route("/ping")
def ping():
    host = request.args.get("host")

    # CHANGE: user input passed directly to OS command (Command Injection)
    command = "ping -c 1 " + host
    os.system(command)

    return "Ping sent"
