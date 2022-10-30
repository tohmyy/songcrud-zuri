import requests

print("Search database by song Id")

find_id = input("Enter Song Id: ")

find_id = int(find_id)

endpoint = f"http://localhost:8000/api/musicapp/{find_id}/find_song/"

get_response = requests.get(endpoint)
print(get_response.json())