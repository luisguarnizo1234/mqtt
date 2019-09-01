import sqlite3

# SQLite DB Name
DB_Name =  "/home/gonzalo/Desktop/MQTT/datos.db"

#Connect or Create DB File

conexion = sqlite3.connect(DB_Name)
cursor = conexion.cursor()

# SQLite DB Table Schema
sql1="""

CREATE TABLE IF NOT EXISTS tabla1 (
  id INTEGER PRIMARY KEY,
  nodo_id text,
  ssid text,
  rssi int,
  canal int,
  bit_rate int,
  fecha text
)

"""


#Create Tables
sql2= """DROP TABLE IF EXISTS tabla1"""

# SQLite DB Table Schema
sql3="""

CREATE TABLE IF NOT EXISTS tabla2 (
  id INTEGER PRIMARY KEY,
  nodo_id text,
  ssid text,
  rssi int,
  canal int,
  bit_rate int,
  fecha text
)

"""


#Create Tables
sql4= """DROP TABLE IF EXISTS tabla2"""



sql5="""

CREATE TABLE IF NOT EXISTS tabla3 (
  id INTEGER PRIMARY KEY,
  nodo_id text,
  ssid text,
  rssi int,
  canal int,
  bit_rate int,
  fecha text
)

"""


#Create Tables
sql6= """DROP TABLE IF EXISTS tabla3"""



sql7="""

CREATE TABLE IF NOT EXISTS tabla4 (
  id INTEGER PRIMARY KEY,
  nodo_id text,
  ssid text,
  rssi int,
  canal int,
  bit_rate int,
  fecha text
)

"""


#Create Tables
sql8= """DROP TABLE IF EXISTS tabla4"""

#primero se borra la tabla si existe, sino se crea
cursor.execute(sql2)#borra
cursor.execute(sql1)#crea

cursor.execute(sql4)
cursor.execute(sql3)

cursor.execute(sql6)
cursor.execute(sql5)

cursor.execute(sql8)
cursor.execute(sql7)


#Close DB
cursor.close()
conexion.close()
 
