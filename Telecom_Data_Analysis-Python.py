#!/usr/bin/env python
# coding: utf-8

#  # <span style="color:blue"> DATA ANALYSIS - TELECOM COMPANY </span>
# 
#  
#  Telecom is a fictional telecommunication company that provides internet and phone services to 7043 customers in California. Churn data is provided by the 'Maven Analytics'. 
#  ##  <span style="color:blue"> Problem Statement: </span>
#  Company want to improve retention by identifying high value customers and churn risk. Stakeholders want a report showing trends and looking for some recommendations for increasing the revenue.
#  
#  ##  <span style="color:blue"> Data collection: </span>
#  Data was provided by 'Maven Analytics' for a fictional company. Data includes 3 files with details about customer demographics, locations , service and current status. Csv file with 7043 rows and 38 columns was used for this EDA. It is Third party data.
#  
#  ##  <span style="color:blue"> Data Cleaning: </span>
#  Data cleaning includes finding and removing blanks or any duplicate entries. Also verifying the data to be consistent. Before starting, required libraries were imported.Then data was imported and called up for doing further analysis. Data analysis was done by using 'Python' for this case study.
#  
# 
#  

# In[2]:


# importing the required Libraries
import pandas as pd


# In[3]:


import numpy as np


# In[4]:


# import & export CSV files
CustomerData = pd.read_csv('~/telecom_customer_churn.csv')


# ##  Table used for this analysis 

# In[5]:


#Printing the exported CSV 
CustomerData


# ### Exploring the data by using info() function , it shows us total rows and columns in dataframe

# In[6]:



CustomerData.info()


# ### To check Mean, standard deviation, min and max values, we can use describe() function. It helps to know more about data and get an idea about all statistics of the data frame

# In[7]:


CustomerData.describe()


# ### Checking for Null Values

# In[16]:


# Lets check null values and try to clean it
#replacing NaN with 0
CustomerData.fillna(0)


# ### Dropping the blank values , Result showed 1586 rows left afte removing empty cells

# In[17]:


CustomerData.dropna()


# ### Sorting and filtering

# In[8]:


#Result of dropping shows that many rows have been removed as those were empty.
# Now for sorting on the basic of Total revenue from customers

TopCustomer = CustomerData.sort_values(by= ['Total Revenue'],ascending=False)


# In[13]:


TopCustomer


# ### Changing Data type for field required for analysis

# In[30]:


TopCustomer['Number of Referrals'] = TopCustomer['Number of Referrals'].astype(int)


# In[50]:


type(TopCustomer['Number of Referrals'])


#  ##  <span style="color:blue"> Data Analysis: </span>
#   This is mainly about discovering some useful insights so that company can make data-driven decision for its growth. So, follwoing steps were taken for analysis.
#  Creating pivot table quickly help to summarize the important numerical field. Here , as my focus is on churn, created pivot table for Customer status(chruned/joined/stayed) to know the effect on Total revenue.

# In[12]:



StatusVsRevenue = TopCustomer.pivot_table(index='Customer Status', values='Total Revenue', aggfunc=sum)
StatusVsRevenue


# In[30]:


StatusVsRevenue.info()


# ### Another pivot table for checking number of referral by Churned Customers

# In[5]:


# Also considering 'Referral' provided by each type of customer status
ReferralsVsRevenue = pd.pivot_table( CustomerData, index=["Customer Status"], values=['Number of Referrals', 'Total Revenue'], aggfunc={'Number of Referrals':np.sum,'Total Revenue':np.sum})


# In[97]:


ReferralsVsRevenue


# In[13]:


a=(ReferralsVsRevenue['Total Revenue'])
print(a)


# ### Finding out the percentage of revenue came from Customers who left the company. This will help us to know how much risk company can face from these customers.

# In[106]:


# finidng difference in revenue from stayed and churned customers
loss=(a[2]-a[0])
print(loss)


# In[109]:


