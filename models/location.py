#!/usr/bin/python3
import requests, json

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}

YOUR_API_KEY = 'a856a7efd994fee16d3b269264f02185ececb554'

def getLocationDetail(location_id):
    #function to return the image and name of a specific location
    
    response = requests.get("https://comicvine.gamespot.com/api/location/4020-"+ str(location_id) +'/?api_key='+ YOUR_API_KEY +'&format=json', headers=headers)

    if response.status_code != 200:
        return {'image':"",
                'name':""
                } 
    
    results = response.json()['results']

    location_image = results['image']['icon_url']

    location_name = results['name']
    
    return {'image':location_image,
            'name ':location_name
            }