def get_users(username):
    import sqlite3
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = '" + username + "'"  
    cursor.execute(query)
    return cursor.fetchall()

@app.route("/proxy")
def proxy():
    url = request.args.get("url", "https://example.com")

    # Intentionally insecure: turning off certificate validation.
    resp = requests.get(url, verify=False)  # LOW: SSL verification disabled
    return resp.text


if __name__ == "__main__":
    # Just to make it look like a real app
    app.run(host="0.0.0.0", port=5000, debug=True)

# if __name__ == "__main__":
#     app.run(debug=True, port=5002)


