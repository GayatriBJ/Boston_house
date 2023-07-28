import pickle
import numpy as np
import config

class BostonData():
    def __init__(self):
        pass

    def get_data(self):

        with open(config.MODEL_FILE_PATH, "rb") as f:
            self.model=pickle.load(f)

        with open(config.SCALER_FILE_PATH, "rb") as f:
            self.scaler=pickle.load(f)

    def get_predicted_houseprice(self,CRIM,ZN,INDUS,NOX,RM,AGE,RAD,TAX,PTRATIO,LSTAT):

        self.get_data()
    
        CRIM,ZN,INDUS,NOX,RM,AGE,RAD,TAX,PTRATIO,LSTAT = self.scaler.fit_transform([[CRIM,ZN,INDUS,NOX,RM,AGE,RAD,TAX,PTRATIO,LSTAT]])[0]
            
        test_array=np.zeros([1,self.model.n_features_in_])
        test_array[0,0] =CRIM
        test_array[0,1] =ZN
        test_array[0,2] =INDUS
        test_array[0,3] =NOX
        test_array[0,4] =RM
        test_array[0,5] =AGE
        test_array[0,6] =RAD
        test_array[0,7] =TAX
        test_array[0,8] =PTRATIO
        test_array[0,9] =LSTAT

        predicted_houseprice = self.model.predict(test_array)[0]
        return predicted_houseprice
    