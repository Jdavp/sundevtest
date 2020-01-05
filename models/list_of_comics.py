#!/usr/bin/python3
import requests, datetime, json

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}

def getListofComicsInfo(YOUR_API_KEY, headers):
    # get comics basic info (picture,name,date)

    response = requests.get("https://comicvine.gamespot.com/api/issues/?api_key="+ YOUR_API_KEY +"&sort=date_added:desc&format=json", headers=headers)
    results = response.json()['results']

    list_of_comics = []

    for comics in range(len(results)):
        comic_image = results[comics]['image'].get('original_url')
        date_form = datetime.datetime.strptime(results[comics]['date_added'], '%Y-%m-%d %H:%M:%S')
        date = datetime.datetime.strftime(date_form,'%B %d, %Y')
        name_in_image = str(results[comics]['name'])
        issue_number = str(results[comics]['issue_number'])
        volume_name = str(results[comics]['volume'].get('name'))
        name = str(volume_name + name_in_image + " # " +issue_number)
        api_id = results[comics]['id']
        comic_info = {
            "comic_image":comic_image,
            "date": date,
            "name": name,
            "api_id":api_id
        }
        
        list_of_comics.append(comic_info)
    
    return list_of_comics