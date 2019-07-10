import requests
import json
import re
import sys

east_status = [
  { 'name': 'Plunger', 'url': 'pe-browse-plunger-active-ext/plunger/health_check' }
 ]

east_cargo = [
 { 'name': 'CBA', 'url': 'pe-browse-web-vpc-active-int/heartbeat' },
 { 'name': 'Panda', 'url': 'pe-browse-panda-active-ext/heartbeat' }
]

east_scp = [
 { 'name': 'exc-slr', 'url': 'pe-non-exc-slr-active-int/solr/admin/info/properties?wt=json' },
 { 'name': 'recs-slr', 'url': 'pe-non-recs-slr-active-int/solr/admin/info/properties?wt=json' },
 { 'name': 'search-slr', 'url': 'pe-non-search-slr-active-int/solr/admin/info/properties?wt=json' },
 { 'name': 'Suggestcld-slr', 'url': 'pe-non-sggestcld-slr-active-int/solr/admin/info/properties?wt=json' },
 { 'name': 'VPT-slr', 'url': 'pe-non-vpt-slr-active-int/solr/admin/info/properties?wt=json' },
 { 'name': 'UGC-slr', 'url': 'pe-bro-ugc-slr-active-int/solr/admin/info/properties?wt=json' },
 { 'name': 'suggestv3-slr', 'url': 'pe-non-suggestv3-slr-active-int/solr/admin/info/properties?wt=json' }
]

west_status = [
  { 'name': 'Plunger', 'url': 'pw-browse-plunger-active-ext/plunger/health_check' }
 ]

west_cargo = [
 { 'name': 'CBA', 'url': 'pe-browse-web-vpc-active-int/heartbeat' },
 { 'name': 'Panda', 'url': 'pw-browse-panda-active-ext/heartbeat' }
]

west_scp = [
 { 'name': 'exc-slr', 'url': 'pw-non-exc-slr-active-int/solr/admin/info/properties?wt=json' },
 { 'name': 'recs-slr', 'url': 'pw-non-recs-slr-active-int/solr/admin/info/properties?wt=json' },
 { 'name': 'search-slr', 'url': 'pw-non-search-slr-active-int/solr/admin/info/properties?wt=json' },
 { 'name': 'UGC-slr', 'url': 'pw-bro-ugc-slr-active-int/solr/admin/info/properties?wt=json' },
 { 'name': 'VPT-slr', 'url': 'pw-non-vpt-slr-active-int/solr/admin/info/properties?wt=json' },
 { 'name': 'Suggestcld-slr', 'url': 'pw-non-sggestcld-slr-active-int/solr/admin/info/properties?wt=json' },
 { 'name': 'suggestv3-slr', 'url': 'pw-non-suggestv3-slr-active-int/solr/admin/info/properties?wt=json' }
]

def curl_version(data):
     response = requests.post('https://dashboard-service-canaryautomation-canary.omnitank.bestbuy.com/dashboardservice/data/prodheartbeat', data=data)
     jdata = json.loads(response.text)
     return (jdata['applicationVersion'])

def curl_version4(data):
    response = requests.post('https://dashboard-service-canaryautomation-canary.omnitank.bestbuy.com/dashboardservice/data/prodheartbeat', data=data)
    return (response.text)

def curl_version5(data):
    response = requests.post('https://dashboard-service-canaryautomation-canary.omnitank.bestbuy.com/dashboardservice/data/prodheartbeat', data=data)
    jdata = json.loads(response.text)
    next = jdata.get("system.properties")
    return (next['bby.scp.version'])

def curl_version6(data):
    response = requests.post('https://dashboard-service-canaryautomation-canary.omnitank.bestbuy.com/dashboardservice/data/prodheartbeat', data=data)
    jdata = json.loads(response.text)
    next = jdata.get("status")
    return (next['version'])


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


count = 0
with open('east.json') as json_file:
    data1 = json.load(json_file)
    # print (data1)
    with open('west.json') as json_file2:
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


for each in east_cargo:
    for each1 in west_cargo:
        if (each['name']) == (each1['name']):
            if (curl_version4(each['url'])) == (curl_version4(each1['url'])):
                print (each['name'], (curl_version4(each['url'])))
            else:
                print (each['name'] + " east version is " + (curl_version4(each['url'])) + " and west version is " + (curl_version4(each1['url'])))
                count += 1
                send_status_to_hipchat(each['name'] + " east version is " + (curl_version4(each['url'])) + " and west version is " + (curl_version4(each1['url'])), "red")


for each in east_scp:
    for each1 in west_scp:
        if (each['name']) == (each1['name']):
            if (curl_version5(each['url'])) == (curl_version5(each1['url'])):
                print (each['name'], (curl_version5(each['url'])))
            else:
                print (each['name'] + " east version is " + (curl_version5(each['url'])) + " and west version is " + (curl_version5(each1['url'])))
                count += 1
                send_status_to_hipchat(each['name'] + " east version is " + (curl_version5(each['url'])) + " and west version is " + (curl_version5(each1['url'])), "red")

for each in east_status:
    for each1 in west_status:
        if (each['name']) == (each1['name']):
            if (curl_version6(each['url'])) == (curl_version6(each1['url'])):
                print (each['name'], (curl_version6(each['url'])))
            else:
                print (each['name'] + " east version is " + (curl_version6(each['url'])) + " and west version is " + (curl_version6(each1['url'])))
                count += 1
                send_status_to_hipchat(each['name'] + " east version is " + (curl_version6(each['url'])) + " and west version is " + (curl_version6(each1['url'])), "red")

if count == 0:
    print ("all good")
    send_status_to_hipchat("All Application versions are consistent in East and West","green")
