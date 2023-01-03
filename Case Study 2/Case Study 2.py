
#importing required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#reading data from csv file
df = pd.read_csv("CaseStudy.csv")
df.head()


# ####  Total revenue for the current year

#total revenu for current year 2015
total_revenue_2015 = round(df.query("year == 2015")["net_revenue"].sum(), 3)
total_revenue_2015

#total revenu for current year 2016
total_revenue_2016 = round(df.query("year == 2016")["net_revenue"].sum(), 3)
total_revenue_2016
#total revenu for current year 2017
total_revenue_2017 = round(df.query("year == 2017")["net_revenue"].sum(), 3)
total_revenue_2017

# #### New Customer Revenue e.g. new customers not present in previous year only

#separating data for years 2015, 2016 and 2017
df_2015 = df[df["year"] == 2015]
df_2016 = df[df["year"] == 2016]
df_2017 = df[df["year"] == 2017]

#new customer_revenue in 2016
d_2016 = df[(df["customer_email"].isin(df_2016["customer_email"].unique()) & ~df["customer_email"].isin(df_2015["customer_email"].unique()))]
new_customer_revenue_2016 = d_2016[d_2016["year"] == 2016]["net_revenue"].sum()
new_customer_revenue_2016

#new customer_revenue in 2017
d_2017 = df[(df["customer_email"].isin(df_2017["customer_email"].unique()) & ~df["customer_email"].isin(df_2015["customer_email"].unique()) & ~df["customer_email"].isin(df_2016["customer_email"].unique()))]
new_customer_revenue_2017 = d_2017[d_2017["year"] == 2017]["net_revenue"].sum()
new_customer_revenue_2017



# ####  Existing Customer Growth. To calculate this, use the Revenue of existing customers for current year –(minus) Revenue of existing customers from the previous 
# year

#customer growth for year 2016 compare to 2015
d_2015_2016= df[(~df["customer_email"].isin(df_2017["customer_email"].unique()) & df["customer_email"].isin(df_2015["customer_email"].unique()) & 
df["customer_email"].isin(df_2016["customer_email"].unique()))]
customer_growth_2016 = d_2015_2016[d_2015_2016["year"] == 2016]["net_revenue"].sum() - d_2015_2016[d_2015_2016["year"] == 2015]["net_revenue"].sum()
customer_growth_2016 = round(customer_growth_2016, 3)
customer_growth_2016

#customer growth for year 2017 compare to 2016
d_2016_2017= df[(df["customer_email"].isin(df_2017["customer_email"].unique()) & ~df["customer_email"].isin(df_2015["customer_email"].unique()) & df["customer_email"].isin(df_2016["customer_email"].unique()))]
customer_growth_2017 = d_2016_2017[d_2016_2017["year"] == 2017]["net_revenue"].sum() - d_2016_2017[d_2016_2017["year"] == 2016]["net_revenue"].sum()
customer_growth_2017 = round(customer_growth_2017, 3)
customer_growth_2017


# Existing customers growth in 2017 as compare to 2016 is 28751.41.

#revenue lost from attrition in 2016 as compare to 2015
df2 = df[(df["customer_email"].isin(df_2015["customer_email"].unique()) & ~ df["customer_email"].isin(df_2016["customer_email"].unique()) & ~ df["customer_email"].isin(df_2017["customer_email"].unique()))]
revenue_lost_2016 = round(df2["net_revenue"].sum(), 3)
revenue_lost_2016

#revnue lost from attrition in 2017 as compare to 2016
df3 = df[(df["customer_email"].isin(df_2015["customer_email"].unique()) & df["customer_email"].isin(df_2016["customer_email"].unique()) &
 ~ df["customer_email"].isin(df_2017["customer_email"].unique()))]
revenue_lost_2017 = round(df3["net_revenue"].sum(), 3)
revenue_lost_2017

# #### Existing Customer Revenue Current Year

#existing customer revnue in for current year 2016
df3 = df[df["year"] != 2017]
df3 = df3[(df3["customer_email"].isin(df_2015["customer_email"].unique()) & df3["customer_email"].isin(df_2016["customer_email"].unique()))]
df3[df3["year"] == 2016]["net_revenue"].sum()

#existing customer revnue in 2017
df3 = df[df["year"] != 2015]
df3 = df3[(df3["customer_email"].isin(df_2016["customer_email"].unique()) & df3["customer_email"].isin(df_2017["customer_email"].unique()))]
df3[df3["year"] == 2017]["net_revenue"].sum()



