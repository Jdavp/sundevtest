#!/usr/bin/python3
import requests, json

def getConceptDetail(concept_id, YOUR_API_KEY, headers):
    # function to return the info the image an name of a specific concepts

    response = requests.get("https://comicvine.gamespot.com/api/location/4060-"+ str(concept_id) +'/?api_key='+ YOUR_API_KEY +'&format=json', headers=headers)

    if response.json()['status_code'] != 1:
        return {'image':"",
                'name':""
                 }
    
    results = response.json()['results']

    concept_image = results['image']['icon_url']

    concept_name = results['name']
    
    return {'image':concept_image,
            'name':concept_name
            }