import json
import requests


query_string_1 = """
query {
    events( date: "2025-05-10T16:00:00" ) {  
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
query_string_2 = """
query {
    users {
        userName : name
        email
        events(date: "2025-05-10T16:00:00"){
            id
            name
            date
            importance
        }
    }
}
"""


requests_list=[query_string_1, query_string_2]



for query in requests_list:
    payload = {"query": query}
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
    print("\nREQUEST FINISHED\n")
