#!/usr/bin/python3                                                                                                      
                                                                                                                        
from pyspark import SparkContext                                                                                        
from pyspark.sql import SparkSession                                                                                    
from pyspark.streaming import StreamingContext                                                                          
from pyspark.streaming.kafka import KafkaUtils 
import requests
import json
import spark
from kafka import KafkaConsumer
#import nltk
# nltk.download('vader_lexicon')
#from nltk.sentiment.vader import SentimentIntensityAnalyzer

#processing each micro batch
def process_events(event):
    print("event ", event[1])
    l = event[1].split(',')
    if(l[3] == 'NA'): l[3] = 0
    if(l[26] == 'NA'): l[26] = 0
    if(l[34] == 'NA'): l[34] = 0
    if(l[36] == 'NA'): l[36] = 0
    if(l[37] == 'NA'): l[37] = 0
    if(l[38] == 'NA'): l[38] = 0
    if(l[47] == 'NA'): l[47] = 0
    if(l[48] == 'NA'): l[48] = 0
    if(l[55] == 'NA'): l[55] = 0
    if(l[57] == 'NA'): l[57] = 0
    if(l[58] == 'NA'): l[58] = 0
    payload = {
    "MSSubClass": l[1],
    "MSZoning": l[2],
    "LotFrontage": l[3],
    "LotArea": l[4],
    "Street": l[5],
    "Alley": l[6],
    "LotShape": l[7],
    "LandContour": l[8],
    "Utilities": l[9],
    "LotConfig": l[10],
    "LandSlope": l[10],
    "Neighborhood": l[12],
    "Condition1": l[13],
    "Condition2": l[14],
    "BldgType": l[15],
    "HouseStyle": l[16],
    "OverallQual": l[17],
    "OverallCond": l[18],
    "YearBuilt": l[19],
    "YearRemodAdd": l[20],
    "RoofStyle": l[21],
    "RoofMatl": l[22],
    "Exterior1st": l[23],
    "Exterior2nd": l[24],
    "MasVnrType": l[25],
    "MasVnrArea": l[26],
    "ExterQual": l[27],
    "ExterCond": l[28],
    "Foundation": l[29],
    "BsmtQual": l[30],
    "BsmtCond": l[31],
    "BsmtExposure": l[32],
    "BsmtFinType1": l[33],
    "BsmtFinSF1": l[34],
    "BsmtFinType2": l[35],
    "BsmtFinSF2": l[36],
    "BsmtUnfSF": l[37],
    "TotalBsmtSF": l[38],
    "Heating": l[39],
    "HeatingQC": l[40],
    "CentralAir": l[41],
    "Electrical": l[42],
    "FirstFlrSF": l[43],
    "SecondFlrSF": l[44],
    "LowQualFinSF": l[45],
    "GrLivArea": l[46],
    "BsmtFullBath": l[47],
    "BsmtHalfBath": l[48],
    "FullBath": l[49],
    "HalfBath": l[50],
    "BedroomAbvGr": l[51],
    "KitchenAbvGr": l[52],
    "KitchenQual": l[53],
    "TotRmsAbvGrd": l[54],
    "Functional": l[55],
    "Fireplaces": l[56],
    "FireplaceQu": l[57],
    "GarageType": l[58],
    "GarageYrBlt": l[59],
    "GarageFinish": l[60],
    "GarageCars": l[61],
    "GarageArea": l[62],
    "GarageQual": l[63],
    "GarageCond": l[64],
    "PavedDrive": l[65],
    "WoodDeckSF": l[66],
    "OpenPorchSF": l[67],
    "EnclosedPorch": l[68],
    "ThreeSsnPorch": l[69],
    "ScreenPorch": l[70],
    "PoolArea": l[71],
    "PoolQC": l[72],
    "Fence": l[73],
    "MiscFeature": l[74],
    "MiscVal": l[75],
    "MoSold": l[76],
    "YrSold": l[77],
    "SaleType": l[78],
    "SaleCondition": l[79]         
     }
