import requests
import json

# URL for the web service, should be similar to:
# 'http://8530a665-66f3-49c8-a953-b82a2d312917.eastus.azurecontainer.io/score'
scoring_uri = "http://e4c0265f-a61a-4575-884a-631b364fbe6d.eastus.azurecontainer.io/score"

# If the service is authenticated, set the key or token
key = "zzXg2zrnv5ux2psjN82DaHIKuT9hWRK3"

# Two sets of data to score, so we get two results back
data =  {
  "Inputs": {
    "data": [
      {
        "age": 42,
        "job": "doctor",
        "marital": "married",
        "education": "university.degree",
        "default": "no",
        "housing": "yes",
        "loan": "yes",
        "contact": "cellular",
        "month": "jul",
        "day_of_week": "fri",
        "duration": 112,
        "campaign": 3,
        "pdays": 999,
        "previous": 0,
        "poutcome": "success",
        "emp.var.rate": 1.4,
        "cons.price.idx": 93.3,
        "cons.conf.idx": -40,
        "euribor3m": 3.4,
        "nr.employed": 5000
      }
    ]
  },
  "GlobalParameters": {
    "method": "predict"
  }
}

# Convert to JSON string
input_data = json.dumps(data)
with open("data.json", "w") as _f:
    _f.write(input_data)

# Set the content type
headers = {"Content-Type": "application/json"}
# If authentication is enabled, set the authorization header
headers["Authorization"] = f"Bearer {key}"

# Make the request and display the response
resp = requests.post(scoring_uri, input_data, headers=headers)
print(resp.json())
