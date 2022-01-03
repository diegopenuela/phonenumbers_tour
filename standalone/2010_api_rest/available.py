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


def debug_countries(available_phone_numbers):
    available_countries = list()
    for record in available_phone_numbers:
        available_countries.append(tuple((record.country,len(record.subresource_uris))))

    available_countries.sort()
    print("\n---- Lista de Países y Subresource_uris-----")
    print(available_countries)


#Returns: List Objects
available_phone_numbers = client.available_phone_numbers.list()
print(f"Total países: {len(available_phone_numbers)}")
debug_countries(available_phone_numbers)

#ONE COUNTRY
#Get root object: AvailablePhoneNumber to access Subresource_uris
print("\n---- One Country -----")
available_phone_number_country = client.available_phone_numbers('AU').fetch()
print(vars(available_phone_number_country))
