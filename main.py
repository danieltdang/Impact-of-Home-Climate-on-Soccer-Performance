import requests
import json
import csv
import time

def Get_Matches():
    url = 'https://www.fotmob.com/api/leagues?id=130&ccode3=USA_FL&season=2022'
    payload = {}
    headers = {}

    matchData = json.loads(requests.request("GET", url, headers=headers, data=payload).text)["matches"]["allMatches"]

    with open('matches.csv', 'w', newline='', encoding='utf-8') as file:
        fieldnames = ['Match ID', 'Date', 'Stadium', 'City', 'Country', 'Latitude', 'Longitude']
        for i in range(1, 23):
            fieldnames.extend([f'Player{i} Rating'])
        
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for match in matchData:
            matchId = match["id"]
            matchUrl = f"https://www.fotmob.com/api/matchDetails?matchId={matchId}"
            matchResponse = json.loads(requests.request("GET", matchUrl, headers=headers, data=payload).text)

            stadium = matchResponse['content']['matchFacts']['infoBox']['Stadium']
            date = matchResponse["general"]["matchTimeUTC"]

            row_data = {
                'Match ID': matchId,
                'Date': date,
                'Stadium': stadium['name'],
                'City': stadium['city'],
                'Country': stadium['country'],
                'Latitude': stadium['lat'],
                'Longitude': stadium['long']
            }

            player_count = 1
            for team in range(2):
                teamName = matchResponse['content']['lineup']['lineup'][team]['teamName']

                try:
                    for player in matchResponse['content']['lineup']['lineup'][team]['optaLineup']['players']:
                        for obj in player:
                            playerRating = obj["rating"]["num"]

                            row_data[f'Player{player_count} Rating'] = playerRating

                            player_count += 1
                            if player_count > 22:
                                break

                except Exception as e:
                    print(f"Error finding lineup")

            writer.writerow(row_data)

            time.sleep(2.5)

Get_Matches()