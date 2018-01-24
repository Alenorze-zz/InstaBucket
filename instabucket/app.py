from flask import Flask, url_for, redirect, render_template, request

app = Flask(__name__)

@app.route('/')
def dashboard():
    return "this is the dashboard"

@app.route('/leaderboard')
def leaderboard():
    return "this is the leaderboard"

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        if email == "test@alenorze.pro" and password == "123":
            return redirect(url_for('dashboard'))
    return render_template("login.html")

if __name__  == "__main__":
    app.run(debug=True)
