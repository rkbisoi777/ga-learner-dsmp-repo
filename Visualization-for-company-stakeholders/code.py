# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_csv(path)
#print(data.head())
loan_status = data['Loan_Status'].value_counts()
loan_status.plot(kind='bar', figsize=(15,10))
plt.show()

#Code starts here


# --------------
#Code starts here
property_and_loan = data.groupby(['Property_Area', 'Loan_Status']).size().unstack()
property_and_loan.plot(kind='bar', stacked=False, figsize=(15,10))
plt.xlabel('Property Area', rotation=45)
plt.ylabel('Loan Status')



# --------------
#Code starts here
education_and_loan = data.groupby(['Education','Loan_Status']).size().unstack()
plt.scatter(x='Education', y='Loan_Status')
plt.xlabel('Education Status', rotation=45)
plt.ylabel('Loan Status')


# --------------
#Code starts here
graduate = data[data['Education'] == 'Graduate']
not_graduate = data[data['Education'] == 'Not Graduate']
graduate.plot(kind='density',label='Graduate')
not_graduate.plot(kind='density',label='Not Graduate')










#Code ends here

#For automatic legend display
plt.legend()


# --------------
#Code starts here
fig, (ax_1, ax_2, ax_3) = plt.subplots(3,2, figsize=(20,10))
plt.scatter(x='ApplicantIncome', y='LoanAmount', label = 'Applicant Income')
#ax_1.set_title('Applicant Income')
plt.scatter(x='CoapplicantIncome', y='LoanAmount', label = 'Coapplicant Income')
#ax_2.set_title('Coapplicant Income')
data['TotalIncome'] = data['ApplicantIncome'] + data['CoapplicantIncome']
plt.scatter(x='TotalTncome', y='LoanAmount', label='Total Income')
#ax_3.set_title('Total Income')


