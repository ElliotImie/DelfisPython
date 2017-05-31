# -*- coding: utf-8 -*-
import json
import mysql.connector
import time

connBDD = mysql.connector.connect(host="localhost", user="root", password="delfis", database="delfis")
cursor = connBDD.cursor()

#Pour bench insert
cursor.execute("""
    CREATE TABLE IF NOT EXISTS usr_01(
    id varchar(20) NOT NULL,
    latitude decimal(10,8) NOT NULL,
    longitude decimal(10,8) NOT NULL
)ENGINE=MEMORY;
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS usr_02(
    id varchar(20) NOT NULL,
    latitude decimal(10,8) NOT NULL,
    longitude decimal(10,8) NOT NULL
)ENGINE=MEMORY;
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS usr_03(
    id varchar(20) NOT NULL,
    latitude decimal(10,8) NOT NULL,
    longitude decimal(10,8) NOT NULL
)ENGINE=MEMORY;
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS usr_04(
    id varchar(20) NOT NULL,
    latitude decimal(10,8) NOT NULL,
    longitude decimal(10,8) NOT NULL
)ENGINE=MEMORY;
""")

i=0

timedebut  = time.time()

while i < 1 :
    time1 = time.time()

#Pour Bench insert :
    cursor.execute('INSERT INTO usr_01 (id,latitude,longitude) VALUES ("velo0", "0.0" , " 0.0");')
    connBDD.commit()

    cursor.execute('INSERT INTO usr_02 (id,latitude,longitude) VALUES ("velo1", "0.0" , " 0.0");')
    cursor.execute('INSERT INTO usr_02 (id,latitude,longitude) VALUES ("velo2", "0.0" , " 0.0");')
    cursor.execute('INSERT INTO usr_02 (id,latitude,longitude) VALUES ("velo3", "0.0" , " 0.0");')
    cursor.execute('INSERT INTO usr_02 (id,latitude,longitude) VALUES ("velo4", "0.0" , " 0.0");')
    cursor.execute('INSERT INTO usr_02 (id,latitude,longitude) VALUES ("velo5", "0.0" , " 0.0");')
    connBDD.commit()

    cursor.execute('INSERT INTO usr_03 (id,latitude,longitude) VALUES ("velo0", "0.003" , " 0.0");')
    connBDD.commit()

    cursor.execute('INSERT INTO usr_04 (id,latitude,longitude) VALUES ("velo0", "0.0" , " 0.0");')
    cursor.execute('INSERT INTO usr_04 (id,latitude,longitude) VALUES ("velo1", "0.0" , " 0.0");')
    cursor.execute('INSERT INTO usr_04 (id,latitude,longitude) VALUES ("velo2", "0.0" , " 0.0");')
    cursor.execute('INSERT INTO usr_04 (id,latitude,longitude) VALUES ("velo3", "0.0" , " 0.0");')
    cursor.execute('INSERT INTO usr_04 (id,latitude,longitude) VALUES ("velo4", "0.0" , " 0.0");')

    cursor.execute('INSERT INTO usr_04 (id,latitude,longitude) VALUES ("velo0", "0.003" , " 0.0");')
    cursor.execute('INSERT INTO usr_04 (id,latitude,longitude) VALUES ("velo1", "0.003" , " 0.0");')
    cursor.execute('INSERT INTO usr_04 (id,latitude,longitude) VALUES ("velo2", "0.003" , " 0.0");')
    cursor.execute('INSERT INTO usr_04 (id,latitude,longitude) VALUES ("velo3", "0.003" , " 0.0");')
    cursor.execute('INSERT INTO usr_04 (id,latitude,longitude) VALUES ("velo4", "0.003" , " 0.0");')


    connBDD.commit()

    time2 = time.time()

    print("insert OK en : " + str(time2 - time1) +"sec")

    i += 1

timefin = time.time()
print("Temps d'execution total : " + str( timefin - timedebut) + " s")

connBDD.close
