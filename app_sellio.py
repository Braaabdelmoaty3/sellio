from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = '330ce90ac2771bcd85ccb1d0ef2bef67'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
posts = []

"""make a database for user and post """

class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Post(db.Model):


    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

""" create the routing to every page in the website """

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
            # Use 'pbkdf2:sha256' as the hashing method
            hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
            
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

def create_tables():
    with app.app_context():
        db.create_all()

@app.route('/create_post', methods=['GET', 'POST'])
def create_post():
    if request.method == 'POST':
        bio = request.form['bio']
        posts.append({'bio': bio, 'comments': []})
        return redirect(url_for('view_posts'))
    return render_template('create_post.html')

@app.route('/posts')
def view_posts():
    return render_template('posts.html', posts=posts)

@app.route('/posts/<int:post_id>/comments', methods=['POST'])
def add_comment(post_id):
    comment = request.form['comment']
    if 0 <= post_id < len(posts):
        posts[post_id]['comments'].append(comment)
    return redirect(url_for('view_posts'))

if __name__ == '__main__':
    create_tables()
    app.run(debug=True)
