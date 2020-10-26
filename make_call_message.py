#added import os

import os

from urllib.parse import urlencode

# Import the Twilio Python Client.\ changed from TwilioRestClient to Client
from twilio.rest import Client

# Set your account ID and authentication token.
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

# The number of the phone initiating the call.
# This should either be a Twilio number or a number that you've verified
from_number = os.environ['TWILIO_SMS_FROM']

# The number of the phone receiving call.
to_number = "+19254781531"

# Use the Twilio-provided site for the TwiML response.
url = "https://twimlets.com/message?"

# The phone message text.
message = "Today is a great day."

# Initialize the Twilio client. # Similiarly updated TwilioRestClient to just Client
client = Client(account_sid, auth_token)

# Make the call.
call = client.calls.create(to=to_number,
                           from_=from_number,
                           url=url + urlencode({'Message': message}))
print(call.sid)
