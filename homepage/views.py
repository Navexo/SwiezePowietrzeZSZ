from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
def ochrona(request):
    return render(request, "ochrona_srodowiska.html")
def homepage(request):
    stations = requests.get("https://api.gios.gov.pl/pjp-api/rest/station/findAll").json()
    dataDictionary = {
        "stations": stations
    }
    dataJSON = json.dumps(dataDictionary)
    return render(request, "index.html", {"data": dataJSON})
def homepageid(request, id):
    stations = requests.get("https://api.gios.gov.pl/pjp-api/rest/station/findAll").json()
    station = requests.get("https://api.gios.gov.pl/pjp-api/rest/aqindex/getIndex/"+str(id)).json()
    for s in stations:
        if s['id']==id:
            city = s["stationName"]
    dataDictionary = {
        "stations": station,
        "city": city,
    }
    dataJSON = json.dumps(dataDictionary)
    return render(request, "home.html", {"data": dataJSON})
#    {
#        'id': 296,
#        'stationName': 'Łódź, ul. Gdańska', 
#        'gegrLat': '51.775411', 
#        'gegrLon': '19.450900', 
#        'city': {'id': 516, 
#            'name': 'Łódź', 
#            'commune': {'communeName': 'Łódź', 
#                'districtName': 'Łódź', 
#                'provinceName': 'ŁÓDZKIE'}},
#        'addressStreet': 'ul. Gdańska 16'},