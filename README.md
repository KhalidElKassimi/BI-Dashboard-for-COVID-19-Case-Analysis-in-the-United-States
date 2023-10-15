# BI-Dashboard-for-COVID-19-Case-Analysis-in-the-United-States
## Introduction
COVID-19 has had a global impact, including in the United States. Dashboards have been created to monitor the pandemic and help decision-makers. Cosmos DB and Power BI are used to create a COVID-19 dashboard in the United States. Cosmos DB is ideal for storing data thanks to its scalability and availability. Data can be stored in JSON and organized into collections for easy management. Power BI is a popular tool for visualizing data and connecting to Cosmos DB to display interactive charts. Users can filter data by state or date. The dashboard can include graphs, maps and comparisons to show trends and forecasts based on historical data.
## Designs and tools
![image](https://github.com/KhalidElKassimi/BI-Dashboard-for-COVID-19-Case-Analysis-in-the-United-States/assets/110225378/138c430f-2bb1-4e5e-b2ab-a56fa37a3613)

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
![image](https://github.com/KhalidElKassimi/BI-Dashboard-for-COVID-19-Case-Analysis-in-the-United-States/assets/110225378/a32686cd-cced-43ab-ab65-af932cf5babf)
### Creating an Event Hub account:
• Access the Azure portal (https://portal.azure.com/)
• Search for “Event Hubs” in the search bar and click on it
• Click on “Create”
• Fill in the necessary information: name, resource group, region, etc.
• Click on “Review + Create” to check the information entered
• Click on “Create” to create the EventHub account
![image](https://github.com/KhalidElKassimi/BI-Dashboard-for-COVID-19-Case-Analysis-in-the-United-States/assets/110225378/79681bce-b218-4e50-b9cb-58deb4257183)

### Creating a Cosmos DB account:
• Access the Azure portal
• Search for “Azure Cosmos DB” in the search bar and click on it
• Click on “Create”
• Fill in the necessary information: name, resource group, region, etc.
• Select the NoSQL API.
![image](https://github.com/KhalidElKassimi/BI-Dashboard-for-COVID-19-Case-Analysis-in-the-United-States/assets/110225378/b3c9643c-4989-4001-b39f-c0b32234c9c1)

• Click on “Review + Create” to check the information entered
• Click on “Create” to create the Cosmos DB account
• After creating the cosmos DB account, we proceed to create our container and our database
• We end up clicking on OK
![image](https://github.com/KhalidElKassimi/BI-Dashboard-for-COVID-19-Case-Analysis-in-the-United-States/assets/110225378/d7e5f333-1a5b-4783-93da-05cd8a367798)

![image](https://github.com/KhalidElKassimi/BI-Dashboard-for-COVID-19-Case-Analysis-in-the-United-States/assets/110225378/2ad7bfe1-3f56-465a-a663-5bb92e672bbc)

###Configuring Stream Analytics:
Access the eventhub account in the Azure portal and click on process data
![image](https://github.com/KhalidElKassimi/BI-Dashboard-for-COVID-19-Case-Analysis-in-the-United-States/assets/110225378/d69b637b-ed72-4ab7-ac1a-6ece17fc5248)

Then choose Materialize data in cosmos db using stream analytics
![image](https://github.com/KhalidElKassimi/BI-Dashboard-for-COVID-19-Case-Analysis-in-the-United-States/assets/110225378/7d285d38-afa8-44ba-adc1-d6cb294a1275)

• Create a stream analytics instance
• Choose our event hub instance as input and our cosmos db database as output
![image](https://github.com/KhalidElKassimi/BI-Dashboard-for-COVID-19-Case-Analysis-in-the-United-States/assets/110225378/2683d79e-1e87-499e-8a28-1939db7213ba)

To retrieve the data from the API, you must execute the script below:
![image](https://github.com/KhalidElKassimi/BI-Dashboard-for-COVID-19-Case-Analysis-in-the-United-States/assets/110225378/31945204-7262-4dac-8215-605422558669)
### Launch of streaming:
After creating the code, we launch the job stream analytics and the code above. We see that the data is transmitted to our cosmos db database in the form of JSON documents
![image](https://github.com/KhalidElKassimi/BI-Dashboard-for-COVID-19-Case-Analysis-in-the-United-States/assets/110225378/b1941d55-7a8e-4432-beb8-5d52fbd67e63)

### Connect cosmosdb to power bi:
In Power BI Desktop, click "Home" in the navigation bar, then click "Get Data."
In the "Get Data" window, search for "Azure" in the search bar, select "Azure CosmosDB", then click "Connect".
![image](https://github.com/KhalidElKassimi/BI-Dashboard-for-COVID-19-Case-Analysis-in-the-United-States/assets/110225378/d3fa7ebe-62b0-4e29-afd5-a2306edbb1c0)

In the next window, enter your AzureCosmos DB account information, including Database URI, Database Name, and Credentials.
After entering the information, click "OK" to connect to the Cosmos DB database.
![image](https://github.com/KhalidElKassimi/BI-Dashboard-for-COVID-19-Case-Analysis-in-the-United-States/assets/110225378/59e7f233-14d9-4c66-a833-1d2740a0efb8)

If you are successfully logged in, you will see a list of all collections available in your database.
![image](https://github.com/KhalidElKassimi/BI-Dashboard-for-COVID-19-Case-Analysis-in-the-United-States/assets/110225378/7dba5ff1-5ea4-4736-ac8f-802c29b259c7)

### ETL and Data Modeling (DATAWAREHOUSING):
After having retrieved the documents from your database, we begin to convert our database into tabular format by clicking on the red button:
![image](https://github.com/KhalidElKassimi/BI-Dashboard-for-COVID-19-Case-Analysis-in-the-United-States/assets/110225378/3dc1c72c-afc7-4280-9634-b7fadc4192eb)

Then we start cleaning the data by removing unwanted columns, converting the types of each column, replacing null values with 0, making negative values positive values.
Then we start to create our data warehouse by duplicating our database and recovering the desired data for each dimension. We save the modifications.
![image](https://github.com/KhalidElKassimi/BI-Dashboard-for-COVID-19-Case-Analysis-in-the-United-States/assets/110225378/23d07235-5c4c-4dd4-a948-192a9929bd03)

In our model we check if the dimension tables are well connected to the facts table.
![image](https://github.com/KhalidElKassimi/BI-Dashboard-for-COVID-19-Case-Analysis-in-the-United-States/assets/110225378/4bb9d3dc-1764-476d-a7ef-f94f634d7a71)

### Data visualization:
We begin to choose the desired graphs for data visualization, while adding the date and state filters.
And since it is an interactive Dashboard, if you select a state or a period, the Dashboard displays the appropriate data.
![image](https://github.com/KhalidElKassimi/BI-Dashboard-for-COVID-19-Case-Analysis-in-the-United-States/assets/110225378/ef414d68-edd2-41d9-a64a-03dcb6e27d67)

![image](https://github.com/KhalidElKassimi/BI-Dashboard-for-COVID-19-Case-Analysis-in-the-United-States/assets/110225378/46ed43cc-7642-47f3-b520-a26da44814fa)










