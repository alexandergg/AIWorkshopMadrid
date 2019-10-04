import requests


input_data = "{\"data\": [230.1,37.8,69.2]}"

headers = {'Content-Type': 'application/json'}
resp = requests.post('http://8542afd2-4a12-47da-9e1e-a81cda14c3a2.eastus.azurecontainer.io/score', input_data, headers=headers)
print("prediction:", resp.text)