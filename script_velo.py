# -*- coding: utf-8 -*-

import sys
import json
import mysql.connector

def main (arg):
    message = json.loads(arg)

    dept = message["dept"]
    id_user = message["id_user"]
    lat = message["latitude"]
    lng = message["longitude"]

    conn = mysql.connector.connect(host="localhost", user="root", password="delfis", database="delfis")
    cursor = conn.cursor()

    cursor.execute("""
    	CREATE TABLE IF NOT EXISTS usr_"""+dept+"""(
    	id varchar(20) NOT NULL,
    	latitude decimal(10,8) NOT NULL,
    	longitude decimal(10,8) NOT NULL
    )ENGINE=MEMORY;
    """)

    reqDel = 'DELETE FROM usr_'+dept+' WHERE id like "'+ id_user +'" ; '
    cursor.execute(reqDel)

    cursor.execute('INSERT INTO usr_'+dept+' (id,latitude,longitude) VALUES ("'+id_user+'", "'+str(lat)+'" , "'+str(lng)+'" );')

    conn.close


if __name__ == "__main__":

    main(sys.argv[1])
