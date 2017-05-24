# -*- coding: utf-8 -*-

import sys
import json
import mysql.connector

def main (arg):
    print arg
    message = json.loads(arg)
    print message

    dept = message["dept"]
    id_user = message["id_user"]
    lat = message["latitude"]
    lng = message["longitude"]

    print dept
    print id_user
    print lat
    print lng


    conn = mysql.connector.connect(host="localhost", user="root", password="delfis", database="delfis")
    cursor = conn.cursor()
    print("connection OK")

    cursor.execute("""
    	CREATE TABLE IF NOT EXISTS usr_"""+dept+"""(
    	id varchar(20) NOT NULL,
    	latitude decimal(10,8) NOT NULL,
    	longitude decimal(10,8) NOT NULL
    )ENGINE = MEMORY;
    """)

    cursor.execute('INSERT INTO usr_'+dept+' (id,latitude,longitude) VALUES ("'+id_user+'", "'+lat+'" , "'+lng+'" );')

    conn.commit()
    print("insert OK")

    conn.close


if __name__ == "__main__":

    main(sys.argv[1])
    # sys.argv[1] --> String au format json
        # {"id_user":string de 15 caractères, "latitude":string de X caractère , "longitude":string de X caractère,"dept": string de 2caractère}

