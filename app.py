from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect("feedback.db")
    return conn

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        message = request.form["message"]

        conn = get_db()
        cur = conn.cursor()
        cur.execute("INSERT INTO feedback (name, message) VALUES (?, ?)", (name, message))
        conn.commit()
        conn.close()

        return redirect("/view")

    return render_template("index.html")

@app.route("/view")
def view():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM feedback")
    data = cur.fetchall()
    conn.close()

    return render_template("view.html", feedback=data)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)

