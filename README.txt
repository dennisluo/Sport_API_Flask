README
Sport_API_Flask
Integration of sport result API data

Created by: Dennis Luo HSBC

Implemented in Flask

Requirements + Packages:
Python/Flask/Requests/Json

Design:
Flask API is structured using Flask Blueprint

EXECUTION:
Project is simply executed using run.py

User can switch between development/production environment using env file

BPL and NBA results are returned using Flask Restful endpoints on localhost
Results are returned 40 at a time

BPL endpoint
http://127.0.0.1:5000/sport_api/v1/bpl

NBA endpoint
http://127.0.0.1:5000/sport_api/v1/nba

BONUS:
Pagination enabled so user can query for specific page required (40 results per page)

User can query results for specified date if it exists on that current page else return empty list
(Date format YYYY-MM-DD)

example ~ Get match results in BPL on page 2 which has date (YYYY-MM_DD)
http://127.0.0.1:5000/sport_api/v1/bpl?page=2&date=YYYY-MM-DD

Additional main endpoint has been added to return all data for both BPL & NBA dataset
No result limits added (http://127.0.0.1:5000/)

Future APIs:
User can add additional api to api_call function and define new endpoint function for that new api

Assumptions:
(Webapp uses pagination feature from nba api for nba pagination
As no pagination is provided by bpl results I have made my own pagination call)


Future Developments/Releases:
Host project on Heroku
Change implementation to GraphQL
More additional/efficient tests