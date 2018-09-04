import requests
import json
import csv


#variable for the url
URL = "https://api.warframe.market/v1/items"


#this is the http request to the api 
client = requests.session()


#this parses in the JSON file to a list of dictionaries in python
item_list = json.loads(client.get(URL).text)['payload']['items']['en']


#Print the JSON object to a JSON file
item_list_jsonfile = open("item_list.json","w")

item_list_jsonfile.write(json.dumps(item_list, indent=2, sort_keys=True))

item_list_jsonfile.close()


master_csv = open('/master_output.csv', 'a')
csvwriter = csv.writer(master_csv)

#Start grabbing all items
i=0
while i < len(item_list):
    URL = "https://api.warframe.market/v1/items/" + item_list['url_name'][i] + "/orders"
    order_list = json.loads(client.get(URL).text)['payload']['orders']
    j=0
    while j < len(order_list):
        if j == 0:
            header = order_list[j].keys()
            csvwriter.writerow(header)
        csvwriter.writerow(order_list[j].values())
        j += 1 
    i += 1

master_csv.close()
        