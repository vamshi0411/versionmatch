import requests
import json
import re
import sys
east_applicationversion = [
{ 'name': 'Beagle Agg', 'url': 'pe-non-actdvcagg-app-active-ext/heartbeat' },
{ 'name': 'Apid App', 'url': 'pe-non-apid-app-active-ext/heartbeat' },
{ 'name': 'Beagle Services', 'url': 'pe-non-actdvcs-app-active-int/heartbeat' },
{ 'name': 'AttachView-Njs', 'url': 'pe-non-attachview-njs-active-int/heartbeat' },
{ 'name': 'AttechApi', 'url': 'pe-non-attechapi-app-active-int/heartbeat' },
{ 'name': 'Apecchmng', 'url': 'pe-non-apecchmng-app-active-int/heartbeat' },
{ 'name': 'Apeslcsrv', 'url': 'pe-non-apeslcsrv-app-active-ext/heartbeat' },
{ 'name': 'Basket Api', 'url': 'pe-non-basketapi-app-active-ext/heartbeat' },
{ 'name': 'Button State', 'url': 'pe-non-bttnstate-app-active-int/heartbeat' },
{ 'name': 'Kraken Cld', 'url': 'pe-non-krakencld-app-active-int/heartbeat' },
{ 'name': 'Clipper', 'url': 'pe-non-clppravlblsvc-app-active-int/AvailabilityService/api/heartbeat' },
{ 'name': 'Case Graph', 'url': 'pe-non-casegraph-app-active-int/heartbeat' },
{ 'name': 'Commerce Services', 'url': 'pe-non-cmmrsrvcs-app-active-int/heartbeat' },
{ 'name': 'Customer Agreements(cstagraph)', 'url': 'pe-rpi-cstagrgph-app-active-int/heartbeat' },
{ 'name': 'AutoTech Njs', 'url': 'pe-non-autotech-njs-active-ext/heartbeat' },
{ 'name': 'Config Read', 'url': 'pe-non-cfgread-app-active-int/heartbeat' },
{ 'name': 'Cuso Web', 'url': 'pe-non-cusoweb-njs-active-ext/heartbeat' },
{ 'name': 'Pricing Coupons', 'url': 'pe-non-cpnsrv-app-active-int/heartbeat' },
{ 'name': 'Calliagtor(new VPC)', 'url': 'pe-non-cllgtrcld-app-active-int/heartbeat' },
{ 'name': 'cia', 'url': 'pe-rpi-cia-app-active-ext/heartbeat' },
{ 'name': 'Digital Gateway', 'url': 'pe-3rd-dagatwy-app-active-ext/heartbeat' },
{ 'name': 'Digital Orchestrator', 'url': 'pe-3rd-dgtassorc-app-active-int/heartbeat' },
{ 'name': 'Dossier-Njs', 'url': 'pe-non-dossier-njs-active-ext/heartbeat' },
{ 'name': 'Dossier-App', 'url': 'pe-non-dossier-app-active-int/heartbeat' },
{ 'name': 'EBay Orders', 'url': 'pe-non-ebayord-app-active-int/heartbeat' },
{ 'name': 'Expert Review', 'url': 'pe-non-excnexrvw-app-active-int/heartbeat' },
{ 'name': 'Exc-Ecorebates', 'url': 'pe-non-ecorbates-app-active-int/heartbeat' },
{ 'name': 'Emit-app', 'url': 'pe-non-emit-app-active-int/heartbeat' },
{ 'name': 'fireview-njs', 'url': 'pe-non-fireview-njs-active-int/heartbeat' },
{ 'name': 'FTS', 'url': 'pe-rpi-fts-app-active-int/heartbeat' },
{ 'name': 'FulFillment-View', 'url': 'pe-non-fulfview-njs-active-ext/heartbeat' },
{ 'name': 'Exc Video Domain Service', 'url': 'pe-non-excvmds-app-active-int/heartbeat' },
{ 'name': 'GeekTriage', 'url': 'pe-non-geektriage-app-active-int/heartbeat' },
{ 'name': 'GeekSquad Cloud', 'url': 'pe-non-geeksqcld-app-active-ext/heartbeat' },
{ 'name': 'Ihaols', 'url': 'pe-rpi-ihaols-app-active-ext/heartbeat' },
{ 'name': 'Ihasched', 'url': 'pe-rpi-ihasched-app-active-int/heartbeat' },
{ 'name': 'Inspireview', 'url': 'pe-non-inspireview-njs-active-int/heartbeat' },
{ 'name': 'ISPU', 'url': 'pe-non-ispu-app-active-ext/fulfillment/ispu/api/heartbeat' },
{ 'name': 'Shipping', 'url': 'pe-non-shipping-app-active-int/fulfillment/shipping/api/heartbeat' },
{ 'name': 'Kuffs', 'url': 'pe-non-kuffs-app-active-int/heartbeat' },
{ 'name': 'Location', 'url': 'pe-browse-location-active-int/location/heartbeat' },
{ 'name': 'List', 'url': 'pe-non-lstsrvces-app-active-ext/heartbeat' },
{ 'name': 'Mag-Delta', 'url': 'pe-non-magdelta-app-active-int/heartbeat' },
{ 'name': 'Group Scheduling', 'url': 'pe-non-groupsch-app-active-ext/heartbeat' },
{ 'name': 'gsinstsch', 'url': 'pe-rpi-gsinstsch-app-active-ext/heartbeat' },
{ 'name': 'Device Graph Njs', 'url': 'pe-non-dvcgraph-njs-active-int/heartbeat' },
{ 'name': 'Mexico-Web', 'url': 'pe-mex-mexico-web-active-int/heartbeat' },
{ 'name': 'Mexico Njs', 'url': 'pe-mex-mexico-njs-active-int/heartbeat' },
{ 'name': 'Mobview-njs', 'url': 'pe-non-mobview-njs-active-int/heartbeat' },
{ 'name': 'Service Interceptor(Naif)', 'url': 'pe-non-naifweb-app-active-int/heartbeat' },
{ 'name': 'NhanceView-njs', 'url': 'pe-non-nhancview-njs-active-int/heartbeat' },
{ 'name': 'Browse NodeJs', 'url': 'pe-browse-nodejs-active-int/heartbeat' },
{ 'name': 'OCPG', 'url': 'pe-rpi-ocpg-app-active-int/heartbeat' },
{ 'name': 'Bundle and save app', 'url': 'pe-non-ofrsvapi-app-active-int/heartbeat' },
{ 'name': 'Order Graph', 'url': 'pe-rpi-ordrgraph-app-active-int/heartbeat' },
{ 'name': 'Pisces(Orville)', 'url': 'pe-non-orville-app-active-ext/heartbeat' },
{ 'name': 'Pixie App', 'url': 'pe-non-pixie-app-active-int/heartbeat' },
{ 'name': 'PLP View Njs', 'url': 'pe-non-plpview-njs-active-int/heartbeat' },
{ 'name': 'Price View Njs', 'url': 'pe-bro-priceview-njs-active-int/heartbeat' },
{ 'name': 'Platview Njs', 'url': 'pe-non-platview-njs-active-int/heartbeat' },
{ 'name': 'Payment', 'url': 'pe-cde-paymntagg-app-active-ext/heartbeat' },
{ 'name': 'PDM Mapper', 'url': 'pe-non-pdmmapper-app-active-int/heartbeat' },
#{ 'name': 'PDM Portal', 'url': 'pe-non-pdmportal-app-active-ext/heartbeat' },
{ 'name': 'PDM Validator', 'url': 'pe-non-pdmvalidator-app-active-int/heartbeat' },
{ 'name': 'PDM Consumer', 'url': 'pe-non-pdmcnsmer-app-active-int/heartbeat' },
{ 'name': 'PDM Ingest', 'url': 'pe-non-pdmingest-app-active-int/heartbeat' },
{ 'name': 'PDM Publisher', 'url': 'pe-non-pdmpblshr-app-active-int/heartbeat' },
{ 'name': 'PDM Processor', 'url': 'pe-non-pdmprcssr-app-active-int/heartbeat' },
{ 'name': 'Resource Server(New VPC)', 'url': 'pe-non-rsrsrvcld-app-active-int/heartbeat' },
{ 'name': 'Plprofile-Njs', 'url': 'pe-non-plprofile-njs-active-ext/heartbeat' },
{ 'name': 'Plprofile-app', 'url': 'pe-non-plprofile-app-active-int/heartbeat' },
{ 'name': 'Qnaview-njs', 'url': 'pe-non-qnaview-njs-active-int/heartbeat' },
{ 'name': 'Wrangler(porerelag)', 'url': 'pe-non-prorelagg-app-active-int/heartbeat' },
{ 'name': 'SCDS-API', 'url': 'pe-non-scdsapi-app-active-int/heartbeat' },
{ 'name': 'STS Internal', 'url': 'pe-non-sctksrint-app-active-int/heartbeat' },
{ 'name': 'Psychic-app', 'url': 'pe-non-psychic-app-active-int/heartbeat' },
{ 'name': 'Search-Api', 'url': 'pe-non-searchapi-app-active-int/heartbeat' },
{ 'name': 'sercalendar', 'url': 'pe-non-sercalendar-app-active-int/heartbeat' },
{ 'name': 'Service Interceptor DeltaCache(SIDCS)', 'url': 'pe-non-sidcs-app-active-int/heartbeat' },
{ 'name': 'SCS Agg(SRVCMPWRV)', 'url': 'pe-non-srvcmpwrv-app-active-int/heartbeat' },
{ 'name': 'Service Interceptor Native Cart', 'url': 'pe-non-srvintnc-app-active-int/heartbeat' },
{ 'name': 'Service Interceptor Own', 'url': 'pe-non-srvintown-app-active-int/heartbeat' },
{ 'name': 'Store Domain', 'url': 'pe-store-active-int/heartbeat' },
{ 'name': 'STS External(New VPC)', 'url': 'pe-non-stsext-app-active-ext/heartbeat' },
{ 'name': 'Suggest Api', 'url': 'pe-non-sggestapi-app-active-int/heartbeat' },
{ 'name': 'Span Api', 'url': 'pe-non-spanapi-app-active-int/heartbeat' },
{ 'name': 'Suggest Web/App', 'url': 'pe-non-suggest-app-active-int/heartbeat' },
{ 'name': 'Solrindex-app', 'url': 'pe-non-solrindex-app-active-int/heartbeat' },
{ 'name': 'Pricing Services Engine', 'url': 'pe-non-pricereng-app-active-int/heartbeat' },
{ 'name': 'TotalTech', 'url': 'pe-non-totltech-app-active-ext/heartbeat' },
{ 'name': 'Transaction Graph', 'url': 'pe-non-trnsgraph-app-active-int/heartbeat' },
{ 'name': 'UGC-Njs', 'url': 'pe-bro-ugc-njs-active-int/heartbeat' },
{ 'name': 'Widget View', 'url': 'pe-non-widgetview-njs-active-int/heartbeat' },
{ 'name': 'Visitor Graph', 'url': 'pe-bro-vgraph-api-active-int/heartbeat' },
{ 'name': 'UCR', 'url': 'pe-non-usrclasres-app-active-int/heartbeat' },
{ 'name': 'ZK Agent', 'url': 'pe-bro-zkagent-svc-active-int/zk-agent/heartbeat' },
{ 'name': 'Pricing-Services-Aggregator', 'url': 'pe-non-priceragg-app-active-ext/heartbeat' },
#{ 'name': 'CSI', 'url': 'pe-csi-web-active-ext/api/csiservice/heartbeat'},
{ 'name': 'Customer-Graph', 'url': 'pe-rpi-cgraph-app-active-int/heartbeat'},
{ 'name': 'Purchase Finder', 'url': 'pe-non-prchsfndr-app-active-ext/heartbeat'},
{ 'name': 'Psychic App', 'url': 'pe-non-psychic-app-active-int/heartbeat'},
{ 'name': 'RNRView App', 'url': 'pe-non-rnrview-njs-active-int/heartbeat'},
{ 'name': 'UGC Api', 'url': 'pe-non-ugcapi-app-active-int/heartbeat' },
{ 'name': 'TTSgifting-app', 'url': 'pe-cde-ttsgifting-app-active-int/heartbeat'},
{ 'name': 'TTSgifting-Njs', 'url': 'pe-cde-ttsgifting-njs-active-ext/heartbeat'},
{ 'name': 'TRS', 'url': 'pe-non-trnrsksrv-app-active-int/heartbeat'},
{ 'name': 'Product Fulfillment(Profulfil)', 'url': 'pe-bro-profulfil-web-active-ext/productfulfillment/heartbeat' }
            ]



