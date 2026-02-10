import re
import sqlite3
from flask import request, jsonify, abort

USERNAME_RE = re.compile(r"^[A-Za-z0-9_.-]{1,64}$")  # adjust to your policy

@app.route("/user", methods=["GET"])
def user():
    init_db()

    username = (request.args.get("username") or "").strip()
    if not username:
        abort(400, description="Missing 'username' parameter")
    if not USERNAME_RE.fullmatch(username):
        abort(400, description="Invalid username format")

    # Use a context manager so the connection closes reliably
    try:
        with sqlite3.connect(DB) as conn:
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()

            # Parameterized query prevents SQL injection
            cur.execute(
                "SELECT id, username FROM users WHERE username = ? LIMIT 1",
                (username,),
            )
            row = cur.fetchone()

    except sqlite3.Error:
        # Avoid leaking internal DB error details to clients
        abort(500, description="Database error")

    if row is None:
        return jsonify({"error": "User not found"}), 404

    # Return structured JSON instead of raw tuple/string
    return jsonify({"id": row["id"], "username": row["username"]}), 200
