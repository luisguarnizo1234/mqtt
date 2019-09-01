import json
import sqlite3
from heatmap import graficar
from datetime import datetime
import matplotlib.pyplot as plt

# SQLite DB Name
DB_Name =  "/home/gonzalo/Desktop/MQTT/datos.db"
#===============================================================
# Database Manager Class
n1=1
n2=1
n3=1
n4=1

y1=1
y2=1
y3=1
y4=1
class DatabaseManager():
	def __init__(self):
		self.conexion = sqlite3.connect(DB_Name)
		self.conexion.execute('pragma foreign_keys = on')
		self.conexion.commit()
		self.cursor = self.conexion.cursor()
		
	def add_del_update_db_record(self, sql_query, args=()):
		self.cursor.execute(sql_query, args)
		self.conexion.commit()
		return

	def __del__(self):
		self.cursor.close()
		self.conexion.close()

#===================================================================
#Metodo para consultar datos		
	def consulta(self, sql_query):
		self.cursor.execute(sql_query)
		
		#resultado = self.cursor.fetchall()
		#print(resultado)
		row= self.cursor.fetchall()
		print row[0]
		for filas in row:
			print(filas)
		tamano = len(row) - 1
		print(tamano)
		dato = row[tamano]
		print "el ultimo dato fue:"
		print(dato)
		self.conexion.commit()
		return(dato)
		

#=================================================s==============
# Functions to push Sensor Data into Database

# Function to save Temperature to DB Table
	
	
def data_Handler1(jsonData):
	print "topic nodo1"
	
	#Parse Data 
	query = json.loads(jsonData)
	
	nodoid = query["nodo_id"]
	id = float(nodoid)
	y1 = query["rssi"]
	y2 = float(y1)
	#heatmap	
	#graficar(n1, n2, n3, n4)
	
	
	nodoid = query["nodo_id"]
	SSID = query["ssid"]
	RSSI = query["rssi"]
	CANAL = query["canal"]
	Bit_rate = query["bit_rate"]
	FECHA = (datetime.today()).strftime("%d-%b-%Y %H:%M:%S:%f")
	print(FECHA)
	
	#Data_and_Time = json_Dict['Date']	
	#Push into DB Table
	dbObj = DatabaseManager()
	dbObj.add_del_update_db_record("insert into tabla1 (nodo_id, ssid, rssi, canal, bit_rate, fecha) values (?,?,?,?,?,?)",[nodoid, SSID, RSSI, CANAL, Bit_rate, FECHA])
	print "Inserted Temperature Data into Database."
	y1 = dbObj.consulta("select rssi from tabla1")
	y2 = dbObj.consulta("select rssi from tabla2")
	y3 = dbObj.consulta("select rssi from tabla3")
	y4 = dbObj.consulta("select rssi from tabla4")
	print "rssi nodo 1:"
	print (y1) 
	print "rssi nodo 2:"
	print (y2) 
	print "rssi nodo 3:"
	print (y3) 
	print "rssi nodo 4:"
	print (y4) 
	print"eso es todo"

	graficar(y1, y2, y3, y4)	
	#dbObj.consulta("select id from tabla1")
	#print(resultado)
	del dbObj
	print ""
	
#=================================================================
#guardar datos del nodo2
def data_Handler2(jsonData):
	print "topic nodo2"
	
	#Parse Data 
	query = json.loads(jsonData)
	#heatmap	
	#graficar(n1, n2, n3, n4)
	
	nodoid = query["nodo_id"]
	SSID = query["ssid"]
	RSSI = query["rssi"]
	CANAL = query["canal"]
	Bit_rate = query["bit_rate"]
	FECHA = (datetime.today()).strftime("%d-%b-%Y %H:%M:%S:%f")
	
	#Data_and_Time = json_Dict['Date']	
	#Push into DB Table
	dbObj = DatabaseManager()
	dbObj.add_del_update_db_record("insert into tabla2 (nodo_id, ssid, rssi, canal, bit_rate, fecha) values (?,?,?,?,?,?)",[nodoid, SSID, RSSI, CANAL, Bit_rate, FECHA])
	print "Inserted Temperature Data into Database."
	y1 = dbObj.consulta("select rssi from tabla1")
	y2 = dbObj.consulta("select rssi from tabla2")
	y3 = dbObj.consulta("select rssi from tabla3")
	y4 = dbObj.consulta("select rssi from tabla4")
	print "rssi nodo 1:"
	print (y1) 
	print "rssi nodo 2:"
	print (y2) 
	print "rssi nodo 3:"
	print (y3) 
	print "rssi nodo 4:"
	print (y4) 
	print"eso es todo"

	graficar(y1, y2, y3, y4)	
	#dbObj.consulta("select id from tabla1")
	#print(resultado)
	del dbObj
	print ""
	
