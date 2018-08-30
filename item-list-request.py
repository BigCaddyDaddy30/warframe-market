#imports
import requests
import json


URL = "https://api.warframe.market/v1/items"


client = requests.session()


item_list = json.loads(client.get(URL).text)['payload']['items']['en']


#Print the JSON into a text file
item_list_textfile = open("item-list-output.txt","w")

item_list_textfile.write(json.dumps(item_list, indent=2, sort_keys=True))

item_list_textfile.close()


#Print the JSON object to a JSON file
item_list_jsonfile = open("item-list.json","w")

item_list_jsonfile.write(json.dumps(item_list, indent=2, sort_keys=True))

item_list_jsonfile.close()