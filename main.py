from statsbombpy import sb
import pandas as pd

# Get the list of competitions
competitions = sb.competitions()

# Filter the competitions by season 2019/2020
seasons = []
for competition in competitions:
    print(competition)
    """if competition['season_name'] == '2019/2020':
        seasons.append(competition)"""

for season in seasons:
    print(season)
# Get the list of matches for each competition and season
matches = []
"""for comp_id, season_id in zip(seasons.competition_id, seasons.season_id):
    matches.append(sb.matches(competition_id=comp_id, season_id=season_id))

# Concatenate the matches into a single dataframe
matches = pd.concat(matches, ignore_index=True)"""

# Print the number of matches and the first matches rows
print(f"There are {len(matches)} matches in season 2019/2020.")
print(matches[:5])
