import os
from google.cloud import pubsub_v1
import json
import psycopg2
import time
from datetime import datetime

project_id = os.getenv("project_id")
subscription_id = 'feedback-topic-sub'

db_config = {
    'host' : os.getenv('gcp_postgre_ip'),
    'dbname' : 'feedback_db',
    'user' : 'postgres',
    'password' : os.getenv('gcp_postgre_pass'),
    'port' : 5432
}

subscriber = pubsub_v1.SubscriberClient()
subscription_path = subscriber.subscription_path(project_id, subscription_id)

def callback(message):
    try:
        decoded = json.loads(message.data.decode('utf-8'))
        username = decoded['username']
        feedback = decoded['message']
        timestamp = decoded['timestamp']

        clean_timestamp = datetime.fromisoformat(timestamp.replace("Z","").replace("T:", "T"))


        conn = psycopg2.connect(**db_config)
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO feedback (username, message, timestamp)
                    VALUES (%s, %s, %s)
                    """, (username, feedback, clean_timestamp))
        
        conn.commit()

        cursor.execute("SELECT * FROM feedback")
        rows = cursor.fetchall()
        print(f'postgres data: {rows}')
        
        cursor.close()
        conn.close()

        print("Feedback stored in the postgres db!")
        message.ack()

    except Exception as e:
        print(f'Failed to insert feedback to db. {e}')
        message.nack()
    
subscriber.subscribe(subscription_path, callback=callback)
print(f'Listening for messages on: {subscription_path}')

while True:
    time.sleep(30)