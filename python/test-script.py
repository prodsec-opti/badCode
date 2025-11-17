# Vulnerability 1: SQL Injection (CWE-89)
def get_user(username):
    import sqlite3
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = '" + username + "'"  # SQLi
    cursor.execute(query)
    return cursor.fetchall()


