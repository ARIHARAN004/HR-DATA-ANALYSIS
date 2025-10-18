import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_excel("E:/excel/hr data.xlsx")
print(df)
print(df.head())
print(df.shape)
print(df.info())
print(df.describe(include="all"))
print(df.columns.tolist())
print(df.nunique())  # duplicate values find
print(df.isnull())
print(df.isnull().sum())
sumofemployees=df.shape[0]
print(f"TOTAL EMPLOYEES",sumofemployees)
attrition=df[df["Attrition"]=="Yes"].shape[0]
print(f"ATTRITION",attrition)
activeemployee=sumofemployees-attrition
print(f"ACTIVE EMPLOYEE",activeemployee)
attritionrate=attrition/sumofemployees*100
attritionrate1=round(attritionrate,2)
print(f"ATTRITION RATE",attritionrate1)
averageage=float(df["Age"].mean())
averageage1=round(averageage,2)
print(f"AVERAGE AGE",averageage1)
jobsatisficationrating=float(df["Job Satisfaction"].mean())
jobsatisficationrating1=round(jobsatisficationrating,2)
print(f"JOBSATISFICATIONRATING",jobsatisficationrating1)
data={
    "TOTAL EMPLOYEES":[sumofemployees],
    "ATTRITION":[attrition],
    "ACTIVE EMPLOYEES":[activeemployee],
    "ATTRITION RATE":[attritionrate1],
    "AVERAGE AGE":[averageage1],
    "JOB SATISFICATION RATING":[jobsatisficationrating1]
}
df1=pd.DataFrame(data)
print(df1)
#hr summary matrics
df1_transposed = df1.T
df1_transposed.columns = ['Value']
plt.barh(df1_transposed.index, df1_transposed['Value'])
plt.title('HR Summary Metrics')
plt.xlabel('Value')
plt.ylabel('Metric')
for i, value in enumerate(df1_transposed['Value']):
    plt.text(value + 0.5, i, str(value), va='center', fontsize=10, color='black')
plt.tight_layout()
plt.show()
#employess by gender
gender_counts = df['Gender'].value_counts()
labels = [f"{gender} ({count})" for gender, count in gender_counts.items()]
plt.pie(gender_counts,labels=labels,autopct='%1.1f%%', startangle=90)
plt.title('Employees by Gender')
plt.tight_layout()
plt.show()
#department wise attrition
dept_attrition = df[df['Attrition'] == 'Yes']['Department'].value_counts()
labels1 = [f"{department} ({count})" for department, count in dept_attrition.items()]
plt.pie(dept_attrition,labels=labels1,autopct='%1.1f%%', startangle=90 )
plt.title('Attrition by Department')
plt.tight_layout()
plt.show()
#education wise attrition
edu_attrition = df[df['Attrition'] == 'Yes']['Education'].value_counts().sort_index()
plt.barh(edu_attrition.index,edu_attrition.values, color='cornflowerblue')
for i, value in enumerate(edu_attrition.values):
    plt.text(value + 1, i, str(value), va='center', color='black', fontsize=10)
plt.title('Attrition by Education Level')
plt.xlabel('Number of Employees')
plt.ylabel('Education Level')
plt.tight_layout()
plt.show()
#attrition by job role
jobrole_attrition = df[df['Attrition'] == 'Yes']['Job Role'].value_counts()
sns.barplot(x=jobrole_attrition.values, y=jobrole_attrition.index)
for i, value in enumerate(jobrole_attrition.values):
    plt.text(value + 1, i, str(value), va='center', color='black', fontsize=10)
plt.title('Attrition by Job Role')
plt.xlabel('Number of Employees')
plt.ylabel('Job Role')
plt.tight_layout()
plt.show()
#attrition by marital
marital_attrition = df[df['Attrition'] == 'Yes']['Marital Status'].value_counts()
sns.barplot(x=marital_attrition.index, y=marital_attrition.values)
for i, value in enumerate(marital_attrition.values):
    plt.text(value +0.5, i, str(value), ha='center', va='bottom', fontsize=10,color='black')
plt.title('Attrition by Marital Status')
plt.xlabel('Marital Status')
plt.ylabel('Number of Employees')
plt.show()



