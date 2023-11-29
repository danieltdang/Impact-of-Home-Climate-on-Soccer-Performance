import requests
import pvcz
import json
import csv
import time

TEAM_ROLES = ['Keeper', 'Defender', 'Midfielder', 'Attacker']

def Get_Matches():
    df = pvcz.get_pvcz_data()
    
    url = 'https://www.fotmob.com/api/leagues?id=130&ccode3=USA_FL&season=2022'
    payload = {}
    headers = {}

    matchData = json.loads(requests.request("GET", url, headers=headers, data=payload).text)["matches"]["allMatches"]

    # Stored counts for printing after finished processing all matches
    matchCount, errorCount = len(matchData), 0
    
    print(f"Processing {matchCount} matches...")
    with open('matches.csv', 'w', newline='', encoding='utf-8') as file:
        fieldnames = ['Match ID', 'Date', 'Stadium', 'City', 'Country', 'Latitude', 'Longitude', 'Koppen Climate', 'Team 1', 'Team 2', 'HomeTeam Avg Rating', 'AwayTeam Avg Rating']
        for role in TEAM_ROLES:
            fieldnames.append(f'HomeTeam {role} Avg Rating')
        
        for role in TEAM_ROLES:
            fieldnames.append(f'AwayTeam {role} Avg Rating')
        
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for i, match in enumerate(matchData):
            matchId = match["id"]
            matchUrl = f"https://www.fotmob.com/api/matchDetails?matchId={matchId}"
            matchResponse = json.loads(requests.request("GET", matchUrl, headers=headers, data=payload).text)

            stadium = matchResponse['content']['matchFacts']['infoBox']['Stadium']
            date = matchResponse["general"]["matchTimeUTC"]

            closest_index = pvcz.arg_closest_point(stadium['lat'], stadium['long'], df['lat'], df['lon'])
            location_data = df.iloc[closest_index]
            
            row_data = {
                'Match ID': matchId,
                'Date': date,
                'Stadium': stadium['name'],
                'City': stadium['city'],
                'Country': stadium['country'],
                'Latitude': stadium['lat'],
                'Longitude': stadium['long'],
                'Koppen Climate': location_data['KG_zone'],
                'Team 1': matchResponse['content']['lineup']['lineup'][0]["teamName"],
                'Team 2': matchResponse['content']['lineup']['lineup'][1]["teamName"]
            }

            for team in range(2):
                playerRating = [0,0,0,0]
                playerCount = [0,0,0,0]
                try:
                    for roles in matchResponse['content']['lineup']['lineup'][team]['players']:
                        for player in roles:

                            try:
                                if player["position"] == 'Keeper':
                                    playerRating[0] += player['stats'][0]['stats']['FotMob rating']['value']
                                    playerCount[0] += 1
                                elif player["position"] == 'Defender':
                                    playerRating[1] += player['stats'][0]['stats']['FotMob rating']['value']
                                    playerCount[1] += 1
                                elif player["position"] == 'Midfielder':
                                    playerRating[2] += player['stats'][0]['stats']['FotMob rating']['value']
                                    playerCount[2] += 1
                                elif player["position"] == 'Attacker':
                                    playerRating[3] += player['stats'][0]['stats']['FotMob rating']['value']
                                    playerCount[3] += 1 
                                
                            except Exception as e:
                                errorCount += 1
                                print(f"Match {i} [{matchId}] - Team {team + 1} Error finding player rating: {e}")
                                continue
                    
                    #print(f"Match {i} [{matchId}] - Team {team + 1} Successfully written to file")

                except Exception as e:
                    errorCount += 1
                    print(f"Match {i} [{matchId}] - Team {team + 1} Error finding lineup: {e}")

                for i in range(0, 4):
                    if team == 0: 
                        row_data[f'HomeTeam {TEAM_ROLES[i]} Avg Rating'] = round(playerRating[i] / playerCount[i],2)
                    else:
                        row_data[f'AwayTeam {TEAM_ROLES[i]} Avg Rating'] = round(playerRating[i] / playerCount[i],2)

            writer.writerow(row_data)
            print(f"Match {i} [{matchId}] - Successfully written to file")
    
    print(f"Finished processing {matchCount} matches with {matchCount * 22} players and {errorCount} errors")

Get_Matches()