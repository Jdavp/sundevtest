#!/usr/bin/python3
import requests, datetime, json

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}

YOUR_API_KEY = 'a856a7efd994fee16d3b269264f02185ececb554'

def getCharacterDetail(character_id):
    #function to return the image info of a character
    response = requests.get('https://comicvine.gamespot.com/api/character/4005-'+ str(character_id) +'/?api_key='+ YOUR_API_KEY +'&format=json', headers=headers)
    print(response)
    if response.status_code != "200":
        return {'image':"",
                'name':""
                }

    results = response.json()['results']

    character_image = results['image']['icon_url']

    character_name = results['name']
    
    
    return {'image':character_image,
            'name ':character_name
            }