east_status = [
  { 'name': 'Plunger', 'url': 'pe-browse-plunger-active-ext/plunger/health_check' }
 ]



east_cargo = [
 { 'name': 'cargo-app', 'url': 'pe-bro-cargo-api-active-int/shipping-webapp/api/heartbeat' },
 { 'name': 'CBA', 'url': 'pe-browse-web-vpc-active-int/heartbeat' },
 { 'name': 'Panda', 'url': 'pe-browse-panda-active-ext/heartbeat' }
]

east_scp = [
 { 'name': 'exc-slr', 'url': 'pe-non-exc-slr-active-int/solr/admin/info/properties?wt=json' },
 { 'name': 'recs-slr', 'url': 'pe-non-recs-slr-active-int/solr/admin/info/properties?wt=json' },
 { 'name': 'search-slr', 'url': 'pe-non-search-slr-active-int/solr/admin/info/properties?wt=json' },
 { 'name': 'Suggestcld-slr', 'url': 'pe-non-sggestcld-slr-active-int/solr/admin/info/properties?wt=json' },
 { 'name': 'VPT-slr', 'url': 'pe-non-vpt-slr-active-int/solr/admin/info/properties?wt=json' },
 { 'name': 'UGC-slr', 'url': 'pe-bro-ugc-slr-active-int/solr/admin/info/properties?wt=json' }
]



