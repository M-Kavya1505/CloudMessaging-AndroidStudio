import firebase_admin
from firebase_admin import credentials, messaging

# Initialize Firebase app with credentials
# Keep your generate private key file path in place of XYZ
cred = credentials.Certificate("./XYZ")
firebase_admin.initialize_app(cred)

def send_fcm_message_to_topic(topic, title, body):
    # Define a message to send to the topic
    message = messaging.Message(
        notification=messaging.Notification(
            title=title,
            body=body,
        ),
        topic=topic,
    )

    # Send the message
    response = messaging.send(message)
    print('Successfully sent message to topic', topic, ':', response)

if __name__ == '__main__':
    topic = 'tambola'  # Replace with your topic name
    title = 'Notification'
    body = 'Weather update'

    send_fcm_message_to_topic(topic, title, body)