import requests
import json

def Get_Matches():
    url = 'https://www.fotmob.com/api/leagues?id=130&ccode3=USA_FL&season=2022'

    payload = {}
    headers = {}

    response = json.loads(requests.request("GET", url, headers=headers, data=payload).text)

    # print(response["matches"]["allMatches"][0])

    matchId = response["matches"]["allMatches"][0]["id"]
    
    matchUrl = f"https://www.fotmob.com/api/matchDetails?matchId={matchId}"
    matchResponse = json.loads(requests.request("GET", matchUrl, headers=headers, data=payload).text)
    
    # Dictionary with keys: name, city, country, lat, long
    stadium = matchResponse['content']['matchFacts']['infoBox']['Stadium']
    
    # Prints match ID and stadium info
    print(f"Match ID: {matchId}")
    print(f"{stadium['name']}: {stadium['city']}, {stadium['country']} ({stadium['lat']}, {stadium['long']})")
    
    # Loops through both teams
    for team in range(2):
        teamName = matchResponse['content']['lineup']['lineup'][team]['teamName']
        print(teamName)
        
        # Loops through players on each team
        for player in matchResponse['content']['lineup']['lineup'][team]['optaLineup']['players']:
            playerName = player[0]['name']['fullName']
            playerRating = player[0]['stats'][0]['stats']['FotMob rating']['value']
            print(f"\t{playerName}: {playerRating}")
    
Get_Matches()