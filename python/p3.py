def get_users(username):
    import sqlite3
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = '" + username + "'"  
    cursor.execute(query)
    return cursor.fetchall()

def ping_a_host(host):
    import os
    os.system("ping -c 1 " + host)  
    
# Vulnerability 3: Hardcoded Password (CWE-259)
DB_PASSWORD = "superpass123"  # Hardcoded secret

# Vulnerability 4: Deserialization of Untrusted Data (CWE-502)
def load_data(data):
    import pickle
    return pickle.loads(data)  # Unsafe deserialization

