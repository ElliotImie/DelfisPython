# -*- coding: utf-8 -*-
import json
import mysql.connector
import time
import script_velo


connBDD = mysql.connector.connect(host="localhost", user="root", password="delfis", database="delfis")
cursor = connBDD.cursor()

jsonTestDict = {"id_user" : "testBenchVelo2", "latitude" : 11.111, "longitude" : 22.2222, "dept" : "32"}
jsonTest = json.dumps(jsonTestDict)

i=0
timedebut  = time.time()

while i < 100 :
    time1 = time.time()


#Pour bench script_velo :
    script_velo.main(jsonTest)

    time2 = time.time()

    print("insert OK en : " + str(time2 - time1) +"sec")

    i += 1

timefin = time.time()
print("Temps d'execution total : " + str( timefin - timedebut) + " ms")

connBDD.close
