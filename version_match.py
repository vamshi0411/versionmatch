import requests
import json
import re
east_applicationversion = [
{ 'name': 'Beagle Services', 'url': 'pe-non-actdvcagg-app-active-ext/heartbeat' },
{ 'name': 'Apid App', 'url': 'pe-non-apid-app-active-ext/heartbeat' },
{ 'name': 'Beagle', 'url': 'pe-non-actdvcs-app-active-int/heartbeat' },
{ 'name': 'AttachView-Njs', 'url': 'pe-non-attachview-njs-active-int/heartbeat' },
{ 'name': 'AttechApi', 'url': 'pe-non-attechapi-app-active-int/heartbeat' },
{ 'name': 'Basket Api', 'url': 'pe-non-basketapi-app-active-ext/heartbeat' },
{ 'name': 'Button State', 'url': 'pe-non-bttnstate-app-active-int/heartbeat' },
{ 'name': 'Kraken Cld', 'url': 'pe-non-krakencld-app-active-int/heartbeat' },
{ 'name': 'Clipper', 'url': 'pe-browse-clipper-active-int/AvailabilityService/api/heartbeat' },
{ 'name': 'Case Graph', 'url': 'pe-non-casegraph-app-active-int/heartbeat' },
{ 'name': 'Commerce Services', 'url': 'pe-non-cmmrsrvcs-app-active-int/heartbeat' },
{ 'name': 'Customer Agreements(cstagraph)', 'url': 'pe-rpi-cstagrgph-app-active-int/heartbeat' },
{ 'name': 'AutoTech Njs', 'url': 'pe-non-autotech-njs-active-ext/heartbeat' },
{ 'name': 'Config Read', 'url': 'pe-non-cfgread-app-active-int/heartbeat' },
{ 'name': 'Cuso Web', 'url': 'pe-non-cusoweb-njs-active-ext/heartbeat' },
{ 'name': 'Pricing Coupons', 'url': 'pe-non-cpnsrv-app-active-int/heartbeat' },
{ 'name': 'Calliagtor(new VPC)', 'url': 'pe-non-cllgtrcld-app-active-int/heartbeat' },
{ 'name': 'Digital Gateway', 'url': 'pe-3rd-dagatwy-app-active-ext/heartbeat' },
{ 'name': 'Digital Orchestrator', 'url': 'pe-3rd-dgtassorc-app-active-int/heartbeat' },
{ 'name': 'Dossier-Njs', 'url': 'pe-non-dossier-njs-active-ext/heartbeat' },
{ 'name': 'Dossier-App', 'url': 'pe-non-dossier-app-active-int/heartbeat' },
{ 'name': 'EBay Orders', 'url': 'pe-non-ebayord-app-active-int/heartbeat' },
{ 'name': 'Expert Review', 'url': 'pe-non-excnexrvw-app-active-int/heartbeat' },
{ 'name': 'Exc-Ecorebates', 'url': 'pe-non-ecorbates-app-active-int/heartbeat' },
{ 'name': 'Emit-app', 'url': 'pe-non-emit-app-active-int/heartbeat' },
{ 'name': 'FulFillment-View', 'url': 'pe-non-fulfview-njs-active-ext/heartbeat' },
{ 'name': 'Exc Video Domain Service', 'url': 'pe-non-excvmds-app-active-int/heartbeat' },
{ 'name': 'GeekTriage', 'url': 'pe-non-geektriage-app-active-int/heartbeat' },
{ 'name': 'GeekSquad Cloud', 'url': 'pe-non-geeksqcld-app-active-ext/heartbeat' },
{ 'name': 'Kuffs', 'url': 'pe-non-kuffs-app-active-int/heartbeat' },
{ 'name': 'Location', 'url': 'pe-browse-location-active-int/location/heartbeat' },
{ 'name': 'Mag-Delta', 'url': 'pe-non-magdelta-app-active-int/heartbeat' },
{ 'name': 'Group Scheduling', 'url': 'pe-non-groupsch-app-active-ext/heartbeat' },
{ 'name': 'Device Graph Njs', 'url': 'pe-non-dvcgraph-njs-active-int/heartbeat' },
{ 'name': 'Mexico-Web', 'url': 'pe-mex-mexico-web-active-int/heartbeat' },
{ 'name': 'Mexico Njs', 'url': 'pe-mex-mexico-njs-active-int/heartbeat' },
{ 'name': 'Service Interceptor(Naif)', 'url': 'pe-non-naifweb-app-active-int/heartbeat' },
{ 'name': 'NhanceView-njs', 'url': 'pe-non-nhancview-njs-active-int/heartbeat' },
{ 'name': 'Browse NodeJs', 'url': 'pe-browse-nodejs-active-int/heartbeat' },
{ 'name': 'Bundle and save app', 'url': 'pe-non-ofrsvapi-app-active-int/heartbeat' },
{ 'name': 'Pisces(Orville)', 'url': 'pe-browse-orville-active-ext/heartbeat' },
 { 'name': 'Pixie App', 'url': 'pe-non-pixie-app-active-int/heartbeat' },
{ 'name': 'PLP View Njs', 'url': 'pe-non-plpview-njs-active-int/heartbeat' },
{ 'name': 'Price View Njs', 'url': 'pe-bro-priceview-njs-active-int/heartbeat' },
{ 'name': 'Platview Njs', 'url': 'pe-non-platview-njs-active-int/heartbeat' },
{ 'name': 'Resource Server(New VPC)', 'url': 'pe-non-rsrsrvcld-app-active-int/heartbeat' },
{ 'name': 'Plprofile', 'url': 'pe-non-plprofile-njs-active-ext/heartbeat' },
{ 'name': 'Qnaview-njs', 'url': 'pe-non-qnaview-njs-active-int/heartbeat' },
{ 'name': 'Wrangler(porerelag)', 'url': 'pe-non-prorelagg-app-active-int/heartbeat' },
{ 'name': 'SCDS-API', 'url': 'pe-bro-scds-api-active-int/heartbeat' },
{ 'name': 'STS Internal', 'url': 'pe-non-sctksrint-app-active-int/heartbeat' },
{ 'name': 'Psychic-app', 'url': 'pe-non-psychic-app-active-int/heartbeat' },
{ 'name': 'Search-Api', 'url': 'pe-non-searchapi-app-active-int/heartbeat' },
{ 'name': 'Service Interceptor DeltaCache(SIDCS)', 'url': 'pe-non-sidcs-app-active-int/heartbeat' },
{ 'name': 'SCS Agg(SRVCMPWRV)', 'url': 'pe-non-srvcmpwrv-app-active-int/heartbeat' },
{ 'name': 'Service Interceptor Native Cart', 'url': 'pe-non-srvintnc-app-active-int/heartbeat' },
{ 'name': 'Service Interceptor Own', 'url': 'pe-non-srvintown-app-active-int/heartbeat' },
{ 'name': 'Store Domain', 'url': 'pe-store-active-int/heartbeat' },
{ 'name': 'STS External(New VPC)', 'url': 'pe-non-stsext-app-active-ext/heartbeat' },
{ 'name': 'Suggest Api', 'url': 'pe-non-sggestapi-app-active-int/heartbeat' },
{ 'name': 'Span Api', 'url': 'pe-non-spanapi-app-active-int/heartbeat' },
{ 'name': 'Suggest Web/App', 'url': 'pe-non-suggest-app-active-int/heartbeat' },
{ 'name': 'Pricing Services Engine', 'url': 'pe-non-pricereng-app-active-int/heartbeat' },
{ 'name': 'TotalTech', 'url': 'pe-non-totltech-app-active-ext/heartbeat' },
{ 'name': 'Transaction Graph', 'url': 'pe-non-trnsgraph-app-active-int/heartbeat' },
{ 'name': 'Ugc Api App', 'url': 'pe-non-ugcapi-app-active-int/heartbeat' },
{ 'name': 'UGC-Njs', 'url': 'pe-bro-ugc-njs-active-int/heartbeat' },
{ 'name': 'Widget View', 'url': 'pe-non-widgetview-njs-active-int/heartbeat' },
{ 'name': 'Visitor Graph', 'url': 'pe-bro-vgraph-api-active-int/heartbeat' },
{ 'name': 'UCR', 'url': 'pe-non-usrclasres-app-active-int/heartbeat' },
{ 'name': 'ZK Agent', 'url': 'pe-bro-zkagent-svc-active-int/zk-agent/heartbeat' },
 { 'name': 'Pricing-Services-Aggregator', 'url': 'pe-non-priceragg-app-active-ext/heartbeat' }
            ]

