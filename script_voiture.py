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

# degre de précision voulu : 100m,
# +0.001 > lat > -0.001

import sys
import json
import mysql.connector


def main (arg):
    message = json.loads(arg)

    dept = message["dept"]
    lat = message["latitude"]
    lng = message["longitude"]

    zoneCourte = message["zoneCourte"]
    zoneLongue = message["zoneLongue"]

    #Récupère la précision du signal gps de la voiture.
    #Pour limiter les incertitudes on ajoute cette précision au rayon de recherche de vélo.
    #Par exemple, pour une voiture en milieu urbain ( zone large : 250m, zone courte : 50m ),
    #   si la précision du gps de la voiture est de 30m, on élargie la zone large a 280m et zone courte a 80m
    precision = message["precision"]
    precision = precision / 2

    if(precision > 100):
        precision = 0

    precisionCourte = (zoneCourte * 0.00001) + (precision * 0.00001)
    precisionLongue = (zoneLongue * 0.00001) + (precision * 0.00001)

    conn = mysql.connector.connect(host="localhost", user="root", password="delfis", database="delfis")
    cursor = conn.cursor()

    lat_large_max = str(lat + precisionLongue)
    lat_large_min = str(lat - precisionLongue)
    lat_short_max = str(lat + precisionCourte)
    lat_short_min = str(lat - precisionCourte)

    lng_large_max = str(lng + precisionLongue)
    lng_large_min = str(lng - precisionLongue)
    lng_short_max = str(lng + precisionCourte)
    lng_short_min = str(lng - precisionCourte)

    requete_large = 'SELECT count(id) as nbVelo FROM usr_'+dept+'\
    WHERE latitude BETWEEN "'+ lat_large_min+'" AND "'+ lat_large_max +'" \
        AND longitude BETWEEN "'+ lng_large_min +'" AND "'+ lng_large_max +'" ;'

    requete_short = 'SELECT count(id) as nbVelo FROM usr_'+dept+'\
    WHERE latitude BETWEEN "'+ lat_short_min+'" AND "'+ lat_short_max +'" \
        AND longitude BETWEEN "'+ lng_short_min +'" AND "'+ lng_short_max +'" ;'

    cursor.execute(requete_large)
    dataSet = cursor.fetchall()
    fields = cursor.description

    i=0
    j=0
    result_large ={}
    for data in dataSet:
        i=0
        for field in fields:
            if i<data.__len__():
                result_large[field[0]]=str(data[i])
                i+=1

    cursor.execute(requete_short)
    dataSet = cursor.fetchall()
    fields = cursor.description

    i=0
    j=0
    result_min ={}
    for data in dataSet:
        i=0
        for field in fields:
            if i<data.__len__():
                result_min[field[0]]=str(data[i])
                i+=1

    jsonRep = '{ "nbVeloZoneLarge" : '+ str(int(result_large["nbVelo"])-int(result_min["nbVelo"])) +', "nbVeloZoneCourte" : '+ result_min["nbVelo"] +' }'

    conn.close

    return jsonRep


if __name__ == "__main__":

    main(sys.argv[1])