west_applicationversion = [
    { 'name': 'Beagle Agg', 'url': 'pw-non-actdvcagg-app-active-ext/heartbeat' },
    { 'name': 'Apid App', 'url': 'pw-non-apid-app-active-ext/heartbeat' },
    { 'name': 'Magellan Calligator', 'url': 'pw-browse-calligator-active-int/heartbeat' },
    { 'name': 'Beagle Services', 'url': 'pw-non-actdvcs-app-active-int/heartbeat' },
    { 'name': 'AttachView-Njs', 'url': 'pw-non-attachview-njs-active-int/heartbeat' },
    { 'name': 'AttechApi', 'url': 'pw-non-attechapi-app-active-int/heartbeat' },
    { 'name': 'Apecchmng', 'url': 'pw-non-apecchmng-app-active-int/heartbeat' },
    { 'name': 'Apeslcsrv', 'url': 'pw-non-apeslcsrv-app-active-ext/heartbeat' },
    { 'name': 'Button State', 'url': 'pw-non-bttnstate-app-active-int/heartbeat' },
    { 'name': 'Calliagtor(new VPC)', 'url': 'pw-non-cllgtrcld-app-active-int/heartbeat' },
    { 'name': 'Kraken Cld', 'url': 'pw-non-krakencld-app-active-int/heartbeat' },
    { 'name': 'Basket Api', 'url': 'pw-non-basketapi-app-active-ext/heartbeat' },
    { 'name': 'Clipper', 'url': 'pe-non-clppravlblsvc-app-active-int/AvailabilityService/api/heartbeat' },
    { 'name': 'AutoTech Njs', 'url': 'pw-non-autotech-njs-active-ext/heartbeat' },
    { 'name': 'Config Read', 'url': 'pw-non-cfgread-app-active-int/heartbeat' },
    { 'name': 'Bundle and save app', 'url': 'pw-non-ofrsvapi-app-active-int/heartbeat' },
    { 'name': 'Cuso Web', 'url': 'pw-non-cusoweb-njs-active-ext/heartbeat' },
    { 'name': 'Case Graph', 'url': 'pw-non-casegraph-app-active-int/heartbeat' },
    { 'name': 'Customer Agreements(cstagraph)', 'url': 'pw-rpi-cstagrgph-app-active-int/heartbeat' },
    { 'name': 'cia', 'url': 'pw-rpi-cia-app-active-ext/heartbeat' },
    { 'name': 'Digital Gateway', 'url': 'pw-3rd-dagatwy-app-active-ext/heartbeat' },
    { 'name': 'Digital Orchestrator', 'url': 'pw-3rd-dgtassorc-app-active-int/heartbeat' },
    { 'name': 'Expert Review', 'url': 'pw-non-excnexrvw-app-active-int/heartbeat' },
    { 'name': 'Dossier-Njs', 'url': 'pw-non-dossier-njs-active-ext/heartbeat' },
    { 'name': 'Dossier-App', 'url': 'pw-non-dossier-app-active-int/heartbeat' },
    { 'name': 'Exc-Ecorebates', 'url': 'pw-non-ecorbates-app-active-int/heartbeat' },
    { 'name': 'FulFillment-View', 'url': 'pw-non-fulfview-njs-active-ext/heartbeat' },
    { 'name': 'Exc Video Domain Service', 'url': 'pw-non-excvmds-app-active-int/heartbeat' },
    { 'name': 'fireview-njs', 'url': 'pw-non-fireview-njs-active-int/heartbeat' },
    { 'name': 'FTS', 'url': 'pw-rpi-fts-app-active-int/heartbeat' },
    { 'name': 'GeekTriage', 'url': 'pw-non-geektriage-app-active-int/heartbeat' },
    { 'name': 'GeekSquad Cloud', 'url': 'pw-non-geeksqcld-app-active-ext/heartbeat' },
    { 'name': 'Group Scheduling', 'url': 'pw-non-groupsch-app-active-ext/heartbeat' },
    { 'name': 'gsinstsch', 'url': 'pw-rpi-gsinstsch-app-active-ext/heartbeat' },
    { 'name': 'Ignite-Njs', 'url': 'pw-bro-ignite-njs-active-ext/heartbeat' },
    { 'name': 'Ihaols', 'url': 'pw-rpi-ihaols-app-active-ext/heartbeat' },
    { 'name': 'Ihasched', 'url': 'pw-rpi-ihasched-app-active-int/heartbeat' },
    { 'name': 'Inspireview', 'url': 'pw-non-inspireview-njs-active-int/heartbeat' },
    { 'name': 'ISPU', 'url': 'pw-non-ispu-app-active-ext/fulfillment/ispu/api/heartbeat' },
    { 'name': 'Shipping', 'url': 'pw-non-shipping-app-active-int/fulfillment/shipping/api/heartbeat' },
    { 'name': 'Price View Njs', 'url': 'pw-bro-priceview-njs-active-int/heartbeat' },
    { 'name': 'Pixie App', 'url': 'pw-non-pixie-app-active-int/heartbeat' },
    { 'name': 'Platview Njs', 'url': 'pw-non-platview-njs-active-int/heartbeat' },
    { 'name': 'Payment', 'url': 'pw-cde-paymntagg-app-active-ext/heartbeat' },
    { 'name': 'PDM Mapper', 'url': 'pw-non-pdmmapper-app-active-int/heartbeat' },
    #{ 'name': 'PDM Portal', 'url': 'pw-non-pdmportal-app-active-ext/heartbeat' },
    { 'name': 'PDM Validator', 'url': 'pw-non-pdmvalidator-app-active-int/heartbeat' },
    { 'name': 'PDM Consumer', 'url': 'pw-non-pdmcnsmer-app-active-int/heartbeat' },
    { 'name': 'PDM Ingest', 'url': 'pw-non-pdmingest-app-active-int/heartbeat' },
    { 'name': 'PDM Publisher', 'url': 'pw-non-pdmpblshr-app-active-int/heartbeat' },
    { 'name': 'PDM Processor', 'url': 'pw-non-pdmprcssr-app-active-int/heartbeat' },
    { 'name': 'Resource Server(New VPC)', 'url': 'pw-non-rsrsrvcld-app-active-int/heartbeat' },
    { 'name': 'Kuffs', 'url': 'pw-non-kuffs-app-active-int/heartbeat' },
    { 'name': 'Plprofile', 'url': 'pw-non-plprofile-njs-active-ext/heartbeat' },
    { 'name': 'Plprofile-app', 'url': 'pw-non-plprofile-app-active-int/heartbeat' },
    { 'name': 'Location', 'url': 'pw-browse-location-active-int/location/heartbeat' },
    { 'name': 'List', 'url': 'pw-non-lstsrvces-app-active-ext/heartbeat' },
    { 'name': 'Mag-Delta', 'url': 'pw-non-magdelta-app-active-int/heartbeat' },
    { 'name': 'Device Graph Njs', 'url': 'pw-non-dvcgraph-njs-active-int/heartbeat' },
    { 'name': 'Mexico-Web', 'url': 'pw-mex-mexico-web-active-int/heartbeat' },
    { 'name': 'Mexico Njs', 'url': 'pw-mex-mexico-njs-active-int/heartbeat' },
    { 'name': 'Mobview-njs', 'url': 'pw-non-mobview-njs-active-int/heartbeat' },
    { 'name': 'Service Interceptor(Naif)', 'url': 'pw-non-naifweb-app-active-int/heartbeat' },
    { 'name': 'NhanceView-njs', 'url': 'pw-non-nhancview-njs-active-int/heartbeat' },
    { 'name': 'Browse NodeJs', 'url': 'pw-browse-nodejs-active-int/heartbeat' },
    { 'name': 'Pisces(Orville)', 'url': 'pw-non-orville-app-active-ext/heartbeat' },
    { 'name': 'PLP View Njs', 'url': 'pw-non-plpview-njs-active-int/heartbeat' },
    { 'name': 'SCDS-API', 'url': 'pw-non-scdsapi-app-active-int/heartbeat' },
    { 'name': 'OCPG', 'url': 'pw-rpi-ocpg-app-active-int/heartbeat' },
    { 'name': 'Order Graph', 'url': 'pw-rpi-ordrgraph-app-active-int/heartbeat' },
    { 'name': 'Psychic-app', 'url': 'pw-non-psychic-app-active-int/heartbeat' },
    { 'name': 'STS Internal', 'url': 'pw-non-sctksrint-app-active-int/heartbeat' },
    { 'name': 'Search-Api', 'url': 'pw-non-searchapi-app-active-int/heartbeat' },
    { 'name': 'sercalendar', 'url': 'pw-non-sercalendar-app-active-int/heartbeat' },
    { 'name': 'Suggest Api', 'url': 'pw-non-sggestapi-app-active-int/heartbeat' },
    { 'name': 'Service Interceptor DeltaCache(SIDCS)', 'url': 'pw-non-sidcs-app-active-int/heartbeat' },
    { 'name': 'Solar Index Agent', 'url': 'pw-bro-solrindex-svc-active-int/heartbeat' },
    { 'name': 'Solrindex-app', 'url': 'pw-non-solrindex-app-active-int/heartbeat' },
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
    { 'name': 'UGC Api', 'url': 'pw-non-ugcapi-app-active-int/heartbeat' },
    { 'name': 'Pricing-Services-Aggregator', 'url': 'pw-non-priceragg-app-active-ext/heartbeat' },
    { 'name': 'Pricing Services Engine', 'url': 'pw-non-pricereng-app-active-int/heartbeat' },
    { 'name': 'UGC-Njs', 'url': 'pw-bro-ugc-njs-active-int/heartbeat' },
    { 'name': 'Widget View', 'url': 'pw-non-widgetview-njs-active-int/heartbeat' },
    { 'name': 'UCR', 'url': 'pw-non-usrclasres-app-active-int/heartbeat' },
    { 'name': 'Visitor Graph', 'url': 'pw-bro-vgraph-api-active-int/heartbeat' },
    { 'name': 'ZK Agent', 'url': 'pw-bro-zkagent-svc-active-int/zk-agent/heartbeat' },
    { 'name': 'Product Fulfillment(Profulfil)', 'url': 'pw-bro-profulfil-web-active-ext/productfulfillment/heartbeat' },
    #{ 'name': 'CSI', 'url': 'pw-csi-web-active-ext/api/csiservice/heartbeat'},
    { 'name': 'Customer-Graph', 'url': 'pw-rpi-cgraph-app-active-int/heartbeat'},
    { 'name': 'Purchase Finder', 'url': 'pw-non-prchsfndr-app-active-ext/heartbeat'},
    { 'name': 'Psychic App', 'url': 'pw-non-psychic-app-active-int/heartbeat'},
    { 'name': 'RNRView App', 'url': 'pw-non-rnrview-njs-active-int/heartbeat'},
    { 'name': 'TTSgifting-app', 'url': 'pw-cde-ttsgifting-app-active-int/heartbeat'},
    { 'name': 'TTSgifting-Njs', 'url': 'pw-cde-ttsgifting-njs-active-ext/heartbeat'},
    { 'name': 'TRS', 'url': 'pw-non-trnrsksrv-app-active-int/heartbeat'},
    { 'name': 'Product Fulfillment(Profulfil)', 'url': 'pw-bro-profulfil-web-active-ext/productfulfillment/heartbeat' }
    ]



