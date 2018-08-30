import json
import requests



URL = "https://api.warframe.market/v1/items"
client = requests.session()


item_list = json.loads(client.get(URL).text)['payload']['items']['en']
html_string = ""






#Print tests
#print(item_list[0]["item_name"])
#print(item_list[0]["url_name"])
#print(item_list[0]["id"])

item_list_htmlfile = open("item-list.html","w")
item_list_htmlfile.write(html_string)
item_list_htmlfile.close()
