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

    # variables for the match
    team = 0
    player = 4
    
    # Dictionary with keys: name, city, country, lat, long
    stadium = matchResponse["content"]["matchFacts"]["infoBox"]["Stadium"]
    teamName = matchResponse["content"]["lineup"]["lineup"][team]["teamName"]
    
    # keep the indices 0 and 0 at the end for player name and rating
    playerName = matchResponse["content"]["lineup"]["lineup"][team]["optaLineup"]["players"][player][0]["name"]["fullName"]
    playerRating = matchResponse["content"]["lineup"]["lineup"][team]["optaLineup"]["players"][player][0]["stats"][0]["stats"]["FotMob rating"]["value"]
    
    print(f"Match ID: {matchId}")
    print(f"{stadium['name']}: {stadium['city']}, {stadium['country']} ({stadium['lat']}, {stadium['long']})")
    print(f"{teamName} - {playerName}:  {playerRating}")
    
Get_Matches()