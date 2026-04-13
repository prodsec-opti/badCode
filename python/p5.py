# sql_injection.py
import sqlite3
from flask import Flask, request

app = Flask(__name__)
DB = "test.db"

def init_db():
    conn = sqlite3.connect(DB)
    conn.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
    conn.execute("INSERT OR IGNORE INTO users (id, username, password) VALUES (1, 'alice', 'passw0rd')")
    conn.commit()
    conn.close()

@app.route("/user")
def user():
    init_db()
    username = request.args.get("username", "")
    #
    query = "SELECT id, username FROM users WHERE username = '%s'" % username
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute(query)
    row = cursor.fetchone()
    conn.close()
    return str(row)

    app.run(debug=True, port=5002)



AWS_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

# @app.route("/run")
# def run():
#     # WARNING: vulnerable to command injection
#     cmd = request.args.get("cmd", "ls")
#     output = os.popen(cmd).read()
#     return "<pre>{}</pre>".format(output)
