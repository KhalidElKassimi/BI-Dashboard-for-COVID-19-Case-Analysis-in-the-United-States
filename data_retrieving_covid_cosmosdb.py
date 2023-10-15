import requests
import json
from azure.eventhub import EventHubProducerClient, EventData

# API endpoint
url = "https://api.covidtracking.com/v1/states/daily.json"

# Event Hub connection string and name
conn_str = "Endpoint=sb://coviddataeventhub.servicebus.windows.net/;SharedAccessKeyName=covid;SharedAccessKey=DxhenLXwcERbflDTQbM2xSOeCab13cJrd+AEhOyWq60=;EntityPath=coviddataeventhub"

# Retrieve data from API
response = requests.get(url)
data = json.loads(response.content)

# Create an Event Hub producer client
producer = EventHubProducerClient.from_connection_string(conn_str)

# Send data to Event Hub
for record in data:
    event_data_batch = producer.create_batch()
    event_data_batch.add(EventData(json.dumps(record)))
    producer.send_batch(event_data_batch)

# Close the producer
producer.close()