east_version = [
 { 'name': 'Product Fulfillment(Profulfil)', 'url': 'pe-bro-profulfil-web-active-ext/productfulfillment/heartbeat' },
 {'name': 'Affcom Njs', 'url': 'pe-non-affcomm-njs-active-int/heartbeat' }
]

east_Version = [
 { 'name': 'Search Master', 'url': 'pe-search-master-active-int/search-api/health' },
 { 'name': 'Search Repeater', 'url': 'pe-search-repeater-active-int/search-api/health' },
 { 'name': 'Search SAAS', 'url': 'pe-search-saas-active-int/search-api/health' }
]



west_applicationversion = [
    { 'name': 'Beagle Services', 'url': 'pw-non-actdvcagg-app-active-ext/heartbeat' },
    { 'name': 'Apid App', 'url': 'pw-non-apid-app-active-ext/heartbeat' },
    { 'name': 'Magellan Calligator', 'url': 'pw-browse-calligator-active-int/heartbeat' },
    { 'name': 'Beagle', 'url': 'pw-non-actdvcs-app-active-int/heartbeat' },
    { 'name': 'AttachView-Njs', 'url': 'pw-non-attachview-njs-active-int/heartbeat' },
    { 'name': 'AttechApi', 'url': 'pw-non-attechapi-app-active-int/heartbeat' },
    { 'name': 'Button State', 'url': 'pw-non-bttnstate-app-active-int/heartbeat' },
    { 'name': 'Calliagtor(new VPC)', 'url': 'pw-non-cllgtrcld-app-active-int/heartbeat' },
    { 'name': 'Kraken Cld', 'url': 'pw-non-krakencld-app-active-int/heartbeat' },
    { 'name': 'Basket Api', 'url': 'pw-non-basketapi-app-active-ext/heartbeat' },
    { 'name': 'Clipper', 'url': 'pw-browse-clipper-active-int/AvailabilityService/api/heartbeat' },
    { 'name': 'AutoTech Njs', 'url': 'pw-non-autotech-njs-active-ext/heartbeat' },
    { 'name': 'Config Read', 'url': 'pw-non-cfgread-app-active-int/heartbeat' },
    { 'name': 'Bundle and save app', 'url': 'pw-non-ofrsvapi-app-active-int/heartbeat' },
    { 'name': 'Cuso Web', 'url': 'pw-non-cusoweb-njs-active-ext/heartbeat' },
    { 'name': 'Case Graph', 'url': 'pw-non-casegraph-app-active-int/heartbeat' },
    { 'name': 'Customer Agreements(cstagraph)', 'url': 'pw-rpi-cstagrgph-app-active-int/heartbeat' },
    { 'name': 'Digital Gateway', 'url': 'pw-3rd-dagatwy-app-active-ext/heartbeat' },
    { 'name': 'Digital Orchestrator', 'url': 'pw-3rd-dgtassorc-app-active-int/heartbeat' },
    { 'name': 'Expert Review', 'url': 'pw-non-excnexrvw-app-active-int/heartbeat' },
    { 'name': 'Dossier-Njs', 'url': 'pw-non-dossier-njs-active-ext/heartbeat' },
    { 'name': 'Dossier-App', 'url': 'pw-non-dossier-app-active-int/heartbeat' },
    { 'name': 'Exc-Ecorebates', 'url': 'pw-non-ecorbates-app-active-int/heartbeat' },
    { 'name': 'FulFillment-View', 'url': 'pw-non-fulfview-njs-active-ext/heartbeat' },
    { 'name': 'Exc Video Domain Service', 'url': 'pw-non-excvmds-app-active-int/heartbeat' },
    { 'name': 'GeekTriage', 'url': 'pw-non-geektriage-app-active-int/heartbeat' },
    { 'name': 'GeekSquad Cloud', 'url': 'pw-non-geeksqcld-app-active-ext/heartbeat' },
    { 'name': 'Group Scheduling', 'url': 'pe-non-groupsch-app-active-ext/heartbeat' },
    { 'name': 'Ignite-Njs', 'url': 'pw-bro-ignite-njs-active-ext/heartbeat' },
    { 'name': 'Price View Njs', 'url': 'pw-bro-priceview-njs-active-int/heartbeat' },
    { 'name': 'Pixie App', 'url': 'pw-non-pixie-app-active-int/heartbeat' },
    { 'name': 'Platview Njs', 'url': 'pw-non-platview-njs-active-int/heartbeat' },
    { 'name': 'Resource Server(New VPC)', 'url': 'pw-non-rsrsrvcld-app-active-int/heartbeat' },
    { 'name': 'Kuffs', 'url': 'pw-non-kuffs-app-active-int/heartbeat' },
    { 'name': 'Plprofile', 'url': 'pw-non-plprofile-njs-active-ext/heartbeat' },
    { 'name': 'Location', 'url': 'pw-browse-location-active-int/location/heartbeat' },
    { 'name': 'Mag-Delta', 'url': 'pw-non-magdelta-app-active-int/heartbeat' },
    { 'name': 'Device Graph Njs', 'url': 'pw-non-dvcgraph-njs-active-int/heartbeat' },
    { 'name': 'Mexico-Web', 'url': 'pw-mex-mexico-web-active-int/heartbeat' },
    { 'name': 'Mexico Njs', 'url': 'pw-mex-mexico-njs-active-int/heartbeat' },
    { 'name': 'Service Interceptor(Naif)', 'url': 'pw-non-naifweb-app-active-int/heartbeat' },
    { 'name': 'NhanceView-njs', 'url': 'pw-non-nhancview-njs-active-int/heartbeat' },
    { 'name': 'Browse NodeJs', 'url': 'pw-browse-nodejs-active-int/heartbeat' },
    { 'name': 'Pisces(Orville)', 'url': 'pw-browse-orville-active-ext/heartbeat' },
    { 'name': 'PLP View Njs', 'url': 'pw-non-plpview-njs-active-int/heartbeat' },
    { 'name': 'SCDS-API', 'url': 'pw-bro-scds-api-active-int/heartbeat' },
    { 'name': 'Psychic-app', 'url': 'pw-non-psychic-app-active-int/heartbeat' },
    { 'name': 'STS Internal', 'url': 'pw-non-sctksrint-app-active-int/heartbeat' },
    { 'name': 'Search-Api', 'url': 'pw-non-searchapi-app-active-int/heartbeat' },
    { 'name': 'Suggest Api', 'url': 'pw-non-sggestapi-app-active-int/heartbeat' },
    { 'name': 'Service Interceptor DeltaCache(SIDCS)', 'url': 'pw-non-sidcs-app-active-int/heartbeat' },
    { 'name': 'Solar Index Agent', 'url': 'pw-bro-solrindex-svc-active-int/heartbeat' },
    { 'name': 'SCS Agg(SRVCMPWRV)', 'url': 'pw-non-srvcmpwrv-app-active-int/heartbeat' },
    { 'name': 'Service Interceptor Native Cart', 'url': 'pw-non-srvintnc-app-active-int/heartbeat' },
    { 'name': 'Service Interceptor Own', 'url': 'pw-non-srvintown-app-active-int/heartbeat' },
    { 'name': 'Store Domain', 'url': 'pw-store-active-int/heartbeat' },
    { 'name': 'STS External', 'url': 'pw-falcon-sts-active-ext/heartbeat' },
    { 'name': 'Qnaview-njs', 'url': 'pw-non-qnaview-njs-active-int/heartbeat' },
    { 'name': 'STS External(New VPC)', 'url': 'pw-non-stsext-app-active-ext/heartbeat' },
    { 'name': 'Span Api', 'url': 'pw-non-spanapi-app-active-int/heartbeat' },
    { 'name': 'Suggest Web/App', 'url': 'pw-non-suggest-app-active-int/heartbeat' },
    { 'name': 'TotalTech', 'url': 'pw-non-totltech-app-active-ext/heartbeat' },
    { 'name': 'Transaction Graph', 'url': 'pw-non-trnsgraph-app-active-int/heartbeat' },
    { 'name': 'UGC Api', 'url': 'pw-bro-ugc-api-active-int/heartbeat' },
    { 'name': 'Pricing-Services-Aggregator', 'url': 'pw-non-priceragg-app-active-ext/heartbeat' },
    { 'name': 'Pricing Services Engine', 'url': 'pw-non-pricereng-app-active-int/heartbeat' },
    { 'name': 'UGC-Njs', 'url': 'pw-bro-ugc-njs-active-int/heartbeat' },
    { 'name': 'Ugc Api App', 'url': 'pw-non-ugcapi-app-active-int/heartbeat' },
    { 'name': 'Widget View', 'url': 'pw-non-widgetview-njs-active-int/heartbeat' },
    { 'name': 'UCR', 'url': 'pw-non-usrclasres-app-active-int/heartbeat' },
    { 'name': 'Visitor Graph', 'url': 'pw-bro-vgraph-api-active-int/heartbeat' },
    { 'name': 'ZK Agent', 'url': 'pw-bro-zkagent-svc-active-int/zk-agent/heartbeat' },
    { 'name': 'Product Fulfillment(Profulfil)', 'url': 'pw-bro-profulfil-web-active-ext/productfulfillment/heartbeat' },
    ]

