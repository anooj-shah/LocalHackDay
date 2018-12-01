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
    feelings_response = request.args.get('Body')
    append_message(feelings_response)
    # Add a message
    resp.message("Thank's for sharing with feelr :)")

    return str(resp)

@app.route("/message/<message>", methods=['GET','POST'])
def ios_message(message):
    remove_format = str(message)
    remove_format = remove_format.replace("_"," ")
    append_message(remove_format)
    return remove_format

def append_message(message):
    with open('feelings.csv', 'a', newline='\n') as csvfile:
        feeling_writer = csv.writer(csvfile, delimiter='�')
        feeling_writer.writerow([datetime.now()] + [message])

if __name__ == "__main__":
    app.run(debug=True)
