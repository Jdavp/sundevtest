#!/usr/bin/python3
import requests, json

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}

YOUR_API_KEY = 'a856a7efd994fee16d3b269264f02185ececb554'

def getIssueDetail(api_id):
    #function to return detail issue info(image, characters, team, location)

    response = requests.get('https://comicvine.gamespot.com/api/issue/4000-'+ api_id +'/?api_key='+ YOUR_API_KEY +'&format=json', headers=headers)

    if response.status_code != 200:
        return { "comics_image":"",
            "list_character_ids":"",
            "list_team_ids":"",
            "list_location_ids":"",
            "list_of_concepts_ids":""
            }

    results = response.json()['results']

    comics_image = results['image']['original_url']

    lists_of_character_ids = []
    for i in range(len(results['character_credits'])):
        lists_of_character_ids.append(results['character_credits'][i]['id'])
    
    list_of_teams_ids = []
    for i in range(len(results['team_credits'])):
        list_of_teams_ids.append(results['team_credits'][i]['id'])

    list_of_location_ids = []
    for i in range(len(results['location_credits'])):
        list_of_location_ids.append(results['location_credits'][i]['id'])

    list_of_concepts_ids = []
    for i in range(len(results['concept_credits'])):
        list_of_concepts_ids.append(results['concept_credits'][i]['id'])   


    return { "comics_image":comics_image,
            "list_character_ids":lists_of_character_ids,
            "list_team_ids":list_of_teams_ids,
            "list_location_ids":list_of_location_ids,
            "list_of_concepts_ids":list_of_concepts_ids
            }
