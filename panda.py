import requests
import json
import re
import sys
east_cargo = [
 { 'name': 'Panda', 'url': 'pw-non-pandaweb-app-active-ext/heartbeat' }
]
west_cargo = [
 { 'name': 'Panda', 'url': 'pe-non-pandaweb-app-active-ext/heartbeat' }
]


def curl_version(data):
       response = requests.post('https://dashboard-service-canaryautomation-canary.omnitank.bestbuy.com/dashboardservice/data/prodheartbeat', data=data)
       jdata = json.loads(response.text)
       return (jdata['applicationVersion'])

def send_status_to_hipchat(message,color):
    # room_id_real = sys.argv[1]
    # auth_token_real = sys.argv[2]
    # url = 'https://hipchat.bestbuy.com/v2/room/'+room_id_real+'/notification'
    # headers = {
    #     "content-type": "application/json",
    #     "authorization": "Bearer %s" % auth_token_real}
    # datastr = json.dumps({
    #     'message': message,
    #     'color': color,
    #     'message_format': 'text',
    #     'notify': True,
    #     'from': 'From Jenkins'})
    # request = requests.post(url, headers=headers, data=datastr)
    # print (request.text)
    # print ("posted to hipchat", message, color)
    # return request.status_code
    print ("from hichat")


for each in east_cargo:
    for each1 in west_cargo:
        if (each['name']) == (each1['name']):
            if (curl_version(each['url'])) == (curl_version(each1['url'])):
                print (each['name'], (curl_version(each['url'])))
            else:
                print (each['name'] + " east version is " + (curl_version(each['url'])) + " and west version is " + (curl_version(each1['url'])))
                count += 1
                send_status_to_hipchat(each['name'] + " east version is " + (curl_version(each['url'])) + " and west version is " + (curl_version(each1['url'])), "red")


with open('east1.json') as json_file:
    data1 = json.load(json_file)
    # print (data1)
    with open('west1.json') as json_file2:
         data2 = json.load(json_file2)
         for each in data1:
             for each1 in data2:
                 if (each) == (each1):
                     print each
                     if (curl_version(data1[each])) == (curl_version(data2[each1])):
                         print (each, (curl_version(data1[each])))
                     else:
                        print ( each + " east version is " + curl_version(data1[each]) + " and west version is " + curl_version(data2[each1]))
                        count += 1
                        send_status_to_hipchat(each + " east version is " + curl_version(data1[each]) + " and west version is " + curl_version(data2[each1]), "red")
