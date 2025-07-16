# # Vulnerability 1: SQL Injection (CWE-89)
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
    
# # Vulnerability 3: Hardcoded Password (CWE-259)
# DB_PASSWORD = "supersecret123"  # Hardcoded secret

# # Vulnerability 4: Deserialization of Untrusted Data (CWE-502)
# def load_data(data):
#     import pickle
#     return pickle.loads(data)  # Unsafe deserialization

# # Vulnerability 5: Exposed Secret in Code

# AWS_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"
# AWS_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"