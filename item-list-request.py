#imports
import requests
import json


URL = "https://api.warframe.market/v1/items"


client = requests.session()


item_list = json.loads(client.get(URL).text)['payload']['items']['en']


print json.dumps(item_list, indent=2, sort_keys=False)
