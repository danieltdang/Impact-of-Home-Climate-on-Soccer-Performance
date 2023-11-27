import requests
import json

def Get_Matches():
    url = "https://www.fotmob.com/api/leagues?id=130&ccode3=USA_FL&season=2022"

    payload = {}
    headers = {}

    response = json.loads(requests.request("GET", url, headers=headers, data=payload).text)

    print(response["matches"]["allMatches"][0])


Get_Matches()