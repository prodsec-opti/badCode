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

# # def run_command(command):
    
# #     os.system(f"ping {command}")  
    
# # if __name__ == "__main__":
# #     user_input = input("Enter the user ID: ")
# #     print(get_user_info(user_input))

# #     command_input = input("Enter the IP Address to ping: ")
# #     run_command(command_input)
