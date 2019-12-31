#!/usr/bin/python3
import requests, datetime, json
import os

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}

YOUR_API_KEY = str(os.environ.get('YOUR_API_KEY'))

api_url = "https://comicvine.gamespot.com/api/issue/4000-6/"

def getListofComicsInfo():
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
        api_url = results[comics]['api_detail_url']
        comic_info = {
            "comic_image":comic_image,
            "date": date,
            "name": name,
            "api_url":api_url
        }
        
        list_of_comics.append(comic_info)
    
    return list_of_comics


def getIssueDetail(api_url):
    #function to return detail issue info(image, characters, team, location)

    response = requests.get(api_url +'?api_key='+ YOUR_API_KEY +'&format=json', headers=headers)

    results = response.json()['results']

    comics_image = results['image'].get('original_url')

    lists_of_character_urls = []
    for i in range(len(results['character_credits'])):
        lists_of_character_urls.append(results['character_credits'][i]['api_detail_url'])
    
    list_of_teams_urls = []
    for i in range(len(results['team_credits'])):
        list_of_teams_urls.append(results['team_credits'][i]['api_detail_url'])

    list_of_location_urls = []
    for i in range(len(results['location_credits'])):
        list_of_location_urls.append(results['location_credits'][i]['api_detail_url'])

    list_of_concepts_urls = []
    for i in range(len(results['concept_credits'])):
        list_of_concepts_urls.append(results['concept_credits'][i]['api_detail_url'])   


    return { "comics_image":comics_image,
            "list_character_credits":lists_of_character_urls,
            "list_team_credits":list_of_teams_urls,
            "list_location_credits":list_of_location_urls,
            "list_of_concepts_credits":list_of_concepts_urls
            }


def getCharacterDetail(character_credits):
    #function to return the image info of a character

    response = requests.get(character_credits +'?api_key='+ YOUR_API_KEY +'&format=json', headers=headers)

    results = response.json()['results']

    character_image = results['image']['icon_url']

    character_name = results['name']
    
    return {'image':character_image,
            'name ':character_name
            }

def getTeamDetail(team_credits):
    #function to return the image an name of an specific team
    
    response = requests.get(team_credits +'?api_key='+ YOUR_API_KEY +'&format=json', headers=headers)

    results = response.json()['results']

    teams_image = results['image']['icon_url']

    teams_name = results['name']
    
    return {'image':teams_image,
            'name ':teams_name
            }

def getLocationDetail(location_credits):
    #function to return the image and name of a specific location
    
    response = requests.get(location_credits +'?api_key='+ YOUR_API_KEY +'&format=json', headers=headers)

    results = response.json()['results']

    location_image = results['image']['icon_url']

    location_name = results['name']
    
    return {'image':location_image,
            'name ':location_name
            }

def getConceptDetail(concept_credits):
    # function to return the info the image an name of a specific concepts

    response = requests.get(concept_credits +'?api_key='+ YOUR_API_KEY +'&format=json', headers=headers)

    results = response.json()['results']

    concept_image = results['image']['icon_url']

    concept_name = results['name']
    
    return {'image':concept_image,
            'name ':concept_name
            }
                      

def getAllComicBookDetail(api_url):
    # get image and name for all name, team, location, concept - multithhreding to improve speed
    
    issue_detail = getIssueDetail(api_url)

    final_list = {}
    
    comic_book_image = issue_detail.get("comics_image")
    character_list = issue_detail.get('list_character_credits')
    teams_list = issue_detail.get('list_team_credits')
    location_list = issue_detail.get('list_location_credits')
    #concept_list = issue_detail.get('list_of_concepts_credits')

    #final_list.append(comic_book_image)

    each_character_info = []
    each_teams_info = []
    each_location_info = []

    for i in range(len(character_list)):
        each_character_info = getCharacterDetail(character_list[i])

    for i in range(len(teams_list)):
        each_teams_info = getTeamDetail(teams_list[i])

    for i in range(len(location_list)):
       each_location_info = getLocationDetail(location_list[i])

    #for i in range(len(concept_list)):
        #each_concept_info = getConceptDetail(concept_list[i])
    #final_list.append(each_concept_info)
    
    final_list = {"comic_image":comic_book_image,
                " characters": each_character_info,
                "teams": each_teams_info,
                "location":each_location_info
    }
    print(final_list)
    return final_list

getListofComicsInfo()
getAllComicBookDetail('https://comicvine.gamespot.com/api/issue/4000-731886/')