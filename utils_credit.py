import pickle
import json
import numpy as np
import config

class LoanStatus():
    def __init__(self,Gender,Married,Dependents,Education,Self_Employed,
                 ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,
                 Credit_History,Property_Area):
        print("****** INIT Function *********")
        self.Gender =Gender
        self.Married = Married
        self.Dependents = Dependents
        self.Education = Education
        self.Self_Employed = Self_Employed
        self.ApplicantIncome = ApplicantIncome
        self.CoapplicantIncome = CoapplicantIncome
        self.LoanAmount = LoanAmount
        self.Loan_Amount_Term = Loan_Amount_Term
        self.Credit_History = Credit_History
        self.Property_Area = Property_Area
        

    def __load_saved_data(self):

        with open(config.MODEL_FILE_PATH,'rb') as f:
            self.logmodel = pickle.load(f)

        with open(config.JSON_FILE_PATH,'r') as f:
            self.Proj_data = json.load(f)

    def get_loan_status(self):
        self.__load_saved_data()

        Gender = self.Proj_data['Gender'][self.Gender]
        Married = self.Proj_data['Married'][self.Married]
        Dependents=self.Proj_data["Dependents"][self.Dependents]
        Education=self.Proj_data["Education"][self.Education]
        Self_Employed=self.Proj_data["Self_Employed"][self.Self_Employed]
        
        Property_Area = 'Property_Area_'+ self.Property_Area

        Property_Area_index = self.Proj_data["column_names"].index(Property_Area)

        test_array = np.zeros([1,self.logmodel.n_features_in_])
        test_array[0,0] = Gender
        test_array[0,1] = Married
        test_array[0,2] = Dependents
        test_array[0,3] = Education
        test_array[0,4] = Self_Employed
        test_array[0,5]=self.ApplicantIncome
        test_array[0,6]=self.CoapplicantIncome
        test_array[0,7]=self.Credit_History
        test_array[0,8]=self.LoanAmount
        test_array[0,9]=self.Loan_Amount_Term
        test_array[0,Property_Area_index] = 1

        predicted_loan_status = np.around(self.logmodel.predict(test_array)[0],3)
        return predicted_loan_status


