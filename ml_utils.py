import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import accuracy_score

# GradientBoostingRegressor
gb = GradientBoostingRegressor()
enc = []
#keep_feats1 = []
lenc = LabelEncoder()

# function to train and load the model during startup
def load_model():
    #import data
    train_data = pd.read_csv('train.csv')
    #test = pd.read_csv('test.csv')
    #Id = test.iloc[:, 0]
    
    #Prepare Data
    #trainc = train.columns[train.isnull().any()] # Null columns in train data
    #testc = test.columns[test.isnull().any()]    # Null columns in test data 
    #totc = train.columns 
    
    # Keeping features which don't have missing values in train data
    #keep_feats1 = [x for x in totc if x not in trainc]
    #print("keep_feats: ", keep_feats)
    #train_data = train.loc[:, keep_feats]
    
    #keep_feats.remove('Electrical')
    #print(type(train))
    #train_data = train.loc[:, keep_feats]
    #test_data = test.loc[:, keep_feats[:-1]]    
    #train_data.fillna('NA', inplace=True)
    train_data = train_data.iloc[:, 1:]
    #train_data = train_data.replace(np.nan, np.)
    #train_data.fillna(0)
    for types in train_data.dtypes.iteritems():
        if not str(types[1]) == 'int64': 
            enc.append(types[0])
    
    train_data.loc[:, enc] = train_data.loc[:, enc].apply(lenc.fit_transform)
    #test_data.loc[:, enc] = test_data.loc[:, enc].apply(lenc.fit_transform)

    #Splitting the data for training and testing
    X = train_data.iloc[:, :-1]
    y = train_data.iloc[:, -1]
    X_train, X_test, y_train, y_test = train_test_split(X, y)
    #print(X_train)
    gb.fit(X_train, y_train)

    # calculate the print the accuracy score 
    print(gb.score(X_train, y_train))
    print(gb.score(X_test, y_test))
    #print("keep_feats: ", keep_feats)
    #acc = accuracy_score(y_test, gb.predict(X_test))
    #print(f"Model trained with accuracy: {round(acc, 3)}")


# function to predict
def predict(query_data):
    #print("keep_feats: ", keep_feats)
    #pred_data = list(query_data.dict().values())
    columns = ["MSSubClass","MSZoning","LotFrontage","LotArea","Street","Alley","LotShape","LandContour","Utilities","LotConfig","LandSlope","Neighborhood","Condition1","Condition2","BldgType","HouseStyle","OverallQual","OverallCond","YearBuilt","YearRemodAdd","RoofStyle","RoofMatl","Exterior1st","Exterior2nd","MasVnrType","MasVnrArea","ExterQual","ExterCond","Foundation","BsmtQual","BsmtCond","BsmtExposure","BsmtFinType1","BsmtFinSF1","BsmtFinType2","BsmtFinSF2","BsmtUnfSF","TotalBsmtSF","Heating","HeatingQC","CentralAir","Electrical","FirstFlrSF","SecondFlrSF","LowQualFinSF","GrLivArea","BsmtFullBath","BsmtHalfBath","FullBath","HalfBath","BedroomAbvGr","KitchenAbvGr","KitchenQual","TotRmsAbvGrd","Functional","Fireplaces","FireplaceQu","GarageType","GarageYrBlt","GarageFinish","GarageCars","GarageArea","GarageQual","GarageCond","PavedDrive","WoodDeckSF","OpenPorchSF","EnclosedPorch","ThreeSsnPorch","ScreenPorch","PoolArea","PoolQC","Fence","MiscFeature","MiscVal","MoSold","YrSold","SaleType","SaleCondition"]    
    index = [0]
    df = pd.DataFrame(query_data.dict(), columns=columns, index=index)
    #print("df: ", df)
    #print("keep_feats: ", keep_feats)
    #test_data = df.loc[:, keep_feats[:-1]]
    #print("keep_feats: ", keep_feats)
    #print("test_data: ", test_data)
    #print("enc: ", enc)
    test_data = df;
    #test_data = test_data.replace(np.nan, 'NA', regex=True)
    #test_data.fillna('NA', inplace=True)
    #print("test_Data: ", test_data)
    #test_data.fillna(0)
    test_data.loc[:, enc] = test_data.loc[:, enc].apply(lenc.fit_transform)
    #print(test_data)
    #print(test_data.isnull().values.any())
    #print(test_data.isnull())
    #test_data.isnull().to_csv("out.csv",index=False)
    prediction = gb.predict(test_data)
    print("Model prediction: ", prediction)
    #p1 = lenc.inverse_transform(prediction)
    #print("p1: ", p1[0])
    #print(f"Model prediction: {classes[p1[0]-1]}")
    #return classes[p1[0]-1]
    return prediction[0]