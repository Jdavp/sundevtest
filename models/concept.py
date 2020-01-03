#!/usr/bin/python3
import requests, json

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}

YOUR_API_KEY = 'a856a7efd994fee16d3b269264f02185ececb554'

def getConceptDetail(concept_id):
    # function to return the info the image an name of a specific concepts

    response = requests.get("https://comicvine.gamespot.com/api/location/4060-"+ str(concept_id) +'/?api_key='+ YOUR_API_KEY +'&format=json', headers=headers)

    if response.status_code != 200:
        return {'image':"",
                'name':""
                }
    
    results = response.json()['results']

    concept_image = results['image']['icon_url']

    concept_name = results['name']
    
    return {'image':concept_image,
            'name ':concept_name
            }