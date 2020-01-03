#!/usr/bin/python3
import requests, datetime, json

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}

YOUR_API_KEY = 'a856a7efd994fee16d3b269264f02185ececb554'

def getTeamDetail(team_id):
    #function to return the image an name of an specific team

    response = requests.get( "https://comicvine.gamespot.com/api/team/4060-"+ str(team_id) +'/?api_key='+ YOUR_API_KEY +'&format=json', headers=headers)

    if response.status_code != 200:
        return {'image':"",
                'name':""
                }

    results = response.json()['results']

    teams_image = results['image']['icon_url']

    teams_name = results['name']


    return {'image':teams_image,
            'name ':teams_name
            }