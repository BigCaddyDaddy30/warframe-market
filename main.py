import requests
import json
import csv
import time


#variable for the url
URL = "https://api.warframe.market/v1/items"


#this is the http request to the api 
client = requests.session()


#this parses in the JSON file to a list of dictionaries in python
item_list = json.loads(client.get(URL).text)['payload']['items']['en']


#Start grabbing all items
i=0
while i < len(item_list):
    URL = "https://api.warframe.market/v1/items/" + item_list[i]['url_name'] + "/orders"
    order_list = json.loads(client.get(URL).text)['payload']['orders']
    
    csv_filename = 'master_output.csv'
    master_csv = open(csv_filename, 'a')
    csvwriter = csv.writer(master_csv)
    
    if i == 0:
        csvwriter.writerow(["Quantity", "Creation Date", "Order Type", "Platform", "Platinum", "Region", "Last Update", "id", "Item Name"])

    j=0
    while j < len(order_list):
        csvwriter.writerow([order_list[j]['quantity'], order_list[j]['creation_date'], order_list[j]['order_type'].encode('utf-8'), order_list[j]['platform'].encode('utf-8'), order_list[j]['platinum'], order_list[j]['region'].encode('utf-8'), order_list[j]['last_update'], order_list[j]['id'].encode('utf-8'), item_list[i]['item_name'].encode('utf-8')])
        j += 1 
        
    i += 1
    time.sleep(.120)
    print(i)

master_csv.close()
        