from flask import Flask, jsonify, request, render_template
from utils import BostonData
import numpy as np

app= Flask(__name__)

@app.route('/')
def home():
    return render_template("sample.html")

@app.route('/houseprice_prediction', methods = ["POST"])
def get_houseprice_prediction():
    data = request.form
    print("Data :", data)

    CRIM = data["CRIM"]
    ZN= data["ZN"]
    INDUS= data["INDUS"]
    NOX= data["NOX"]
    RM= data["RM"]
    AGE= data["AGE"]
    RAD= data["RAD"]
    TAX= data["TAX"]
    PTRATIO= data["PTRATIO"]
    LSTAT= data["LSTAT"]

    obj1 = BostonData()
    PREDICTED_HOUSEPRICE = np.around((obj1.get_predicted_houseprice(CRIM,ZN,INDUS,NOX,RM,AGE,RAD,TAX,PTRATIO,LSTAT))*1000, 2)
    return render_template("sample.html" , PREDICTEDHOUSEPRICE = PREDICTED_HOUSEPRICE)

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 8080)