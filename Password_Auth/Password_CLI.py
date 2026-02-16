from flask import Flask, request, jsonify
import argon2
import time
import json
import os

app = Flask(__name__)

# Reuse one Argon2 hasher (same reasoning as before)
ph = argon2.PasswordHasher()

USERS_FILE = "users.json"


# ---------- Storage helpers ----------

def load_users():
    if not os.path.exists(USERS_FILE):
        return {}

    try:
        with open(USERS_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {}


def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=4)


# ---------- Password rules ----------

def password_valid(password):
    if len(password) < 8:
        return False, "Password must be at least 8 characters"
    if not any(c.isdigit() for c in password):
        return False, "Password must contain a digit"
    if not any(c.isupper() for c in password):
        return False, "Password must contain an uppercase letter"
    if not any(c.islower() for c in password):
        return False, "Password must contain a lowercase letter"
    return True, None


# ---------- Routes ----------

@app.route("/register", methods=["POST"])
def register():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 400

    users = load_users()

    if username in users:
        return jsonify({"error": "Username already exists"}), 400

    ok, msg = password_valid(password)
    if not ok:
        return jsonify({"error": msg}), 400

    hashed = ph.hash(password)

    users[username] = {
        "hash": hashed,
        "attempts": 0,
        "locked_until": None
    }

    save_users(users)
    return jsonify({"message": "User registered successfully"}), 201


@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 400

    users = load_users()

    if username not in users:
        return jsonify({"error": "Invalid credentials"}), 401

    user = users[username]

    # Enforce lockout BEFORE verification
    locked_until = user["locked_until"]
    if locked_until and time.time() < locked_until:
        remaining = int(locked_until - time.time())
        return jsonify({
            "error": f"Account locked. Try again in {remaining} seconds"
        }), 403

    try:
        ph.verify(user["hash"], password)
        # Success
        user["attempts"] = 0
        user["locked_until"] = None
        save_users(users)
        return jsonify({"message": "Login successful"}), 200

    except argon2.exceptions.VerifyMismatchError:
        user["attempts"] += 1

        if user["attempts"] >= 5:
            user["locked_until"] = time.time() + 900
            user["attempts"] = 0
            save_users(users)
            return jsonify({"error": "Account locked for 15 minutes"}), 403

        save_users(users)
        return jsonify({"error": "Invalid credentials"}), 401


# ---------- Run ----------

if __name__ == "__main__":
    app.run(debug=True)
