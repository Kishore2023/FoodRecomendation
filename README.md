# FoodRecomendation   -

**1.** **PROJECT OVERVIEW**

Recommendation system build for the multi – cuisine restaurant.
Model build for existing and New Customer based on previous order and New customer based on food. 
Collecting the data from Primary source(survey).  
Based on the collected data completing the preprocessing(EDA). 
Storing the data in Azure tools. And performing the Recommendation System based on Content based Filtering to find out the recommendation of the food based on the customer historic information based on the ingredients preferred.
The prediction would be suggesting  the recommended food to the customer. 
This will be automatically performed based on the Machine learning model.

**PROJECT SCOPE**

The Vendor can efficiently predict customer recommended food orders which is faster, more efficiently and cost effectively based on historical data. 
Predictive analysis helps decision makers in designing new recommendation strategies based on food orders which will help in customer improvement as well as overall growth to the business.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
**2.** **Business Objective:** 

The business objective to build a recommendation model to predict the recommended food based on customer exiting details or  food mostly preferred by other customers for a multi cuisine restaurant.

  Minimize:  Customer non - preferred food
  
  Maximize:  Preferred food options to customer to increase the profits in business

**Business Constraints:** 

	Recommending the customer's food based on previous order.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
**3.** **CRISP-ML(Q) Methodology**

1a. Business Understanding:  Understanding the Business Objects & Constraints for the Success Criteria

1b. Data Understanding:  Understanding the Data Types which is collected.

2. Data Preparation: Data being Cleansed and explored for feature engineering 

3. Model Building: Unsupervised Learning based model has been built - Recommendation System. 

4. Evaluation: Model also build in Azure AML process for accuracy check.

5. Model Deployment: Model used in the application streamlit, docker and deployed the model in Microsoft Azure.

6. Monitoring & Maintenance: Should be done using the Azure Monitoring Application
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
**4.** **Technical Stacks**

The systems used to build the model.

**Backend stacks**
Programming language – Python

Application Used : Spyder, Microsoft Visual Studio, Docker image creator.

Library Used :  Pandas, Pickle, Streamlit, NumPy, Simple Imputer, TfidfVectorizer, Linear Kernel

Data Preparation – Anaconda (Spyder & Jupyter notebook)

Data Storage- Microsoft Azure data storage.

Model Building - Microsoft Azure Machine Learning Workspace

**Frontend stacks**
App Development : Steamlit Webapp

Model Deployment : Microsoft Azure Web Services 

Monitoring : Azure Monitoring & Maintenance

---------------------------------------------------------------------------------------------------------------------------------------------------------------------
**5.** **Data Collection and Understanding**

**Data Collection:**

**Primary Source :**

Collecting the data from the customer based on survey responses.

**Data Understanding:**

Understanding the requirements of the objective and gathering those to provide the best output.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
**6.** **Data Information**

Data gathering from the primary source is in the form of structured data. 

Analyzing those data based on the objectives.

Survey Form and Data gathering has been done based on these Three Criteria :

![image](https://user-images.githubusercontent.com/114608753/201947203-8dbadef5-2318-425b-9678-a0dedf87c2eb.png)

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------**7.** **Data Dictionary**

**Restaurant Customer Information**

![image](https://user-images.githubusercontent.com/114608753/201948287-4b88d798-8f32-4da9-9669-ea492ad4cf9f.png)

**Restaurant Features about Customer**

![image](https://user-images.githubusercontent.com/114608753/201948511-104fadc4-39ab-4f03-8567-b50a8c52abf6.png)

**Customer Bill & Rating**

![image](https://user-images.githubusercontent.com/114608753/201948720-7b22ab70-046f-41d0-8487-f293d1e6a704.png)

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
**8.** **System Requirements**

Operating System: Windows 10

Anaconda Navigator System Requirements: Hardware requirements

CPU: 2 x 64-bit 2.8 GHz 8.00 GT/s CPUs.
RAM: 32 GB (or 16 GB of 1600 MHz DDR3 RAM)
Storage: 300 GB.

Anaconda Navigator Features Used:  Software requirements

Spyder
Microsoft Visual Studio
Docker

Loading the Image in a Container : Docker Hub version 20.10.20

Public Repository : GitHub, Streamlit, Heruko

WebApp Creation – Streamlit version 1.14.0 

Microsoft Azure – For Global requirements of the Webpage

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------



