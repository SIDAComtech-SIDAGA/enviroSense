# app.py 

from flask import Flask,render_template, request
from backend.carbon_calculator import calculate_emissions

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])

def index():
    if request.method == "POST":
        electricity = float(request.form["electricity"])
        mileage = float(request.form["mileage"])
        
        total, elec_emissions,car_emissions = calculate_emissions(electricity,mileage)
        return render_template("index.html",total = total,elec_emissions = elec_emissions,car_emissions = car_emissions)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
    
