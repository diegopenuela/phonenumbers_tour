import os
from twilio.rest import Client
import config


account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

# Subresource_uris
# AvailablePhoneNumberLocal
# AvailablePhoneNumberTollFree
# AvailablePhoneNumberMobile


#Capabilities
# Voice, SMS, MMS


#ONE COUNTRY
#Get root object: AvailablePhoneNumber to access Subresource_uris
#available_phone_number_country = client.available_phone_numbers('MX').fetch()

#Get Subresource_uris - LOCAL
local = client.available_phone_numbers('MX').local.list()

#Understand the object
print("\n----LISTA----")
print(type(local))
print(dir(local))
print(len(local))

#
print("\n----ATRIBUTOS----")
for record in local:
    print(dir(record))
    break


print("\n----VALORES----")
for record in local:
    print(vars(record))
    break

#Atributo
print("\n----DETALLE----")
attrs =[o._context for o in local]
print(attrs)