# #### Existing Customer Revenue Prior Year

#existing customer revnue in prior year 2015
df3 = df[df["year"] != 2017]
df3 = df3[(df3["customer_email"].isin(df_2015["customer_email"].unique()) & df3["customer_email"].isin(df_2016["customer_email"].unique()))]
df3[df3["year"] == 2015]["net_revenue"].sum()

#existing customer revnue in prior year 2016
df3 = df[df["year"] != 2015]
df3 = df3[(df3["customer_email"].isin(df_2016["customer_email"].unique()) & df3["customer_email"].isin(df_2017["customer_email"].unique()))]
df3[df3["year"] == 2016]["net_revenue"].sum()

# #### Total Customers Current Year

#total customers in 2016
df[df["year"] == 2016]["customer_email"].nunique()

#total customers in 2017
df[df["year"] == 2017]["customer_email"].nunique()



# #### Total Customers Previous Year

#total customers in year 2015
df[df["year"] == 2015]["customer_email"].nunique()

#total customers in year 2016
df[df["year"] == 2016]["customer_email"].nunique()

# #### New Customers

#new customers in 2016
df2 = df[df["year"] != 2017]
df3 = df2[(df2["customer_email"].isin(df_2016["customer_email"].unique())) & (~df2["customer_email"].isin(df_2015["customer_email"].unique()))]
df3['customer_email'].nunique()

#new customers in 2017
df3 = df[(df["customer_email"].isin(df_2017["customer_email"].unique())) & (~df["customer_email"].isin(df_2015["customer_email"].unique())) & (~df["customer_email"].isin(df_2016["customer_email"].unique()))]
df3['customer_email'].nunique()

# #### Lost Customers

#lost customers in 2016
df_l_2016 = df[(df["customer_email"].isin(df_2015["customer_email"].unique())) & (~df["customer_email"].isin(df_2016["customer_email"].unique())) &
               (~df["customer_email"].isin(df_2017["customer_email"].unique()))]
df_l_2016["customer_email"].nunique()

#lost customers in 2017
df_l_2017 = df[(df["customer_email"].isin(df_2017["customer_email"].unique())) & (~df["customer_email"].isin(df_2016["customer_email"].unique())) &
               (~df["customer_email"].isin(df_2015["customer_email"].unique()))]
df_l_2017["customer_email"].nunique()

# #### Additionally, generate a few unique plots highlighting some information from the dataset. Are there any interesting observations?

#plotting distribution of net_revenue by year
import seaborn as sns
import matplotlib.pyplot as plt
plt.figure(figsize = (10,6))
sns.boxplot(x = "year", y = "net_revenue", data = df)
plt.title("Distribution of Net Revenue by Year", fontsize = 16)
plt.show()

#plotting distribution of existing customers revenue by year
df2 = df[df["year"] != 2017]
df3 = df2[(df2["customer_email"].isin(df_2016["customer_email"].unique())) & (df2["customer_email"].isin(df_2015["customer_email"].unique()))]
df3 = df3[df3["year"] == 2016]
df4 = df[(df["customer_email"].isin(df_2017["customer_email"].unique())) & (df["customer_email"].isin(df_2015["customer_email"].unique()) | df["customer_email"].isin(df_2016["customer_email"].unique()))]
df5 = df4[df4["year"] == 2017]
dff = pd.concat([df3, df5])
#plt.figure()
dff.groupby("year")["net_revenue"].sum().plot(kind = "bar", figsize = (10, 6))
plt.title("Total Existing customers revenue by year", fontsize = 16)
plt.show()


#plotting total revenue for new customers by year
df2 = df[df["year"] != 2017]
df3 = df2[(df2["customer_email"].isin(df_2016["customer_email"].unique()) & ~df2["customer_email"].isin(df_2015["customer_email"].unique()))]
df4 = df[(df["customer_email"].isin(df_2017["customer_email"].unique()) & ~df["customer_email"].isin(df_2016["customer_email"].unique()) & ~df["customer_email"].isin(df_2015["customer_email"].unique()))]
df5 = pd.concat([df3, df4])
df5.groupby("year")["net_revenue"].sum().plot(kind = "bar", figsize = (10, 6))
plt.title("Total New customers revenue by year", fontsize = 16)
plt.show()
