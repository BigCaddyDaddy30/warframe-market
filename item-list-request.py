#imports
import requests
import json

#variable for the url
URL = "https://api.warframe.market/v1/items"

#this is the http request to the api 
client = requests.session()

#this parses in the JSON file to a list of dictionaries in python
item_list = json.loads(client.get(URL).text)['payload']['items']['en']


#Print the JSON into a text file
item_list_textfile = open("item-list-output.txt","w")

item_list_textfile.write(json.dumps(item_list, indent=2, sort_keys=True))

item_list_textfile.close()


#Print the JSON object to a JSON file
item_list_jsonfile = open("item-list.json","w")

item_list_jsonfile.write(json.dumps(item_list, indent=2, sort_keys=True))

item_list_jsonfile.close()