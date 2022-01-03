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
mobile = client.available_phone_numbers('AU').mobile.list()

#Understand the object
print("\n----LIST----")
print(type(mobile))
print(dir(mobile))
print(len(mobile))

#
print("\n----PROPERTIES----")
for record in mobile:
    print(dir(record))
    break


print("\n----VALUES----")
for record in mobile:
    print(vars(record))
    break

#Atributo
print("\n----DETAILS----")
attrs =[o.beta for o in mobile]
print(attrs)

#Get Subresource_uris
print("\n----CUSTOM SEARCH----")

custom_search = client.available_phone_numbers('AU').mobile \
                                                    .list(
                                                        contains='43',
                                                        sms_enabled=True,
                                                        voice_enabled=False
                                                        ) 

result =[item.phone_number for item in custom_search]
print(result)