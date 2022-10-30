import requests

endpoint = "http://localhost:8000/api/musicapp/list/"

data = {
    'title':'Alone',
    'date_released': '2014-06-10',
    'likes': '400000',
    'artiste_id': 2,
    }

post_response = requests.post(endpoint, json=data)
print(post_response.json())