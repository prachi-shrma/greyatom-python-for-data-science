# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading the file
data=pd.read_csv(path)

#Code starts here

# Step 1 
#Reading the file
loan_status=(data['Loan_Status']).value_counts()

#Creating a new variable to store the value counts


#Plotting bar plot
loan_status.plot(kind='bar')


# Step 2
#Plotting an unstacked bar plot
property_and_loan=data.groupby(['Property_Area','Loan_Status'])



#Changing the x-axis label
property_and_loan=property_and_loan.size().unstack()

#Changing the y-axis label
property_and_loan.plot(kind='bar',stacked=False)

#Rotating the ticks of X-axis
plt.xlabel('Property Area')
plt.ylabel('Loan Status')
plt.xticks(rotation=45)
# Step 3
#Plotting a stacked bar plot
education_and_loan=data.groupby(['Education','Loan_Status'])
education_and_loan=education_and_loan.size().unstack()
education_and_loan.plot(kind='bar',stacked=True)

#Changing the x-axis label
plt.xlabel('Education Status')
plt.ylabel('Loan Status')

#Changing the y-axis label


#Rotating the ticks of X-axis
plt.xticks(rotation=45)

# Step 4 
#Subsetting the dataframe based on 'Education' column
graduate=pd.DataFrame(data[data['Education']=='Graduate'])

#Subsetting the dataframe based on 'Education' column
not_graduate=pd.DataFrame(data[data['Education']=='Not Graduate'])

#Plotting density plot for 'Graduate'
graduate['LoanAmount'].plot(kind='density',label='Graduate')

#Plotting density plot for 'Graduate'
not_graduate['LoanAmount'].plot(kind='density',label='Not Graduate')

#For automatic legend display


# Step 5
#Setting up the subplots
fig, (ax_1,ax_2,ax_3)=plt.subplots(nrows=3,ncols=1)

#Plotting scatter plot
ax_1.scatter(data['ApplicantIncome'],data['LoanAmount'])
ax_1.set(title='Applicant Income')
#Setting the subplot axis title
ax_2.scatter(data['CoapplicantIncome'],data['LoanAmount'])
ax_2.set(title='Coapplicant Income')

data['TotalIncome']=data['ApplicantIncome']+data['CoapplicantIncome']

#Plotting scatter plot
ax_3.scatter(data['TotalIncome'],data['LoanAmount'])
ax_3.set(title='Total Income')
#Setting the subplot axis title


#Creating a new column 'TotalIncome'


#Plotting scatter plot



#Setting the subplot axis title



