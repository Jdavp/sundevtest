#!/usr/bin/python3
import requests, datetime, json

def getCharacterDetail(character_id, YOUR_API_KEY, headers):
    #function to return the image info of a character
    response = requests.get('https://comicvine.gamespot.com/api/character/4005-'+ str(character_id) +'/?api_key='+ YOUR_API_KEY +'&format=json', headers=headers)
    print(response)
    if response.json()['status_code'] != 200:
        return {'image':"",
                'name':""
                }

    results = response.json()['results']

    character_image = results['image']['icon_url']

    character_name = results['name']
    
    
    return {'image':character_image,
            'name ':character_name
            }
