import os
from prometheus_client import start_http_server, Gauge
import requests
import time

# Initialize Prometheus gauge metric
SELENIUM_GRID_SESSION_QUEUE_SIZE = Gauge('selenium_grid_session_queue_size', 'Number of sessions in queue')

# Function to fetch sessionQueueSize
def fetch_session_queue_size():
    grid_ip = os.environ.get("GRID_IP", "localhost")  # Default to your hardcoded IP if not set
    grid_port = os.environ.get("GRID_PORT", "32000")
    url = f"http://{grid_ip}:{grid_port}/graphql"
    query = {
        "query": "query Summary { grid { sessionQueueSize } }"
    }
    response = requests.post(url, json=query)
    data = response.json()
    sessionQueueSize = data['data']['grid']['sessionQueueSize']
    return sessionQueueSize

if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8000)
    
    while True:
        sessionQueueSize = fetch_session_queue_size()
        print(f"Fetched sessionQueueSize: {sessionQueueSize}")
        
        # Set the Prometheus gauge
        SELENIUM_GRID_SESSION_QUEUE_SIZE.set(sessionQueueSize)
        
        # Sleep for a bit before fetching the metric again
        time.sleep(10)
