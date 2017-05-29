# -*- coding: utf-8 -*-
import json
import mysql.connector
import time

connBDD = mysql.connector.connect(host="localhost", user="root", password="delfis", database="delfis")
cursor = connBDD.cursor()

#Pour bench insert
cursor.execute("""
    CREATE TABLE IF NOT EXISTS usr_32(
    id varchar(20) NOT NULL,
    latitude decimal(10,8) NOT NULL,
    longitude decimal(10,8) NOT NULL
);
""")

lat = 10.0001
lng = 5.0001
i=0
dept = 32

timedebut  = time.time()

while i < 100 :
    time1 = time.time()

#Pour Bench insert :
    cursor.execute('INSERT INTO usr_'+str(dept)+'(id,latitude,longitude) VALUES ("test",'+ str(lat)+' , '+str(lng)+');')
    connBDD.commit()

    time2 = time.time()

    print("insert OK en : " + str(time2 - time1) +"sec")

#Pour bench insert
    lat += 0.0003
    lng += 0.0003
    i += 1

timefin = time.time()
print("Temps d'execution total : " + str( timefin - timedebut) + " s")

connBDD.close
