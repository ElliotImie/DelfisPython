import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", password="root", database="delfis")
cursor = conn.cursor()
print("connection OK")



cursor.execute("""
	CREATE TABLE IF NOT EXISTS usr_49(
	id varchar(20) NOT NULL,
	latitude varchar(10) NOT NULL,
	longitude varchar(10) NOT NULL
);
""")


cursor.execute("""INSERT INTO usr_49 (id,latitude,longitude) VALUES ("android-123456789012","lat1234567","lon0123456");""")
cursor.execute("""INSERT INTO usr_49 (id,latitude,longitude) VALUES ("android-123456789013","lat1234567","lon0123456");""")
cursor.execute("""INSERT INTO usr_49 (id,latitude,longitude) VALUES ("android-123456789014","lat1234567","lon0123456");""")

conn.commit()
print("insert OK")

conn.close
