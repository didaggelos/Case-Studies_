
# ####  Describe the dataset and any issues with it.

#importing required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#reading data from csv file
df = pd.read_csv("loans_full_schema.csv")
df.head()

#checking dimension of data
df.shape

#summary of data
df.describe()

#checking info of data
df.info()

#columns with null values
a = df.isnull().sum() > 0
df.loc[:,a.values].isnull().sum()

#removing columns with too many null values and with too many categories
df2 = df.drop(columns = ['emp_title', 'emp_length', 'annual_income_joint', 'verification_income_joint', 'debt_to_income_joint',
                        'months_since_last_delinq', 'months_since_90d_late', 'months_since_last_credit_inquiry',
                        'num_accounts_120d_past_due', 'state', 'sub_grade'])


#plotting distribution of debt to income
df2['debt_to_income'].hist();





#filling null values with median value of debt to income
df2['debt_to_income'].fillna(df['debt_to_income'].median(), inplace = True)


# ##### Generate a minimum of 5 unique visualizations using the data and write a brief description of your observations. Additionally, all attempts should be made to 
# make the visualizations visually appealing.

#plotting relation between interest_rate and paid_interes
sns.set_style("darkgrid")
plt.figure(figsize = (10, 6))
sns.scatterplot(x = "paid_interest", y = "interest_rate", data = df2, hue = "grade")
plt.title("Relation between Interest Rate and Paid Interest by Grade", fontsize = 16)
plt.xlabel("Paid_interest", fontsize = 13)
plt.ylabel("Interest_rate", fontsize = 13)
plt.show()

#plotting relation between interest rate and homeowner ship
plt.figure(figsize = (10, 6))
sns.boxplot(x = "homeownership", y = "interest_rate", data = df2)
plt.title("Distribution of Interest Rate by Homeownership", fontsize = 16)
plt.xlabel("Homeownership", fontsize = 13)
plt.ylabel("Interest_rate", fontsize = 13)
plt.show()

#plotting distribution of Interest rate by loan_status
plt.figure(figsize = (10, 6))
sns.histplot(x = "interest_rate", hue = "verified_income", data = df2, multiple = "stack")
plt.title("Distribution of Interest Rate by Verified Income", fontsize = 16)
plt.xlabel("Interest_rate", fontsize = 13)
plt.ylabel("Count", fontsize = 13)
plt.show()

#Distribution of average Interest rate by loan_purpose
df2.groupby("loan_purpose")["interest_rate"].mean().sort_values().plot(kind = "bar", figsize = (10, 5))
plt.title("Distribution of Average Interest Rate by Loan Purpose", fontsize = 16)
plt.xlabel("loan_purpose", fontsize = 13)
plt.ylabel("interest_rate", fontsize = 13)
plt.xticks(rotation =90, fontsize = 12)
plt.show()

#distribution of Interest rate by issue_month
plt.figure(figsize = (10, 5))
sns.violinplot(x = "loan_status", y = "interest_rate", data = df2)
plt.title("Distribution of Interest Rate by Issue Month", fontsize = 16)
plt.xlabel("issue_month", fontsize = 13)
plt.ylabel("interest_rate", fontsize = 13)
plt.show()



# ####  Create a feature set and create a model which predicts interest_rate using at least 2 algorithms.

#### correlation matrix for numerical variables
plt.figure(figsize = (12, 12))
df2.select_dtypes(exclude = 'object').corr()['interest_rate']

#selecting significant features only
df2 = df2[['paid_interest', 'term', 'account_never_delinq_percent', 'total_debit_limit', 
           'accounts_opened_24m', 'total_credit_limit', 'inquiries_last_12m', 'earliest_credit_line', 'debt_to_income',
          'homeownership', 'verified_income', 'loan_purpose', 'application_type', 'grade', 'loan_status', 'initial_listing_status',
          'disbursement_method', "interest_rate"]]

#converting categorical variables into numerical variables
df2_num = pd.get_dummies(df2, drop_first = True)
#separating input and output features
X = df2_num.drop(columns = "interest_rate")
y = df["interest_rate"]

#splitting data into train and test data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 42)


# #### Linear Regression Model

#Initializing and fitting linear regression model
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(X_train, y_train)

#making predictions on test data
lr_preds = lr.predict(X_test)

#mean square error on test data
from sklearn.metrics import mean_squared_error
lr_mse = round(mean_squared_error(y_test, lr_preds), 3)
lr_mse

# #### Random Forest Regressor

#Initializing and fitting Random Forest model
from sklearn.ensemble import RandomForestRegressor
rfc = RandomForestRegressor(random_state = 42)
rfc.fit(X_train, y_train)

#Making predictions on test data
rfc_preds = rfc.predict(X_test)

#mean squared error of random forest model
rfc_mse = round(mean_squared_error(y_test, rfc_preds), 2)
rfc_mse



# ####  Describe any data cleansing that must be performed and analysis when examining the data. Visualize the test results and propose enhancements to the model, what
#  would you do if you had more time. Also describe assumptions you made and your approach.

#plotting actual vs predicted values for Linear Regression Model
plt.figure(figsize = (10,5))
sns.scatterplot(x = y_test, y = lr_preds)
plt.title("Actual Vs Predicted Values", fontsize = 16)
plt.xlabel("Actual Values", fontsize = 13)
plt.ylabel("Predicted values", fontsize = 13)
plt.show()


