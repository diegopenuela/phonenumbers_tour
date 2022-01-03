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


#ONE COUNTRY
#Get root object: AvailablePhoneNumber to access Subresource_uris
#available_phone_number_country = client.available_phone_numbers('MX').fetch()

#Get Subresource_uris - TOLLFREE
tollfree = client.available_phone_numbers('MX').toll_free.list()

#Understand the object
print("\n----LISTA----")
print(type(tollfree))
print(dir(tollfree))
print(len(tollfree))

#
print("\n----ATRIBUTOS----")
for record in tollfree:
    print(dir(record))
    break


print("\n----VALORES----")
for record in tollfree:
    print(vars(record))
    break

#Atributo
print("\n----DETALLE----")
attrs =[o._context for o in tollfree]
print(attrs)
