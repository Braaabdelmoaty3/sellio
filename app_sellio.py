from flask import Flask, render_template, url_for, flash, redirect, request
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = '330ce90ac2771bcd85ccb1d0ef2bef67'

@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html")

@app.route("/about")
def about_page():
    return render_template("about.html")

@app.route("/register", methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        
        if password != confirm_password:
            flash('Passwords do not match', 'danger')
        else:
            hashed_password = generate_password_hash(password, method='sha256')
            # Save user data to the database
            flash('Registration successful!', 'success')
            return redirect(url_for('home_page'))
    
    return render_template("registration.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        # Example of checking credentials, replace with actual user validation
        if email == 'admin@sellio.com' and password == 'password':
            flash('Login successful!', 'success')
            return redirect(url_for('home_page'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    
    return render_template("login.html")

if __name__ == '__main__':
    app.run(debug=True)
