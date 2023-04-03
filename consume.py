import urllib.request
import json
import os
import ssl

def allowSelfSignedHttps(allowed):
    # bypass the server certificate verification on client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context

allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.

# Request data goes here
# The example below assumes JSON formatting which may be updated
# depending on the format your endpoint expects.
# More information can be found here:
# https://docs.microsoft.com/azure/machine-learning/how-to-deploy-advanced-entry-script
data =  {
  "Inputs": {
    "data": [
      {
        "age": 59,
        "job": "retired",
        "marital": "married",
        "education": "basic.9y",
        "default": "unknown",
        "housing": "no",
        "loan": "no",
        "contact": "cellular",
        "month": "jul",
        "day_of_week": "fri",
        "duration": 1330,
        "campaign": 3,
        "pdays": 999,
        "previous": 0,
        "poutcome": "nonexistent",
        "emp.var.rate": 1.4,
        "cons.price.idx": 93.918,
        "cons.conf.idx": -42.7,
        "euribor3m": 4.962,
        "nr.employed": 5228.1
      }
    ]
  },
  "GlobalParameters": {
    "method": "predict"
  }
}

body = str.encode(json.dumps(data))

url = 'http://e4c0265f-a61a-4575-884a-631b364fbe6d.eastus.azurecontainer.io/score'
# Replace this with the primary/secondary key or AMLToken for the endpoint
api_key = 'zzXg2zrnv5ux2psjN82DaHIKuT9hWRK3'
if not api_key:
    raise Exception("A key should be provided to invoke the endpoint")


headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)

    result = response.read()
    print(result)
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(error.read().decode("utf8", 'ignore'))