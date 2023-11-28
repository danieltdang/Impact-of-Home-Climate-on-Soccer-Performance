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

    # first index is team # (0 or 1), second index is player #, third index is always 0, fourth index is always 0
    team = 0
    player = 4
    print(matchResponse["content"]["lineup"]["lineup"][team]["optaLineup"]["players"][player][0]["stats"][0]["stats"]["FotMob rating"]["value"])
Get_Matches()