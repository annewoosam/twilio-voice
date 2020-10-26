import os
from twilio.rest import Client

account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]

client = Client(account_sid, auth_token)

call=client.calls.create(
to="+19254781531",
from_=os.environ["TWILIO_SMS_FROM"],
twiml='<Response><Say>Howdy, Anne!"</Say></Response>',
url="http://demo.twilio.com/docs/voice.xml"
)
print(call.sid)
