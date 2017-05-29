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
)ENGINE=InnoDB;
""")

i=0

timedebut  = time.time()

while i < 100000 :
    time1 = time.time()

#Pour Bench insert :
    cursor.execute('INSERT INTO usr_32 (id,latitude,longitude) VALUES ("test", "10.0001" , " 5.0001");')
    connBDD.commit()

    time2 = time.time()

    print("insert OK en : " + str(time2 - time1) +"sec")

    i += 1

timefin = time.time()
print("Temps d'execution total : " + str( timefin - timedebut) + " s")

connBDD.close
