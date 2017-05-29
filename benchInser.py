# -*- coding: utf-8 -*-
import json
import mysql.connector
import time
import script_velo


connBDD = mysql.connector.connect(host="localhost", user="root", password="delfis", database="delfis")
cursor = connBDD.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS usr_32(
    id varchar(20) NOT NULL,
    latitude decimal(10,8) NOT NULL,
    longitude decimal(10,8) NOT NULL
)ENGINE= MEMORY;
""")

lat = 10.0001
lng = 5.0001
i=0
dept = 32
jsonTestDict = {"id_user" : "testBenchVelo2", "latitude" : 11.111, "longitude" : 22.2222, "dept" : "32"}
jsonTest = json.dumps(jsonTestDict)

timedebut  = time.time()

while i < 10 :
    time1 = time.time()

#Pour Bench insert :
    # cursor.execute('INSERT INTO usr_'+str(dept)+'(id,latitude,longitude) VALUES ("test",'+ str(lat)+' , '+str(lng)+');')
    # connBDD.commit()

#Pour bench script_velo :
    script_velo.main(jsonTest)

    time2 = time.time()

    print("insert OK en : " + str(time2 - time1) +"sec")

    lat += 0.0002
    lng += 0.0002
    i += 1
    #time.sleep(1)

timefin = time.time()
print("Temps d'execution total : " + str( timefin - timedebut) + " ms")

connBDD.close
