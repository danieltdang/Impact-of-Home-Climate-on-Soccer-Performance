import requests
import pvcz
import json
import csv
import time
from datetime import datetime, timezone

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
        fieldnames = ['Koppen Climate', 'Home Team', 'Away Team', 'Home Avg Rating', 'Away Avg Rating']
        
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for i, match in enumerate(matchData):
            matchId = match["id"]
            matchUrl = f"https://www.fotmob.com/api/matchDetails?matchId={matchId}"
            matchResponse = json.loads(requests.request("GET", matchUrl, headers=headers, data=payload).text)

            stadium = matchResponse['content']['matchFacts']['infoBox']['Stadium']
            
            # Convert UTC time to standardized date format
            date = matchResponse["general"]["matchTimeUTC"]
            
            # Define the input format
            input_format = "%a, %b %d, %Y, %H:%M %Z"

            # Parse the UTC time string
            utc_time = datetime.strptime(date, input_format)

            # Convert to local time
            utc_time = utc_time.replace(tzinfo=timezone.utc)
            local_time = utc_time.astimezone()

            # Define the output format
            output_format = "%m/%d/%y"

            formatted_date = local_time.strftime(output_format)

            closest_index = pvcz.arg_closest_point(stadium['lat'], stadium['long'], df['lat'], df['lon'])
            location_data = df.iloc[closest_index]
            
            row_data = {
                'Koppen Climate': location_data['KG_zone'],
                'Home Team': matchResponse['content']['lineup']['lineup'][0]["teamName"],
                'Home Avg Rating': 0.0,
                'Away Team': matchResponse['content']['lineup']['lineup'][1]["teamName"],
                'Away Avg Rating': 0.0
            }

            for team in range(2):
                teamRating = 0.0
                playerCount = 11
                try:
                    for roles in matchResponse['content']['lineup']['lineup'][team]['players']:
                        for player in roles:
                            try:
                                teamRating += player['stats'][0]['stats']['FotMob rating']['value']
                                
                            except:
                                # in rare cases where a player has no rating (1 out of 10,758 so far), we try to get the less accurate rating
                                try:
                                    teamRating += float(player["rating"]["num"])
                                    
                                except Exception as e:
                                    errorCount += 1
                                    print(f"Match {i} [{matchId}] - Team {team + 1} Error finding player rating: {e}")
                                    continue
                    
                    #print(f"Match {i} [{matchId}] - Team {team + 1} Successfully written to file")

                except Exception as e:
                    errorCount += 1
                    print(f"Match {i} [{matchId}] - Team {team + 1} Error finding lineup: {e}")

            
                if team == 0: 
                    row_data['Home Avg Rating'] = round(teamRating / playerCount, 2)
                else:
                    row_data['Away Avg Rating'] = round(teamRating / playerCount, 2)

            writer.writerow(row_data)
            print(f"Match {i} [{matchId}] - Processing complete")
    
    print(f"Finished processing {matchCount} matches with {matchCount * 22} players and {errorCount} errors")