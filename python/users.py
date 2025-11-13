# import sqlite3
# import os

# def get_user_info(user_id):
   
#     conn = sqlite3.connect('test.db')
#     cursor = conn.cursor()
#     query = f"SELECT * FROM users WHERE id = '{user_id}'"  
#     cursor.execute(query) 
#     user_info = cursor.fetchall()
#     conn.close()
#     return user_info

#  def run_command(command):
    
#     os.system(f"ping {command}")  
    
#     if __name__ == "__main__":
#      user_input = input("Enter the user ID: ")
#      print(get_user_info(user_input))

#      command_input = input("Enter the IP Address to ping: ")
    #  run_command(command_input)
# Vulnerability 3: Hardcoded Password (CWE-259)
# DB_PASSWORD = "supersecret123"  # Hardcoded secret

# Vulnerability 4: Deserialization of Untrusted Data (CWE-502)
# def load_data(data):
#     import pickle
#     return pickle.loads(data)  # Unsafe deserialization

# Vulnerability 5: Exposed Secret in Code

# AWS_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"
# AWS_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"