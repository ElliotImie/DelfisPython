# -*- coding: utf-8 -*-
import json
import mysql.connector
import time
import script_velo

id_user = 1
lat = 10.000
lng = 50.000

connBDD = mysql.connector.connect(host="localhost", user="root", password="delfis", database="delfis")
cursor = connBDD.cursor()

i=1000
timedebut  = time.time()

while i < 1000 :

    jsonTestDict = {"id_user" : str(id_user), "latitude" : lat, "longitude" : lng, "dept" : "34"}
    jsonTest = json.dumps(jsonTestDict)

    script_velo.main(jsonTest)

    id_user +=1
    lat += 0.0003
    lng += 0.0003

    i += 1

timefin = time.time()
print("Temps d'execution total : " + str( timefin - timedebut) + " ms")

connBDD.close
