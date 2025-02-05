import json
import requests


query_string = """
query {
    events(importance: 8) {  
        id
        name
        date
        importance
        user {
            userName : name
        }
    }
}
"""


payload = {"query": query_string}
url = "http://127.0.0.1:8000/graphql"
headers = {'Content-Type': 'application/json'}

try:
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    response.raise_for_status() 

    json_response = response.json()

    if "errors" in json_response:
        print("GraphQL Errors:", json_response["errors"])
    else:
        print("GraphQL Response (JSON):", json_response["data"])
        print("HTTP Status Code:", response.status_code)
        print("HTTP Headers:", response.headers)

except requests.exceptions.RequestException as e:
    print("Request failed:", e)
