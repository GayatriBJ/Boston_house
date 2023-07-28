from flask import Flask, jsonify, request, render_template
from utils import BostonData
import pickle

app= Flask(__name__)

@app.route('/')
def home():
    return jsonify({"Result":"Successful"})

@app.route('/houseprice_prediction', methods = ["POST"])
def get_predicted_houseprice():
    data = request.form
    print("Data :", data)

    CRIM    = data["CRIM"]
    ZN      = data["ZN"]
    INDUS   = data["INDUS"]
    NOX     = data["NOX"]
    RM      = data["RM"]
    AGE     = data["AGE"]
    RAD     = data["RAD"]
    TAX     = data["TAX"]
    PTRATIO = data["PTRATIO"]
    LSTAT   = data["LSTAT"]

    obj1 = BostonData()

    PREDICTED_HOUSEPRICE = (obj1.get_predicted_houseprice(CRIM,ZN,INDUS,NOX,RM,AGE,RAD,TAX,PTRATIO,LSTAT))*1000
    return jsonify({"Return" : f"PREDICTED HOUSEPRICE is {PREDICTED_HOUSEPRICE}"})

if __name__ == "__main__":
    app.run(host = "0.0.0.0" , port = 8080)