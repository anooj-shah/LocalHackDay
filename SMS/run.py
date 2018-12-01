from flask import Flask, request
import csv
from datetime import datetime
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_ahoy_reply():
    """Respond to incoming messages with a friendly SMS."""
    # Start our response
    resp = MessagingResponse()
    message = request.args.get('Body')
    #date = request.args.get("time")

    with open('feelings.csv', 'a', newline='\n') as csvfile:
        feeling_writer = csv.writer(csvfile, delimiter=',')
        feeling_writer.writerow([datetime.now()] + [message])

    print("Added to CSV!")


    # Add a message
    resp.message("Thank's for sharing with feelr :)")

    return str(resp)

@app.route("/message", methods=['GET','POST'])
def ios_message():
    return str("Works!")

if __name__ == "__main__":
    app.run(debug=True)
