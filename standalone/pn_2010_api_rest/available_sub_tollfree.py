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
print("\n----LIST----")
print(type(tollfree))
print(dir(tollfree))
print(len(tollfree))

#
print("\n----PROPERTIES----")
for record in tollfree:
    print(dir(record))
    break


print("\n----VALUES----")
for record in tollfree:
    print(vars(record))
    break

#Atributo
print("\n----DETAILS----")
attrs =[o.phone_number for o in tollfree]
print(attrs)

#Get Subresource_uris
print("\n----CUSTOM SEARCH----")

custom_search = client.available_phone_numbers('MX').toll_free \
                                                    .list(
                                                        contains='2731',
                                                        sms_enabled=False,
                                                        voice_enabled=True
                                                        ) 

result =[item.phone_number for item in custom_search]
print(result)