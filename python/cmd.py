from flask import Flask, request
import os

app = Flask(__name__)

@app.route("/run")
def run():
    # WARNING: vulnerable to command injection
    cmd = request.args.get("cmd", "ls")
    output = os.popen(cmd).read()
    return "<pre>{}</pre>".format(output)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
def run_command(command):
    
    os.system(f"ping {command}")  
    
if __name__ == "__main__":
    user_input = input("Enter the user ID: ")
    print(get_user_info(user_input))

    command_input = input("Enter the IP Address to ping: ")
    run_command(command_input)

