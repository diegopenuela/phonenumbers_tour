import os
from twilio.rest import Client
import config


account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)



#incoming_phone_number = client.incoming_phone_numbers \
#                              .create(phone_number='+573162697465')

print("\n---- ACTIVE PN----")
incoming_phone_numbers = client.incoming_phone_numbers.list()
for record in incoming_phone_numbers:
    print(record.sid)

print("\n----DETAILS ACTIVE PN----")
incoming_phone_number = client \
    .incoming_phone_numbers('PN1c05ad7504b1b914e9b006dd23b1ec48') \
    .fetch()
print(vars(incoming_phone_number))

print(incoming_phone_number.address_sid)
print(incoming_phone_number.bundle_sid)