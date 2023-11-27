import requests
import json

def Get_Matches():
    url = "https://www.fotmob.com/api/leagues?id=130&ccode3=USA_FL&season=2022"

    payload = {}
    headers = {}

    response = json.loads(requests.request("GET", url, headers=headers, data=payload).text)

    # print(response["matches"]["allMatches"][0])

    matchId = response["matches"]["allMatches"][0]["id"]
    matchUrl = f"https://www.fotmob.com/api/matchDetails?matchId={matchId}"
    matchResponse = json.loads(requests.request("GET", matchUrl, headers=headers, data=payload).text)

    print(matchResponse)
Get_Matches()