west_status = [
  { 'name': 'Plunger', 'url': 'pw-browse-plunger-active-ext/plunger/health_check' }
 ]



west_cargo = [
 { 'name': 'cargo-app', 'url': 'pw-bro-cargo-api-active-int/shipping-webapp/api/heartbeat' },
 { 'name': 'CBA', 'url': 'pe-browse-web-vpc-active-int/heartbeat' },
 { 'name': 'Panda', 'url': 'pw-browse-panda-active-ext/heartbeat' }
]

west_scp = [
 { 'name': 'exc-slr', 'url': 'pw-non-exc-slr-active-int/solr/admin/info/properties?wt=json' },
 { 'name': 'recs-slr', 'url': 'pw-non-recs-slr-active-int/solr/admin/info/properties?wt=json' },
 { 'name': 'search-slr', 'url': 'pw-non-search-slr-active-int/solr/admin/info/properties?wt=json' },
 { 'name': 'UGC-slr', 'url': 'pw-bro-ugc-slr-active-int/solr/admin/info/properties?wt=json' },
 { 'name': 'VPT-slr', 'url': 'pw-non-vpt-slr-active-int/solr/admin/info/properties?wt=json' },
 { 'name': 'Suggestcld-slr', 'url': 'pw-non-sggestcld-slr-active-int/solr/admin/info/properties?wt=json' }
]

