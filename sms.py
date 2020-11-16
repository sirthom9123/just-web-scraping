# Bulk SMS automation #
import requests
import json

# API url
url = 'https://api.bulksms.com/v1/messages' 
number = input('Enter cell number starting with country code, .i.e. +27...: ')
message = input('Enter your message...: ')

payload = {
    "to": number,
    "routingGroup": "ECONOMY",
    "encoding": "TEXT",
    "longMessageMaxParts": 99,
    "body": message,
    "userSuppliedId": "submission-12765",
    "protocolId": "IMPLICIT",
    "deliveryReports": "ALL"
}
headers = {
    'Authorization': 'Basic <KEY>', # Basic Authorization key provided on bulksms api. 
    'Content-Type': 'application/json'
}

# Post the message via a request method with your data.
response = requests.request('POST', url, headers=headers, data=json.dumps(payload))
print(response.text.encode('utf8')) 