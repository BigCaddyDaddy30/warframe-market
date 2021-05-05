import requests
import json
import csv
import time


#variable for the url
URL = "https://api.warframe.market/v1/items"


#this is the http request to the api 
client = requests.session()


#this parses in the JSON file to a list of dictionaries in python for all items on the site
item_list = json.loads(client.get(URL).text)['payload']['items']['en']

#Create everything to write to CSV
csv_filename = 'master_output.csv'
master_csv = open(csv_filename, 'a')
csvwriter = csv.writer(master_csv)

#Loops through all items in the item list
i = 0
while i < len(item_list):
    #Get a list of all the orders for that specific item
    URL = "https://api.warframe.market/v1/items/" + item_list[i]['url_name'] + "/orders"
    order_list = json.loads(client.get(URL).text)['payload']['orders']

    #Write out the header row for labels
    if i == 0:
        csvwriter.writerow(["Item Name", "Minimum Price", "Average Price", "Maximum Price"])

    min_price = 0
    avg_price = 0
    max_price = 0
    price_list = [0]
    #Loop through all orders and add to lists to calculate the numbers
    j = 0
    while j < len(order_list):
        price_list.append(order_list[j]['platinum'])
        j += 1  
    del price_list[0]
    min_price = min(price_list)
    avg_price = sum(price_list) / len(price_list)
    max_price = max(price_list)
    csvwriter.writerow([item_list[i]['item_name'].encode('utf-8'), min_price.encode('utf-8'), avg_price.encode('utf-8'), max_price.encode('utf-8')])

    #Move to next item (sleep in between to make sure the site does not lock me out for too frequent queries)
    i += 1
    time.sleep(.120)

#Close csv file
master_csv.close()











####### USED FOR SCHOOL PROJECT TO COLLECT DATA #########

#Start grabbing all items
#i=0
#while i < len(item_list):
#    URL = "https://api.warframe.market/v1/items/" + item_list[i]['url_name'] + "/orders"
#    order_list = json.loads(client.get(URL).text)['payload']['orders']
#    
#    csv_filename = 'master_output.csv'
#    master_csv = open(csv_filename, 'a')
#    csvwriter = csv.writer(master_csv)
#    
#    if i == 0:
#        csvwriter.writerow(["Quantity", "Creation Date", "Order Type", "Platform", "Platinum", "Region", "Last Update", "id", "Item Name"])
#
#    j=0
#    while j < len(order_list):
#        csvwriter.writerow([order_list[j]['quantity'], order_list[j]['creation_date'], order_list[j]['order_type'].encode('utf-8'), order_list[j]['platform'].encode('utf-8'), order_list[j]['platinum'], order_list[j]['region'].encode('utf-8'), order_list[j]['last_update'], order_list[j]['id'].encode('utf-8'), item_list[i]['item_name'].encode('utf-8')])
#        j += 1 
#        
#    i += 1
#    time.sleep(.120)
#    print(i)
#
#master_csv.close()
        