west_version = [
 { 'name': 'Product Fulfillment(Profulfil)', 'url': 'pw-bro-profulfil-web-active-ext/productfulfillment/heartbeat' },
 # {'name': 'Affcom Njs', 'url': 'pw-non-affcomm-njs-active-int/heartbeat' }
 ]



west_Version = [
 { 'name': 'Search Master', 'url': 'pw-search-master-active-int/search-api/health' },
 # { 'name': 'Search Repeater', 'url': 'pw-search-repeater-active-int/search-api/health' },
 # { 'name': 'Search SAAS', 'url': 'pw-search-saas-active-int/search-api/health' }
]


def curl_version(data):
    response = requests.post('https://dashboard-service-canaryautomation-canary.omnitank.bestbuy.com/dashboardservice/data/prodheartbeat', data=data)
    jdata = json.loads(response.text)
    return (jdata['applicationVersion'])


def curl_version2(data):
    response = requests.post('https://dashboard-service-canaryautomation-canary.omnitank.bestbuy.com/dashboardservice/data/prodheartbeat', data=data)
    jdata = json.loads(response.text)
    return (jdata['version'])

def curl_version3(data):
    response = requests.post('https://dashboard-service-canaryautomation-canary.omnitank.bestbuy.com/dashboardservice/data/prodheartbeat', data=data)
    jdata = json.loads(response.text)
    return (jdata['Version'])


