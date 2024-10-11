from flask import Flask, render_template
from prometheus_flask_exporter import PrometheusMetrics
# from flask_sqlalchemy import SQLAlchemy
# from flask_bcrypt import Bcrypt
# from flask_login import LoginManager, UserMixin, login_user
# from flask_login import logout_user, login_required, current_user


app = Flask(__name__)


# Prometheus monitoring
metrics = PrometheusMetrics(app)


# Database and security configuration
# app.config['SECRET_KEY'] = 'your_secret_key'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'


# Initialize extensions
# db = SQLAlchemy(app)
# bcrypt = Bcrypt(app)
# login_manager = LoginManager(app)
# login_manager.login_view = 'login'


# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))


# Define User model for database
# class User(db.Model, UserMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(150), unique=True, nullable=False)
#     email = db.Column(db.String(150), unique=True, nullable=False)
#     password = db.Column(db.String(60), nullable=False)

#     def __repr__(self):
#         return f"User('{self.username}', '{self.email}')"


# Route: Home page
@app.route('/')
# @login_required
def home():
    return render_template('index.html')


# Route: Personal info page
@app.route('/personal-info')
def personal_info():
    return render_template('personal_info.html')


# Route: About page
@app.route('/about')
def about():
    return render_template('about.html')


# Route: Register
# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         username = request.form['username']
#         email = request.form['email']
#         password = request.form['password']
#         hashedp = bcrypt.generate_password_hash(password).decode('utf-8')
#         user = User(username=username, email=email, password=hashedp)
#         db.session.add(user)
#         db.session.commit()
#         flash('Your account has been created!', 'success')
#         return redirect(url_for('login'))
#     return render_template('register.html')


# Route: Login
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         email = request.form['email']
#         password = request.form['password']
#         user = User.query.filter_by(email=email).first()
#         if user and bcrypt.check_password_hash(user.password, password):
#             login_user(user)
#             flash('Login successful!', 'success')
#             return redirect(url_for('home'))
#         else:
#             flash('Login failed. Check your email and password.', 'danger')
#     return render_template('login.html')

# Route: Logout


# @app.route('/logout')
# def logout():
#     logout_user()
#     flash('You have been logged out.', 'info')
#     return redirect(url_for('login'))


# Protected route: Dashboard (only accessible after login)
# @app.route('/dashboard')
# # @login_required
# def dashboard():
#     return render_template('dashboard.html', username=current_user.username)


# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
