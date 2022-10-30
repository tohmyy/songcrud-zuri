import requests

endpoint = "http://localhost:8000/api/musicapp/list/"

data = {
    'title':'You & I (Nobody in the World)',
    'date_released': '2014-06-10',
    'likes': '112967000',
    'artiste_id': 1,
    }

post_response = requests.post(endpoint, json=data)
print(post_response.json())