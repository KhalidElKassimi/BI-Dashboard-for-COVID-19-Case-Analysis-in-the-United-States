# BI-Dashboard-for-COVID-19-Case-Analysis-in-the-United-States
## Introduction
COVID-19 has had a global impact, including in the United States. Dashboards have been created to monitor the pandemic and help decision-makers. Cosmos DB and Power BI are used to create a COVID-19 dashboard in the United States. Cosmos DB is ideal for storing data thanks to its scalability and availability. Data can be stored in JSON and organized into collections for easy management. Power BI is a popular tool for visualizing data and connecting to Cosmos DB to display interactive charts. Users can filter data by state or date. The dashboard can include graphs, maps and comparisons to show trends and forecasts based on historical data.
## Designs and tools
![image](https://github.com/KhalidElKassimi/BI-Dashboard-for-COVID-19-Case-Analysis-in-the-United-States/assets/110225378/246bc2e3-a24f-4a1a-b5cb-acbc18e346b0)

The Covid19 Data Visualization Project involves collecting, processing and visualizing Covid19 data in real-time using multiple tools and technologies. Here are the key steps involved in this project:
1. Data Collection: Covid19 data is collected from the CovidTracking API using the Python programming language. The API provides real-time data on confirmed cases, deaths, and recoveries related to Covid19 for the United States.
2. Sending data to Event Hub: The collected data is then sent to EventHub, a messaging and data streaming service in Azure. This allows data to be stored and processed in real time.
3. Data Processing: Azure Stream Analytics service is used to process data in real time. This allows real-time analysis and filtering of data before storing it in Cosmos DB
4. Data storage: Processed data is stored in Cosmos DB, a NoSQL database in Azure. This allows unstructured data to be stored and queried, which is useful for Covid19 data which can be complex in nature.
5. Data Transformation: Power Query is used to perform data transformations and to clean the data stored in CosmosDB.
6. Data Visualization: Finally, the transformed data is visualized using Power BI, a Business Intelligence tool that helps create interactive dashboards and data visualizations. This allows users to view Covid19 data in real-time and perform in-depth analysis.
## Project stage
### Création du ressource group:
Here are the steps to create a resource group in the Azure portal:
1. Log in to the Azure portal.
2. Click the “Create Resource” button in the upper left corner of the portal home page.
3. In the “New Resource” window, search for “Resource Group” and select it from the search results.
4. Click the “Create” button to start creating a resource group.
5. In the "Create Resource Group" window, select your subscription and enter a unique name for the resource group.
6. Choose the region in which you want to host the resource group.
7. You can also add tags to organize your resources and make them easier to manage.
8. Click the “Check + Create” button to validate your settings and create the resource group.
9. Wait for the resource group to be created. You can follow the progress of the creation by clicking on the "Notifications" button at the top of the page.
![image](https://github.com/KhalidElKassimi/BI-Dashboard-for-COVID-19-Case-Analysis-in-the-United-States/assets/110225378/76ba484e-c497-4d75-83b6-efdb36aa5d9c)
### Creating an Event Hub account:
• Access the Azure portal (https://portal.azure.com/)
• Search for “Event Hubs” in the search bar and click on it
• Click on “Create”
• Fill in the necessary information: name, resource group, region, etc.
• Click on “Review + Create” to check the information entered
• Click on “Create” to create the EventHub account
![image](https://github.com/KhalidElKassimi/BI-Dashboard-for-COVID-19-Case-Analysis-in-the-United-States/assets/110225378/eea1cd0e-f03d-42f3-932f-cfc52a71ffab)
### Creating a Cosmos DB account:
• Access the Azure portal
• Search for “Azure Cosmos DB” in the search bar and click on it
• Click on “Create”
• Fill in the necessary information: name, resource group, region, etc.
• Select the NoSQL API.
![image](https://github.com/KhalidElKassimi/BI-Dashboard-for-COVID-19-Case-Analysis-in-the-United-States/assets/110225378/6eae803b-4da2-4eb0-9bcd-f3fe496ebf69)
• Click on “Review + Create” to check the information entered
• Click on “Create” to create the Cosmos DB account
• After creating the cosmos DB account, we proceed to create our container and our database
• We end up clicking on OK
![image](https://github.com/KhalidElKassimi/BI-Dashboard-for-COVID-19-Case-Analysis-in-the-United-States/assets/110225378/eb5d2b03-21cc-4cb0-be51-76f3e8cfb6ba)
![image](https://github.com/KhalidElKassimi/BI-Dashboard-for-COVID-19-Case-Analysis-in-the-United-States/assets/110225378/c21fc655-1386-45c6-b926-0c2b0d3bf0dd)
###Configuring Stream Analytics:
Access the eventhub account in the Azure portal and click on process data
![image](https://github.com/KhalidElKassimi/BI-Dashboard-for-COVID-19-Case-Analysis-in-the-United-States/assets/110225378/cfba7719-9c5c-434f-a568-e1ef9ef7a038)
Choisir ensuite Materialize data in cosmos db à l’aide de stream analytics
![image](https://github.com/KhalidElKassimi/BI-Dashboard-for-COVID-19-Case-Analysis-in-the-United-States/assets/110225378/ec23103f-fe89-4eaa-9ecb-4970b8b25b0b)
• Create a stream analytics instance
• Choose our event hub instance as input and our cosmos db database as output
![image](https://github.com/KhalidElKassimi/BI-Dashboard-for-COVID-19-Case-Analysis-in-the-United-States/assets/110225378/d9648ed3-4182-44a7-b0bd-6afecad29957)
To retrieve the data from the API, you must execute the script below:
![image](https://github.com/KhalidElKassimi/BI-Dashboard-for-COVID-19-Case-Analysis-in-the-United-States/assets/110225378/31945204-7262-4dac-8215-605422558669)
### Launch of streaming:
After creating the code, we launch the job stream analytics and the code above. We see that the data is transmitted to our cosmos db database in the form of JSON documents
![image](https://github.com/KhalidElKassimi/BI-Dashboard-for-COVID-19-Case-Analysis-in-the-United-States/assets/110225378/ff8f14bc-f40a-4b8d-ad89-a578c1e02b5c)
### Connect cosmosdb to power bi:
In Power BI Desktop, click "Home" in the navigation bar, then click "Get Data."
In the "Get Data" window, search for "Azure" in the search bar, select "Azure CosmosDB", then click "Connect".
![image](https://github.com/KhalidElKassimi/BI-Dashboard-for-COVID-19-Case-Analysis-in-the-United-States/assets/110225378/13fb59bd-7240-48d6-b426-88be70d69b58)
In the next window, enter your AzureCosmos DB account information, including Database URI, Database Name, and Credentials.
After entering the information, click "OK" to connect to the Cosmos DB database.
![image](https://github.com/KhalidElKassimi/BI-Dashboard-for-COVID-19-Case-Analysis-in-the-United-States/assets/110225378/0e1e7c04-75c5-445f-a35a-bb5e20b14bb3)
If you are successfully logged in, you will see a list of all collections available in your database.
![image](https://github.com/KhalidElKassimi/BI-Dashboard-for-COVID-19-Case-Analysis-in-the-United-States/assets/110225378/d5321ed6-f011-424e-9081-de23d3c0250f)
### ETL and Data Modeling (DATAWAREHOUSING):
After having retrieved the documents from your database, we begin to convert our database into tabular format by clicking on the red button:
![image](https://github.com/KhalidElKassimi/BI-Dashboard-for-COVID-19-Case-Analysis-in-the-United-States/assets/110225378/6e5e98ec-6ebf-4dc8-bd54-9838ee31b2b0)
Then we start cleaning the data by removing unwanted columns, converting the types of each column, replacing null values with 0, making negative values positive values.
Then we start to create our data warehouse by duplicating our database and recovering the desired data for each dimension. We save the modifications.
![image](https://github.com/KhalidElKassimi/BI-Dashboard-for-COVID-19-Case-Analysis-in-the-United-States/assets/110225378/878ef5d2-d04c-4dd1-8f91-c93b932b2016)
In our model we check if the dimension tables are well connected to the facts table.
![image](https://github.com/KhalidElKassimi/BI-Dashboard-for-COVID-19-Case-Analysis-in-the-United-States/assets/110225378/6e3eb2e1-598b-4531-804a-e3d8c0d4da18)
### Data visualization:
We begin to choose the desired graphs for data visualization, while adding the date and state filters.
And since it is an interactive Dashboard, if you select a state or a period, the Dashboard displays the appropriate data.
![image](https://github.com/KhalidElKassimi/BI-Dashboard-for-COVID-19-Case-Analysis-in-the-United-States/assets/110225378/dcc590a3-4560-430a-9a85-102ed6df937b)
![image](https://github.com/KhalidElKassimi/BI-Dashboard-for-COVID-19-Case-Analysis-in-the-United-States/assets/110225378/14a70f67-fa75-4c4e-b332-d149b5c7f13f)









