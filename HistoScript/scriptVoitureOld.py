# -*- coding: utf-8 -*-

#table correspondance degre gps, précision :
#source : https://en.wikipedia.org/wiki/Decimal_degrees
# decimal
# places   degrees          distance
# -------  -------          --------
# 0        1                111  km
# 1        0.1              11.1 km
# 2        0.01             1.11 km
# 3        0.001            111  m
# 4        0.0001           11.1 m
# 5        0.00001          1.11 m
# 6        0.000001         11.1 cm
# 7        0.0000001        1.11 cm
# 8        0.00000001       1.11 mm

import sys
import json
import mysql.connector

def main (arg):
    print(arg)
    message = json.loads(arg)
    print(message)

    dept = message["dept"]
    id_user = message["id_user"]
    lat = message["latitude"]
    lng = message["longitude"]
    mode = message["mode"]

    print(dept)
    print (id_user)
    print (lat)
    print (lng)
    print (mode)


    conn = mysql.connector.connect(host="localhost", user="root", password="root", database="delfis")
    cursor = conn.cursor()
    print("connection OK")

    # cursor.execute("""
    # 	CREATE TABLE IF NOT EXISTS usr_"""+dept+"""(
    # 	id varchar(20) NOT NULL,
    # 	latitude varchar(10) NOT NULL,
    # 	longitude varchar(10) NOT NULL
    # );
    # """)

    cursor.execute('SELECT count(id) as nbVelo FROM usr_'+dept+' WHERE latitude BETWEEN "42.1235" AND "42.1236" ;')
    dataSet = cursor.fetchall()
    fields = cursor.description
    print (fields)
    i=0
    j=0
    result={}
    # resultSet={}
    for data in dataSet:
            i=0
            for field in fields:
                    if i<data.__len__():
                            result[field[0]]=str(data[i])
                            i+=1
            # resultSet[j] = result.copy()
            # j+=1
    print (result["nbVelo"])

    return result["nbVelo"]
    # print fields
    #
    # conn.commit()
    # print("insert OK")

    conn.close


if __name__ == "__main__":

    main(sys.argv[1])
    # sys.argv[1] --> String au format json
        # {"id_user":string de 15 caractères, "latitude":string de X caractère , "longitude":string de X caractère,"dept": string de 2caractère,"mode": rural/urbain}


        #    self.cursor.execute(query)
        #         dataSet=self.cursor.fetchall()
        #         fields=self.cursor.description
        #         i=0
        #         j=0
        #         result={}
        #         resultSet={}
        #         for data in dataSet:
        #                 i=0
        #                 for field in fields:
        #                         if i<data.__len__():
        #                                 result[field[0]]=str(data[i])
        #                                 i+=1
        #                 resultSet[j] = result.copy()
        #                 j+=1
        #         return resultSet