Grand_Revenue= (a[0]+a[1]+a[2])
print(Grand_Revenue)


# In[129]:


# Showing loss in percentage,17% is occupied by customers who churned at the end of quarter
percentage=(a[0]/Grand_Revenue)*100
print(percentage.round(2))


# ### Also checking how many referrals were given by Churned customers

# In[6]:


#Checking referrals by churned customers (in percentage)
b=(ReferralsVsRevenue['Number of Referrals'])
print(b)
total_ref=(b[0]+b[1]+b[2])
print(total_ref)


# In[11]:


ref_perc=(b[0]/total_ref)*100
print((ref_perc).round(2))


# ### Analysing the reasons behind leaving Telecom. So it shows 20 reasons, company need to work on this for improving retention.

# In[31]:


List_of_reasons=(CustomerData['Churn Reason'].unique())
print(List_of_reasons)


# In[33]:


Reason_for_churn = CustomerData.groupby('Churn Reason')['Churn Reason'].count()
print(Reason_for_churn)


# ### So, three most common reasons that most customer gave while leaving are:
# 1. Competitor having better devices
# 2. Better offers from competitor company
# 3. Support person attitude issues.

# ##  <span style="color:blue"> Data Visualization: </span>
#  First we need to import 'matplotlib' for creating visuals. 
# ### 1. Scatter plot for Age and revenue: Scatter plot shows no relation between two and also the ages of customer is from all age groups. 

# In[29]:



import matplotlib.pyplot as plt


#Age Vs Revenue
x = TopCustomer['Age']
y = TopCustomer['Total Revenue']
plt.scatter(x, y)

plt.show()


# ### 2. Plot showing the trend for three categories of 'Customer status'

# In[31]:



  # Creating a plot to see realation of Customer status with Revenue generated
plt.plot(StatusVsRevenue["Total Revenue"])
  
# Title to the plot
plt.title("Customer Status Vs Revenue")
  

plt.show()


# ### 3. Bar chart  showing how much churned categort contributes to total revenue. Joined plays negligible role as per the data.

# In[62]:


# Creating bar chart 
StatusVsRevenue.plot(kind ="bar",title="Customer Status Vs Revenue" ,color='red')


# ### 4. Pie Chart highlighting the part of revenue from Churned customer

# In[17]:


y = np.array([a[0],a[1],a[2]])
mylabels = ["Churned", "Joined", "Stayed"]
myexplode = [0.1, 0, 0, ]
mycolors = ["red", "yellow", "green"]
plt.pie(y, labels = mylabels, explode = myexplode, colors = mycolors )
plt.show() 


# ### 5. Line graph showing both 'Total Revenue' and 'Referrals' from all Customers

# In[65]:


ReferralsVsRevenue.plot(kind ="line",title="Referrals Vs Revenue")
# Number of Referrals don't play any critical role for revenue


# ### 6 . Bar graph showing the reason behind leaving company. Bar graph clearly shows 3 most common reason that many customer talked about while leaving company. 

# In[13]:


Reason_for_churn.plot(kind ="bar",title="Reasons for churn" ,color='purple')


# ## <span style="color:blue"> Sharing useful insights from data and recommendation to stakeholders </span>
# 
# 
# 1. 17% of the total revenue is generated by the customer who left the company which is great risk for company.
# 2. 7% of total referral are from churned Customer
# 3. Age of customer is not a factor that effecting revenue 
# 4. Top 3 most common reasons that customer are leaving and joining competitor are showing that Support people are not good, Telecom offers and amount of data given by telecom is less compared to competitor company.
# 5. To improve the situation, training to 'support persons' on monthly basis focusing on 'assurance' and 'empthy' with customers. Also survey can be created for employees to know why attitude is one of the reason for customer leaving.
# 6. Rechecking of the offers given to customers and providing better offers to those who are loyal with company for many years.
# 7. Company can launch of scheme of 'gift hampers' after some time interval to improve customer-company relationship
# 