def curl_version(data):
    response = requests.post('https://dashboard-service-canaryautomation-canary.omnitank.bestbuy.com/dashboardservice/data/prodheartbeat', data=data)
    jdata = json.loads(response.text)
    return (jdata['applicationVersion'])


def curl_version2(data):
    response = requests.post('https://dashboard-service-canaryautomation-canary.omnitank.bestbuy.com/dashboardservice/data/prodheartbeat', data=data)
    # print (response.text)
    jdata = json.loads(response.text)
    # print (jdata)
    return (jdata['version'])


def curl_version4(data):
    response = requests.post('https://dashboard-service-canaryautomation-canary.omnitank.bestbuy.com/dashboardservice/data/prodheartbeat', data=data)
    return (response.text)
    # jdata = json.loads(response.text)
    # print (jdata)
    # return (jdata['Cargo-Shipping Version'])

def curl_version5(data):
    response = requests.post('https://dashboard-service-canaryautomation-canary.omnitank.bestbuy.com/dashboardservice/data/prodheartbeat', data=data)
    # print (response.text)
    jdata = json.loads(response.text)
    next = jdata.get("system.properties")
    return (next['bby.scp.version'])

def curl_version6(data):
    response = requests.post('https://dashboard-service-canaryautomation-canary.omnitank.bestbuy.com/dashboardservice/data/prodheartbeat', data=data)
        # print (response.text)
    jdata = json.loads(response.text)
    next = jdata.get("status")
    return (next['version'])


