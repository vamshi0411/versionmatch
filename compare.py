import requests
import subprocess
import os
import json
import re
import sys

Token = sys.argv[1]
# username = sys.argv[2]
# password = sys.argv[3]

def curl_version(data):
    response = requests.post('https://dashboard-service-canaryautomation-canary.omnitank.bestbuy.com/dashboardservice/data/prodheartbeat', data=data)
    if 'applicationVersion' in response.text:
        return True
    else:
        return False

def list_apps():
    # Token= '5e7a3dfd0445233521e98badf164d2aff52c4e433479b352e8402d099eff61f7'
    url = 'https://imr.monitoring.bestbuy.com/api/applications'
    headers = {
        "content-type": "application/json",
        "authorization": "Bearer %s" % Token}
    list_request = requests.get(url, headers=headers)
    list = json.loads(list_request.text)
    # print list
    with open('browse.json', mode='w') as f:
        json.dump(list, f)
    print "done writing"

def check_app(appname):
    # appname = 'cgraph-app'
    # Token= '5e7a3dfd0445233521e98badf164d2aff52c4e433479b352e8402d099eff61f7'
    url = 'https://imr.monitoring.bestbuy.com/api/configuration/environments/prod/applications/'+appname
    headers = {
        "content-type": "application/json",
        "authorization": "Bearer %s" % Token}
    request = requests.get(url, headers=headers)
    if (request.status_code) != (200) :
        url = 'https://imr.monitoring.bestbuy.com/api/configuration/environments/cgraph_prod/applications/'+appname
        request = requests.get(url, headers=headers)
        if (request.status_code) != (200) :
            print "Not in prod and cgraph account"
            return
    data2 = json.loads(request.text)

    if 'item' not in data2:
        print "no item"
        return
    if 'configuration' not in data2['item']:
        print "No config for app"
        return
    if appname not in data2['item']['configuration']:
        print "this is not a deploy app"
        return
    # config = data2['item']['configuration'][appname]
    if "elb" not in data2['item']['configuration'][appname]:
        print "this app doesnt have farms"
        return
    elb = data2['item']['configuration'][appname]['elb']
    # print elb
    if "bdc" in elb:
        print "It is a DC app"
        return
    elif "us-west-2" in elb:
        for each in elb['us-west-2']:
            path = "-active-int/heartbeat"
            west_url = each[:-7] + path
            if not curl_version(west_url):
                print "heartbeat not responding for int"
                path = "-active-ext/heartbeat"
                west_url = each[:-7] + path
                if not curl_version(west_url):
                    print "heartbeat not responding for ext, exiting"
                    return
        for each in elb['us-east-1']:
            east_url = each[:-7] + path

    # elif "us-west-2" in elb and "/prod/" in url:
    #     west_url = "pw-non-"+appname+"-active-int/heartbeat"
    #     east_url = "pe-non-"+appname+"-active-int/heartbeat"
    else:
        print appname+" is only in east"
        return
    # if not curl_version(west_url):
    #     print "heartbeat not responding"
    #     return
    print "updating url"

    # with open('list.json', mode='w') as f:
    #     json.dump([], f)
    with open('west.json') as feedsjson:
        feeds_west = json.load(feedsjson)
    west_applicationversion = {appname: west_url}
    feeds_west.update(west_applicationversion)
    with open('west.json', mode='w') as f:
        json.dump(feeds_west, f)

    with open('east.json') as feedsjson:
        feeds_east = json.load(feedsjson)
    east_applicationversion = {appname: east_url}
    feeds_east.update(east_applicationversion)
    with open('east.json', mode='w') as f:
        json.dump(feeds_east, f)
    print "url updated"



        #     print 'it is aws app'
        # elif "bdc-" in elb:
        #     print 'it is dc app'
        # else:
        #     print "someething wrong"

    # for line in request:
    #     if re.search('us-east-1', line) is None:
    #         sys.stdout.write(line)
    # with open(request, "rb") as fin:
    #     content = json.load(fin)
    # with open("stringJson.txt", "wb") as fout:
    #     json.dump(content, fout, indent=1)
    # print (stringJson.txt)

# list_apps()
#
# with open('browse.json') as json_file:
#     data1 = json.load(json_file)
#     # for each1 in data1['items']:
#     #      print each1['name']
#     with open('east.json') as json_file2:
#          data2 = json.load(json_file2)
#          for each1 in data1['items']:
#                    count = 0
#                    for each in data2:
#                        if (each1['name']) == (each):
#                            count = count + 1
#                        else:
#                            continue
#                            # print each
#                    if count == 0:
#                        if not ( each1['name'].startswith(('skeletor')) or each1['name'].endswith(('-os', '-dc', '-ami', '-preview', '-boxes', '-frontend', '-jobs')) ):
#                        # or each1['name'].endswith(suffix2) or each1['name'].endswith(suffix3) or each1['name'].endswith(suffix4) or each1['name'].endswith(suffix5) or each1['name'].endswith(suffix6) or each1['name'].endswith(suffix7)):
#                             print each1['name']
#                             check_app(each1['name'])




os.system("git status --porcelain")
os.system("git add .")
os.system("git commit -m 'updating new urls' ")
# git_url = https://+:cricket18@github.com/vamshi0411/versionmatch.git
os.system("git push https://%s:%s@github.com/vamshi0411/versionmatch.git --all" % ('sys.argv[2]','sys.argv[3]'))
