# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file
bank_data = pd.read_csv(path)


#Code starts here
bank=pd.DataFrame(bank_data)
categorical_var=bank.select_dtypes(include='object')
numerical_var=bank.select_dtypes(include='number')
categorical_var.shape
numerical_var.shape

banks=pd.DataFrame(bank.drop(['Loan_ID'],axis=1))
print(banks.isnull().sum())
bank_mode=banks.mode()
banks=banks.fillna(bank_mode)
avg_loan_amount=banks.pivot_table(index=['Gender','Married','Self_Employed'],values=['LoanAmount'],aggfunc=np.mean)
loan_approved_se=((banks['Self_Employed']=='Yes') & (banks['Loan_Status']=='Y')).sum()
loan_approved_nse=((banks['Self_Employed']=='No') & (banks['Loan_Status']=='Y')).sum()
percentage_se=(loan_approved_se*100/614)
print(percentage_se)
percentage_nse=(loan_approved_nse*100/614)
loan_term= banks['Loan_Amount_Term'].apply( lambda x:x/12)
big_loan_term=(banks['Loan_Amount_Term']>=25).sum()
loan_groupby=banks.groupby(banks['Loan_Status'])
loan_groupby=loan_groupby[['ApplicantIncome','Credit_History']]
mean_values=loan_groupby.agg([np.mean])





