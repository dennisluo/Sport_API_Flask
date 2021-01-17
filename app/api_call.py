import requests
import json


# Calls APIs and merges into single dataset
def api_call(page=''):
    # Gather specific page if parameter
    pagination = '&page=' + str(page) if page != '' else ''

    # Retrieve basketball game data from api and store as json dict
    req1 = requests.get('https://www.balldontlie.io/api/v1/games?per_page=40' + pagination)
    nba_games = json.loads(req1.content)

    # Retrieve football game data from api and store as json dict
    req2 = requests.get('https://api.football-data.org/v2/competitions/PL/matches',
                        headers={'X-Auth-Token': '1a78569f128144ceb68faad10fab0cd6'})
    bpl_games = json.loads(req2.content)

    # Combine data to single dataset
    games = {'nba_games': nba_games['data'], 'bpl_games': bpl_games['matches']}

    return games


if __name__ == '__main__':
    print(api_call())
