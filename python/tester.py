# sql_injection.py
import sqlite3
from flask import Flask, request
from articles.config import Config


app = Flask(__name__)
DB = "test.db"



# Vulnerability 1: SQL Injection (CWE-89)


# def get_user(username):
#     import sqlite3
#     conn = sqlite3.connect('users.db')
#     cursor = conn.cursor()
#     query = "SELECT * FROM users WHERE username = '" + username + "'"  # SQLi
#     cursor.execute(query)
#     return cursor.fetchall()

# # Vulnerability 2: Command Injection (CWE-78)
# def ping_host(host):
#     import os
#     os.system("ping -c 1 " + host)  # Command injection
    
# Vulnerability 3: Hardcoded Password (CWE-259)
# DB_PASSWORD = "supersecret123"  # Hardcoded secret

# Vulnerability 4: Deserialization of Untrusted Data (CWE-502)
# def load_data(data):
#     import pickle
#     return pickle.loads(data)  # Unsafe deserialization

# Vulnerability 5: Exposed Secret in Code
app.run(debug=True, port=5002)
# AWS_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"
# AWS_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

# markupsafe.escape() converts special HTML characters (e.g. < → &lt;)
# so the browser renders the input as plain text, not executable HTML/JS.
# @app.route("/search/secure")
# def search_secure():
#     query = escape(request.args.get("q", ""))  # SAFE
#     return f"<h1>Results for: {query}</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=Config.DEBUG, port=Config.FLASK_PORT, use_reloader=Config.USE_RELOADER) 
