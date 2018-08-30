import json
import requests



URL = "https://api.warframe.market/v1/items"
client = requests.session()


item_list = json.loads(client.get(URL).text)['payload']['items']['en']
html_string = '<html><body><table style="width:100%", border=1><tr><th>URL NAME</th><th>ITEM NAME</th><th>ID</th></tr>'


i=0
while i < len(item_list):
    html_string += "\n<tr><th>" + item_list[i]["url_name"] + "</th><th>" + item_list[i]["item_name"] + "</th><th>" + item_list[i]["id"] + "</th></tr>"
    i += 1
    print(i)

html_string += "</table></body></html>"

#Print tests
#print(item_list[0]["item_name"])
#print(item_list[0]["url_name"])
#print(item_list[0]["id"])

#item_list_htmlfile = open("item-list.html","w")
#item_list_htmlfile.write(html_string)
#item_list_htmlfile.close()

#item_list_textfile = open("item-list-html.txt","w")
#item_list_textfile.write(html_string)
#item_list_textfile.close()

print(html_string)