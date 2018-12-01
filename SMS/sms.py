from twilio.rest import Client

account_sid = "AC745b080b3512355a2c7ea0378137338a"
auth_token = "0961877d3f9df59fd2af95557a567837"
client = Client(account_sid,auth_token)


body_text = "test!"
from_number = "+18172706314"
to_number = "+18177262720"


message = client.messages.create(body = body_text, from_ = from_number, to = to_number)

print(message.sid)
