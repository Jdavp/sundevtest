#!/usr/bin/python3
import requests, datetime, json
from models.issue_detail import getIssueDetail
from models.characters import getCharacterDetail
from models.team import getTeamDetail 
from models.location import getLocationDetail



def getAllComicBookDetail(api_id, YOUR_API_KEY, headers):
    # get image and name for all name, team, location, concept - multithhreding to improve speed
    
    issue_detail = getIssueDetail(api_id, YOUR_API_KEY, headers)

    #final_list = []
    
    comic_book_image = issue_detail.get("comics_image")
    character_list = issue_detail.get('list_character_ids')
    teams_list = issue_detail.get('list_team_ids')
    location_list = issue_detail.get('list_location_ids')
    #concept_list = issue_detail.get('list_of_concepts_credits')

    #final_list.append(comic_book_image)

    each_character_info = []
    each_teams_info = []
    each_location_info = []

    for i in range(len(character_list)):
        each_character_info.append(getCharacterDetail(character_list[i], YOUR_API_KEY, headers))   

    for i in range(len(teams_list)):
        each_teams_info.append(getTeamDetail(teams_list[i], YOUR_API_KEY, headers))

    for i in range(len(location_list)):
       each_location_info.append(getLocationDetail(location_list[i], YOUR_API_KEY, headers))
    print(each_character_info)
    #for i in range(len(concept_list)):
        #each_concept_info = getConceptDetail(concept_list[i])
    #final_list.append(each_concept_info)

    print(character_list)
    print(each_character_info)
    print(teams_list)
    print(each_teams_info)
    print(location_list)
    print(each_location_info)
    return  {
                "comic_image":comic_book_image,
                "Characters": each_character_info,
                "Teams": each_teams_info,
                "Location":each_location_info
            }
