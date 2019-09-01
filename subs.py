import sys
import paho.mqtt.client
from store_Sensor_Data_to_DB import sensor_Data_Handler


def on_connect(client, userdata, flags, rc):
	print('connected (%s)' % client._client_id)
	client.subscribe(topic = '#', qos=0)

def on_message(client, userdata, msg):
	print('-------------')
	print('topic: %s' % msg.topic)
	print('payload: %s' % msg.payload)
	sensor_Data_Handler(msg.topic, msg.payload)
	
def main():
 
	client = paho.mqtt.client.Client(client_id= 'espectro', clean_session=False)
	client.on_connect = on_connect
	client.on_message = on_message
	client.connect(host='127.0.0.1', port=1883)
	client.loop_forever()
	
if __name__== '__main__':
	main()
	
sys.exit(0)
	
