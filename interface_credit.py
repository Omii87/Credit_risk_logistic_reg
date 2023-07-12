from flask import Flask, request, jsonify, render_template
from utils_credit import LoanStatus
import config

app = Flask(__name__)

@app.route('/')
def home1():
    
    return render_template('credit_risk.html')


@app.route('/predict_loan_status', methods = ['GET'])
def predict_loan_status():

    if request.method == 'GET':
        data = request.args.get
        print("Data :",data)
        
        Gender = data('Gender')
        Married = data('Married')
        Dependents = data('Dependents')
        Education=data('Education')
        Self_Employed=data('Self_Employed')
        ApplicantIncome = eval(data('ApplicantIncome'))
        CoapplicantIncome = eval(data('CoapplicantIncome'))
        LoanAmount = eval(data('LoanAmount'))
        Loan_Amount_Term=eval(data("Loan_Amount_Term"))
        Credit_History=eval(data('Credit_History'))
        Property_Area=data('Property_Area')

        Obj = LoanStatus(Gender, Married, Dependents,Education, Self_Employed,
       ApplicantIncome, CoapplicantIncome, LoanAmount,
       Loan_Amount_Term, Credit_History,Property_Area)
        pred_price = Obj.get_loan_status()
        
        #return jsonify({"Result":f"Predicted Loan Approval == {pred_price}"})
        return render_template('credit_risk.html', prediction = pred_price)

    elif request.method == 'POST':
        data = request.form
        print("Data :",data)
        Gender      = data['Gender']
        Married   = data['Married']
        Dependents      = data['Dependents']
        Education = data['Education']
        Self_Employed   = data['Self_Employed']
        ApplicantIncome   = data['ApplicantIncome']
        CoapplicantIncome =data['CoapplicantIncome']
        LoanAmount =data['LoanAmount']
        Loan_Amount_Term=data['Loan_Amount_Term']
        Credit_History=data['Credit_History']
        Property_Area=data['Property_Area']


        Obj = LoanStatus(Gender, Married, Dependents,Education, Self_Employed,
       ApplicantIncome, CoapplicantIncome, LoanAmount,
       Loan_Amount_Term, Credit_History,Property_Area)
        pred_price = Obj.get_loan_status()
        
        # return jsonify({"Result":f"Predicted Loan Approval == {pred_price}"})
        return render_template('medical_insurence.html', prediction = pred_price)

    return jsonify({"Message" : "Unsuccessful"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=config.PORT_NUMBER)
