# app.py 

from flask import Flask,render_template, request, redirect, url_for, flash
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin,login_user,login_required,logout_user, current_user
from backend.carbon_calculator import calculate_emissions
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config['SECRET_KEY'] = '1010'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
Login_manager = LoginManager(app)
Login_manager.login_view = "login"

# User model 
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    
# Initialize database 
@Login_manager.user_loader

def load_user(user_id):
    return User.query.get(int(user_id))

# Home route login user only 
@app.route("/", methods=["GET","POST"])
@login_required
def index():
    if request.method == "POST":
        electricity = float(request.form["electricity"])
        mileage = float(request.form["mileage"])
        
        total, elec_emissions,car_emissions = calculate_emissions(electricity,mileage)
        return render_template("index.html",total = total,elec_emissions = elec_emissions,car_emissions = car_emissions)
    return render_template("index.html")

@app.route("/register", methods=["GET","POST"])

def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
# Check if the username is taken 

    if User.query.filter_by(username=username).first():
        flash("Username already exists. Please choose another. ", "danger")
        return redirect(url_for("register"))
# Hash the passcode and save the user in the database 
    hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")
    new_user = User(username=username,password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    
    flash("")

if __name__ == "__main__":
    app.run(debug=True)
    
