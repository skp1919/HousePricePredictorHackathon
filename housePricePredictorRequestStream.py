#!/usr/bin/python3                                                                                                      
                                                                                                                        
from kafka import KafkaProducer                                                                                         
from random import randint                                                                                              
from time import sleep
from csv import reader
import sys                                                                                                              
                                                                                                                        
BROKER = 'localhost:9092'                                                                                               
TOPIC = 'HousePricePredictorRequests'                                                                                                      
                                                                        
                                                                                                                        
try:                                                                                                                    
    p = KafkaProducer(bootstrap_servers=BROKER)                                                                         
except Exception as e:                                                                                                  
    print(f"ERROR --> {e}")                                                                                             
    sys.exit(1)                                                                                                        
                                                                                                                        
while True:                                                                                                             
    message = []                                                                                                       
    
    with open('test.csv', 'r') as read_obj:
    	csv_reader = reader(read_obj)
    	header = next(csv_reader)
    	# Check file as empty
    	if header != None:
        	# Iterate over each row after the header in the csv
        	for row in csv_reader:
            		message = ', '.join(row)                                                                 
            		print(f">>> '{message}'")                                                                                           
            		p.send(TOPIC, bytes(message,encoding="utf8"))                                                                      
            		sleep(randint(1,4))
