import re
import sqlite3
from flask import request, jsonify, abort

@app.route("/user", methods=["GET"])
def user():
    init_db()

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
