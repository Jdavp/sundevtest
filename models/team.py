#!/usr/bin/python3
import requests, datetime, json

def getTeamDetail(team_id, YOUR_API_KEY, headers):
    #function to return the image an name of an specific team

    response = requests.get( "https://comicvine.gamespot.com/api/team/4060-"+ str(team_id) +'/?api_key='+ YOUR_API_KEY +'&format=json', headers=headers)

    if response.json()['status_code'] != 1:
        return {'image':"",
                'name':""
                 }

    results = response.json()['results']

    teams_image = results['image']['icon_url']

    teams_name = results['name']


    return {'image':teams_image,
            'name':teams_name
            }