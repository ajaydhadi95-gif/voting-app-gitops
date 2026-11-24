
from flask import Flask, render_template, request, jsonify
import sqlite3
import os

app = Flask(__name__)

DB_PATH = os.getenv("DB_PATH", "data/votes.db")

def get_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def initialize_db():
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS votes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            choice TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/vote", methods=["POST"])
def vote():
    data = request.get_json(silent=True) or {}
    choice = data.get("choice")

    if choice not in ["Python", "Java"]:
        return jsonify({"error": "Invalid vote"}), 400

    conn = get_db()
    conn.execute(
        "INSERT INTO votes (choice) VALUES (?)",
        (choice,)
    )
    conn.commit()
    conn.close()

    return jsonify({
        "message": "Vote submitted successfully",
        "choice": choice
    }), 201

@app.route("/api/results")
def results():
    conn = get_db()

    rows = conn.execute("""
        SELECT choice, COUNT(*) AS total
        FROM votes
        GROUP BY choice
    """).fetchall()

    conn.close()

    counts = {"Python": 0, "Java": 0}

    for row in rows:
        counts[row["choice"]] = row["total"]

    total = sum(counts.values())

    return jsonify({
        "Python": counts["Python"],
        "Java": counts["Java"],
        "total": total,
        "Python_percent": round(counts["Python"] / total * 100, 1) if total else 0,
        "Java_percent": round(counts["Java"] / total * 100, 1) if total else 0
    })

@app.route("/health")
def health():
    try:
        conn = get_db()
        conn.execute("SELECT 1")
        conn.close()
        return jsonify({"status": "healthy"}), 200
    except sqlite3.Error:
        return jsonify({"status": "unhealthy"}), 500

initialize_db()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
