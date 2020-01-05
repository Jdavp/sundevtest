#!/usr/bin/python3
import requests, json


def getLocationDetail(location_id, YOUR_API_KEY, headers):
    #function to return the image and name of a specific location
    
    response = requests.get("https://comicvine.gamespot.com/api/location/4020-"+ str(location_id) +'/?api_key='+ YOUR_API_KEY +'&format=json', headers=headers)

    if response.json()['status_code'] != 200:
        return {'image':"",
                'name':""
                } 
    
    results = response.json()['results']

    location_image = results['image']['icon_url']

    location_name = results['name']
    
    return {'image':location_image,
            'name ':location_name
            }