def send_status_to_hipchat(message,color):
    room_id_real = "3900"
    auth_token_real = "YLrql28g98EVrrHPQTrkhkvzPogC7GmLlTZT7MOB"
    url = 'https://hipchat.bestbuy.com/v2/room/3900/notification'
    headers = {
        "content-type": "application/json",
        "authorization": "Bearer %s" % auth_token_real}
    datastr = json.dumps({
        'message': message,
        'color': color,
        'message_format': 'text',
        'notify': False,
        'from': 'From Jenkins'})
    request = requests.post(url, headers=headers, data=datastr)
    print (request.text)
    print ("posted to hipchat", message, color)
    return request.status_code


count = 0
for each in east_applicationversion:
    for each1 in west_applicationversion:
        if (each['name']) == (each1['name']):
            if (curl_version(each['url'])) == (curl_version(each1['url'])):
                print (each['name'], (curl_version(each['url'])))
            else:
                # print ("versions are not same")
                print (each['name'] + " east version is " + (curl_version(each['url'])) + " and west version is " + (curl_version(each1['url'])))
                count += 1
                send_status_to_hipchat(each['name'] + " east version is " + (curl_version(each['url'])) + " and west version is " + (curl_version(each1['url'])), "red")
#         else:
#             # print ("apps are not same")
#             # print ((curl_version(each['url'])), (curl_version(each1['url'])), each['name'], each1['name'])

