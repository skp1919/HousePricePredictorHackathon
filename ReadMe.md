## Problem Statement
- House Price Prediction

## Group Name
- Group 1 Hackathon 2

## Names:
- Parsha Sai Krishna
- Kanukollu Gnana Venkata Ram Mohan

## File components
- main.py : This is the main python file for the api application.
- ml_utils.py : This is the utility file to perform the actual ml processing like data loading, model building, training, predicting
- housePricePredictorRequestStream.py : This is the producer stream which will read data from test.csv and stream one by one row through kafka.
- predictor.py : Kafka stream consumer. Consumes the stream, uses API to predict and store the complete data set to hive.
- createtable.txt : sql command to create 'HousePricePredictor' in Hive
- see_contents.py : can be used to see the contents in the 'HousePricePredictor' table in hive while the service is running
- requirements.txt : This lists all the dependencies
- snaps : This folder has the screenshots of all the results.
- housePricePredictor.ipynb : jupyter notebook file used to test, before adding them to actual project
- EnvironmentSetupHelper.txt : Has the download links, commands for environment setup.
- data_description.txt : Description of the data used
- train.csv : train data
- test.csv : test data
- ReadMe.md: This is the read me file.

## Running Instructions
- Please ensure Environment setup (mentioned below) is complete before proceeding
- Install dependencies using `pip3 install -r requirements.txt`
- Terminal 1: move to kafka directory, start zookeeper server
	$ cd kafka/
	~/kafka$ bin/zookeeper-server-start.sh config/zookeeper.properties
- Terminal 2: move to kafka directory, start kafka server
	~$ cd kafka/
	~/kafka$ bin/kafka-server-start.sh config/server.properties
- Terminal 3: Create a topic 'HousePricePredictorRequests'
	~/kafka$ bin/kafka-topics.sh --list --bootstrap-server localhost:9092
	~/kafka$ bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic HousePricePredictorRequests
- Terminal 4: Start Hive service
	~$ hive --service metastore
- Terminal 5: Check for records in Hive
	~$ hive
	...
	hive> select count(*) from default.HousePricePredictor;
- Terminal 6: Stream Producer
	~$ python3 housePricePredictorRequestStream.py
- Terminal 7: Run Predictor API
	~$ python3 main.py
- Terminal 8: Stream Consumer, predict and store to hive
	~$ spark-submit --jars spark-streaming-kafka-0-8-assembly_2.11-2.4.8.jar predictor.py
- Once the processing starts please use Terminal 5 for checking the data in hive

## Environment Setup

- VM Setup - Ubuntu 18.04 Image.
- Install Kafka, unzip the contents and rename the folder to 'kafka'
- Install Java.
- Install Kafka-Python
- Install Hadoop, unzip the contents and rename the folder to 'hadoop'
- Update Hadoop environment variables.
- Setup Hadoop
- Setup SSH
- Start the Hadoop cluster
- Install Hive, unzip the contents and rename the folder 'hive'
- Update Hive environment variables
- Setup Permissions to HDFS
- Setup Hive
- create a database schema for Hive
- Start the Hive Metastore server.
- Enter Hive shell and Make the database for storing our House Price Prediction data	
- Install Spark, unzip the contents and rename the folder to 'spark'
- Install pyspark
- Update spark, pyspark environment variables.
- Download the JAR file for pyspark to connect to kafka.

For more details on Environment setup, please use EnvironmentSetupHelper.txt

Note: This is checked into github : https://github.com/skp1919/HousePricePredictorHackathon/tree/master