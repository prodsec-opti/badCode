# Vulnerability 1: SQL Injection (CWE-89)
def get_user(username):
    import sqlite3
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = '" + username + "'"  # SQLi
    cursor.execute(query)
    return cursor.fetchall()

def ping_host(host):
    import os
    os.system("ping -c 1 " + host)  

    
@app.route("/user")
def user():
    init_db()
    username = request.args.get("username", "")
    # WARNING: vulnerable to SQL injection
    query = "SELECT id, username FROM users WHERE username = '%s'" % username
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute(query)
    row = cursor.fetchone()
    conn.close()
    return str(row)