#        print("payload", payload )
    response = requests.post('http://localhost:8887/predict_house_price/', json = payload)
    #print("l[0] ", l[0])
    response_dict = json.loads(response.text)
    print("response_dict ", response_dict)
    return (l[1],l[2],l[3],l[4],l[5],l[6],l[7],l[8],l[9],l[10],l[11],l[12],l[13],l[14],l[15],l[16],l[17],l[18],l[19],l[20],l[21],l[22],l[23],l[24],l[25],l[26],l[27],l[28],l[29],l[30],l[31],l[32],l[33],l[34],l[35],l[36],l[37],l[38],l[39],l[40],l[41],l[42],l[43],l[44],l[45],l[46],l[4],l[48],l[49],l[50],l[51],l[52],l[53],l[54],l[55],l[56],l[57],l[58],l[59],l[60],l[61],l[62],l[63],l[64],l[65],l[66],l[67],l[68],l[69],l[70],l[71],l[72],l[73],l[74],l[75],l[76],l[77],l[78],l[79],response_dict['saleprice'])

def handle_rdd(rdd):                                                                                                    
    if not rdd.isEmpty():                                                                                               
        global ss                                                                                                       
        df = ss.createDataFrame(rdd, schema=["MSSubClass","MSZoning","LotFrontage","LotArea","Street","Alley","LotShape","LandContour","Utilities","LotConfig","LandSlope","Neighborhood","Condition1","Condition2","BldgType","HouseStyle","OverallQual","OverallCond","YearBuilt","YearRemodAdd","RoofStyle","RoofMatl","Exterior1st","Exterior2nd","MasVnrType","MasVnrArea","ExterQual","ExterCond","Foundation","BsmtQual","BsmtCond","BsmtExposure","BsmtFinType1","BsmtFinSF1","BsmtFinType2","BsmtFinSF2","BsmtUnfSF","TotalBsmtSF","Heating","HeatingQC","CentralAir","Electrical","FirstFlrSF","SecondFlrSF","LowQualFinSF","GrLivArea","BsmtFullBath","BsmtHalfBath","FullBath","HalfBath","BedroomAbvGr","KitchenAbvGr","KitchenQual","TotRmsAbvGrd","Functional","Fireplaces","FireplaceQu","GarageType","GarageYrBlt","GarageFinish","GarageCars","GarageArea","GarageQual","GarageCond","PavedDrive","WoodDeckSF","OpenPorchSF","EnclosedPorch","ThreeSsnPorch","ScreenPorch","PoolArea","PoolQC","Fence","MiscFeature","MiscVal","MoSold","YrSold","SaleType","SaleCondition","SalePrice"])                                                
        df.show()                                                                                                       
        df.write.saveAsTable(name='default.HousePricePredictor', format='hive', mode='append')                                       
                                                                                                                        
sc = SparkContext(appName="Something")                                                                                     
ssc = StreamingContext(sc, 5)                                                                                           
                                                                                                                        
ss = SparkSession.builder.appName("Something").config("spark.sql.warehouse.dir", "/user/hve/warehouse").config("hive.metastore.uris", "thrift://localhost:9083").enableHiveSupport().getOrCreate()                                                                                                  
                                                                                                                        
ss.sparkContext.setLogLevel('WARN')
                                                                                    
                                                                                                                        
ks = KafkaUtils.createDirectStream(ssc, ['HousePricePredictorRequests'], {'metadata.broker.list': 'localhost:9092'})  

transform = ks.map(lambda x : process_events(x)) 
 
                                                                                                            
#transform = lines.map(lambda r: (60,"RL",65,8450,"Pave","NA","Reg","Lvl","AllPub","Inside","Gtl","CollgCr","Norm","Norm","1Fam", "2Story",7,5,2003,2003,"Gable","CompShg","VinylSd","VinylSd","BrkFace",196,"Gd","TA","PConc","Gd","TA","No","GLQ",706,"Unf",0,150,856,"GasA","Ex","Y","SBrkr",856,854,0,1710,1,0,2,1,3,1,"Gd",8,"Typ",0,"NA","Attchd",2003,"RFn",2,548,"TA","TA","Y",0,61,0,0,0,0,"NA","NA","NA",0,2,2008,"WD","Normal",205115.96305968))                                  

transform.foreachRDD(handle_rdd)                                                                                        
                                                                                                                        
ssc.start()                                                                                                             
ssc.awaitTermination()

# CREATE TABLE tweets (text STRING, words INT, length INT, text STRING) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\\|' STORED AS TEXTFILE;
