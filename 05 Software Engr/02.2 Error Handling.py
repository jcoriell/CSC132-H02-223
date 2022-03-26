
import requests # pip install requests

try:
    response = requests.get("https://pokeapi.co/api/v2/pokemon/")   # an HTTP GET request
    if not response:
        raise Exception
    
    data = response.json()

    for item in data["results"]:
        print(item)

except:
    print("An error occurred")