for each in east_version:
    for each1 in west_version:
        if (each['name']) == (each1['name']):
            if (curl_version2(each['url'])) == (curl_version2(each1['url'])):
                print (each['name'], (curl_version2(each['url'])))
            else:
                # print ("versions are not same")
                print (each['name'] + " east version is " + (curl_version2(each['url'])) + " and west version is " + (curl_version2(each1['url'])))
                count += 1
                send_status_to_hipchat(each['name'] + " east version is " + (curl_version2(each['url'])) + " and west version is " + (curl_version2(each1['url'])), "red")
        # else:
            # print ("apps are not same")
            # print ((curl_version(each['url'])), (curl_version(each1['url'])), each['name'], each1['name'])

for each in east_Version:
    for each1 in west_Version:
        if (each['name']) == (each1['name']):
            if (curl_version3(each['url'])) == (curl_version3(each1['url'])):
                print (each['name'], (curl_version3(each['url'])))
            else:
                # print ("versions are not same")
                print (each['name'] + " east version is " + (curl_version(each['url'])) + " and west version is " + (curl_version(each1['url'])))
                count += 1
                send_status_to_hipchat(each['name'] + " east version is " + (curl_version3(each['url'])) + " and west version is " + (curl_version3(each1['url'])), "red")


if count == 0:
    send_status_to_hipchat("All Application versions are consistent in East and West","green")
