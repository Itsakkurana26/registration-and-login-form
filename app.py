from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

# Create database tables
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return "Welcome! Use the `/register` endpoint to register users."


    # Validate input
    if not data or 'username' not in data or 'email' not in data or 'password' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    # Check if user exists
    if User.query.filter((User.username == data['username']) | (User.email == data['email'])).first():
        return jsonify({'error': 'Username or Email already exists'}), 400

    # Add user to the database
    new_user = User(username=data['username'], email=data['email'], password=data['password'])
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'}), 201

if __name__ == '__main__':
    app.run(debug=True)
