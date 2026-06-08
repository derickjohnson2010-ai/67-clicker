from flask import Flask, request, session, redirect
import random

app = Flask(__name__)
app.secret_key = "change_this"

@app.route("/")
def home():
    return '''
    <h1>67 Clicker Sign Up</h1>
    <form action="/signup" method="post">
        <input name="username" placeholder="Username"><br><br>
        <input name="password" type="password" placeholder="Password"><br><br>
        <input name="phone" placeholder="Phone Number"><br><br>
        <button type="submit">Send Verification Code</button>
    </form>
    '''
@app.route("/signup", methods=["POST"])
def signup():
    session["username"] = request.form["username"]
    session["password"] = request.form["password"]
    session["phone"] = request.form["phone"]
    code = str(random.randint(100000, 999999))
    session["code"] = code
    print(f"Verification code for {session['phone']}: {code}")
    return redirect("/verify")

@app.route("/verify")
def verify():
    return '''
    <h1>Verify Your Account</h1>
    <form method="post">
        <input name="code" placeholder="Verification Code">
        <button type="submit">Verify</button>
    </form>
    '''

@app.route("/verify", methods=["POST"])
def verify_post():
    if request.form["code"] == session.get("code"):
        return f"<h1>Account Created!</h1><p>Welcome, {session['username']}!</p>"
    return "<h1>Invalid Code</h1>"

if __name__ == "__main__":
    app.run(debug=True)
