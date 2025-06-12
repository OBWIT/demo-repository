import os
import subprocess

# 🚨 Hardcodiertes Secret (sollte von GitHub erkannt werden)
API_KEY = "ghp_1234567890abcdefEXAMPLESECRET"

# 🚨 Unsichere Verwendung von Benutzereingaben in Shell-Befehlen
def run_command():
    user_input = input("Gib einen Shell-Befehl ein: ")
    subprocess.call(user_input, shell=True)  # Command Injection möglich

# 🚨 Unsichere Speicherung von Passwörtern
def save_password(password):
    with open("passwords.txt", "a") as f:
        f.write(password + "\n")

# 🚨 Beispiel für SQL-Injection (wenn du sqlite3 einbinden willst)
def find_user(username):
    import sqlite3
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    return cursor.fetchall()

if __name__ == "__main__":
    print("Starte unsicheres Beispielprogramm...")
    run_command()
