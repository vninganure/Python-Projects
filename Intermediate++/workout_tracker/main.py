import requests

APP_ID = "f8b226f4"
API_KEY = "fb922c8a4d1198d7b8fc7fd268ba1393"
API_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

api_param ={
    "query": input("what was your todays activity:"),
    "gender":"male",
    "weight_kg":68,
    "height_cm":179,
    "age":24
}
response = requests.post(url=API_ENDPOINT, json=api_param, headers=headers)
print(response.json())
