# -*- coding: utf-8 -*-
import json
import mysql.connector
import time

connBDD = mysql.connector.connect(host="localhost", user="root", password="delfis", database="delfis")
cursor = connBDD.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS usr_30(
    id varchar(20) NOT NULL,
    latitude decimal(10,8) NOT NULL,
    longitude decimal(10,8) NOT NULL
)ENGINE = MEMORY;
""")

lat = 10.0001
lng = 5.0001
i=0
dept = 30
timedebut  = time.time()

while i < 100  :

    time1 = time.time()

    cursor.execute('INSERT INTO usr_'+dept+' (id,latitude,longitude)\
    VALUES ("test", "'+ str(lat)+'" , "'+str(lng)+'" );')
    connBDD.commit()

    time2 = time.time()

    print("insert OK en : " + time2 - time1 +"ms")

    lat += 0.0002
    lng += 0.0002
    i += 1
    time.sleep(1)

timefin = time.time()
print("Temps d'execution total : " + timefin - timedebut + " ms")

connBDD.close
