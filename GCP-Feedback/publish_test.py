from google.cloud import pubsub_v1
import json
from datetime import datetime, timezone
from flask import Flask, render_template, request, jsonify
import os

project_id = os.getenv("project_id")
topic_id = 'feedback-topic'

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_id)



app = Flask(__name__)

@app.route('/')
def home():
    return render_template("feedback_site.html")

@app.route('/submit_form', methods=['POST'])
def get_feedback():
    username = request.form.get('users_name')
    feedback = request.form.get('users_feedback')
    feedback_time = datetime.now(timezone.utc).isoformat()

    message_data = {
    'username' : username,
    'message' : feedback,
    'timestamp' : feedback_time
    }

    data = json.dumps(message_data).encode("utf-8")

    future = publisher.publish(topic_path, data)
    print(f'Sent out: {future.result()}')


    return jsonify({"status" : 'Message success!'})

if __name__ == '__main__':
    app.run(debug=True)