#=================================================================
#guardar datos del nodo3
def data_Handler3(jsonData):
	print "topic nodo3"
	
	#Parse Data 
	query = json.loads(jsonData)
	
	nodoid = query["nodo_id"]
	SSID = query["ssid"]
	RSSI = query["rssi"]
	CANAL = query["canal"]
	Bit_rate = query["bit_rate"]
	FECHA = (datetime.today()).strftime("%d-%b-%Y %H:%M:%S:%f")
	
	#Data_and_Time = json_Dict['Date']	
	#Push into DB Table
	dbObj = DatabaseManager()
	dbObj.add_del_update_db_record("insert into tabla3 (nodo_id, ssid, rssi, canal, bit_rate, fecha) values (?,?,?,?,?,?)",[nodoid, SSID, RSSI, CANAL, Bit_rate, FECHA])
	print "Inserted Temperature Data into Database."
	y1 = dbObj.consulta("select rssi from tabla1")
	y2 = dbObj.consulta("select rssi from tabla2")
	y3 = dbObj.consulta("select rssi from tabla3")
	y4 = dbObj.consulta("select rssi from tabla4")
	print "rssi nodo 1:"
	print (y1) 
	print "rssi nodo 2:"
	print (y2) 
	print "rssi nodo 3:"
	print (y3) 
	print "rssi nodo 4:"
	print (y4) 
	print"eso es todo"

	graficar(y1, y2, y3, y4)	
	#dbObj.consulta("select id from tabla1")
	#print(resultado)
	del dbObj
	print ""
	
	
#=================================================================
#guardar datos del nodo4
def data_Handler4(jsonData):
	print "topic nodo4"
	
	#Parse Data 
	query = json.loads(jsonData)
	
	nodoid = query["nodo_id"]
	SSID = query["ssid"]
	RSSI = query["rssi"]
	CANAL = query["canal"]
	Bit_rate = query["bit_rate"]
	FECHA = (datetime.today()).strftime("%d-%b-%Y %H:%M:%S:%f")
	
	#Data_and_Time = json_Dict['Date']	
	#Push into DB Table
	dbObj = DatabaseManager()
	dbObj.add_del_update_db_record("insert into tabla4 (nodo_id, ssid, rssi, canal, bit_rate, fecha) values (?,?,?,?,?,?)",[nodoid, SSID, RSSI, CANAL, Bit_rate, FECHA])
	print "Inserted Temperature Data into Database."
	y1 = dbObj.consulta("select rssi from tabla1")
	y2 = dbObj.consulta("select rssi from tabla2")
	y3 = dbObj.consulta("select rssi from tabla3")
	y4 = dbObj.consulta("select rssi from tabla4")
	print "rssi nodo 1:"
	print (y1) 
	print "rssi nodo 2:"
	print (y2) 
	print "rssi nodo 3:"
	print (y3) 
	print "rssi nodo 4:"
	print (y4) 
	print"eso es todo"

	graficar(y1, y2, y3, y4)	
	#dbObj.consulta("select id from tabla1")
	#print(resultado)
	del dbObj
	print ""
#===============================================================
# Master Function to Select DB Funtion based on MQTT Topic

def sensor_Data_Handler(Topic, jsonData):
	print "entro al handler"
	if Topic == "nodo1":
		data_Handler1(jsonData)
	elif Topic == "nodo2":
		data_Handler2(jsonData)
	elif Topic == "nodo3":
		data_Handler3(jsonData) 
	elif Topic == "nodo4":
		data_Handler4(jsonData)
	else:
		print "error" 

		
#===============================================================