def send_status_to_hipchat(message,color):
    room_id_real = sys.argv[1]
    auth_token_real = sys.argv[2]
    url = 'https://hipchat.bestbuy.com/v2/room/'+room_id_real+'/notification'
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
                         # print (each, (curl_version(data1[each])), (curl_version(data2[each1])))
                        print (each + " east version is " + (curl_version(data1['each'])) + " and west version is " + (curl_version(each1['url'])))
                        count += 1
                        send_status_to_hipchat(each['name'] + " east version is " + (curl_version(data['each'])) + " and west version is " + (curl_version(data2['each1'])), "red")


for each in east_cargo:
    for each1 in west_cargo:
        if (each['name']) == (each1['name']):
            if (curl_version4(each['url'])) == (curl_version4(each1['url'])):
                print (each['name'], (curl_version4(each['url'])))
            else:
                # print ("versions are not same")
                print (each['name'] + " east version is " + (curl_version4(each['url'])) + " and west version is " + (curl_version4(each1['url'])))
                count += 1
                send_status_to_hipchat(each['name'] + " east version is " + (curl_version4(each['url'])) + " and west version is " + (curl_version4(each1['url'])), "red")


for each in east_scp:
    for each1 in west_scp:
        if (each['name']) == (each1['name']):
            if (curl_version5(each['url'])) == (curl_version5(each1['url'])):
                print (each['name'], (curl_version5(each['url'])))
            else:
                # print ("versions are not same")
                print (each['name'] + " east version is " + (curl_version5(each['url'])) + " and west version is " + (curl_version5(each1['url'])))
                count += 1
                send_status_to_hipchat(each['name'] + " east version is " + (curl_version5(each['url'])) + " and west version is " + (curl_version5(each1['url'])), "red")

for each in east_status:
    for each1 in west_status:
        if (each['name']) == (each1['name']):
            if (curl_version6(each['url'])) == (curl_version6(each1['url'])):
                print (each['name'], (curl_version6(each['url'])))
            else:
                # print ("versions are not same")
                print (each['name'] + " east version is " + (curl_version6(each['url'])) + " and west version is " + (curl_version6(each1['url'])))
                count += 1
                send_status_to_hipchat(each['name'] + " east version is " + (curl_version6(each['url'])) + " and west version is " + (curl_version6(each1['url'])), "red")

if count == 0:
    print ("all good")
    send_status_to_hipchat("All Application versions are consistent in East and West","green")
