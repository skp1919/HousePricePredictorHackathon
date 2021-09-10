import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from ml_utils import load_model, predict
from typing import List
import datetime

# defining the main app
app = FastAPI(title="House Price Predictor", docs_url="/")

# calling the load_model during startup.
# this will train the model and keep it loaded for prediction.
app.add_event_handler("startup", load_model)

# class which is expected in the payload
class QueryIn(BaseModel):
    MSSubClass: float
    MSZoning: str
    LotFrontage: float
    LotArea: float
    Street: str
    Alley: str
    LotShape: str
    LandContour: str
    Utilities: str
    LotConfig: str
    LandSlope: str
    Neighborhood: str
    Condition1: str
    Condition2: str
    BldgType: str
    HouseStyle: str
    OverallQual: float
    OverallCond: float
    YearBuilt: float
    YearRemodAdd: float
    RoofStyle: str
    RoofMatl: str
    Exterior1st: str
    Exterior2nd: str
    MasVnrType: str
    MasVnrArea: float
    ExterQual: str
    ExterCond: str
    Foundation: str
    BsmtQual: str
    BsmtCond: str
    BsmtExposure: str
    BsmtFinType1: str
    BsmtFinSF1: float
    BsmtFinType2: str
    BsmtFinSF2: float
    BsmtUnfSF: float
    TotalBsmtSF: float
    Heating: str
    HeatingQC: str
    CentralAir: str
    Electrical: str
    FirstFlrSF: float
    SecondFlrSF: float
    LowQualFinSF: float
    GrLivArea: float
    BsmtFullBath: float
    BsmtHalfBath: float
    FullBath: float
    HalfBath: float
    BedroomAbvGr: float
    KitchenAbvGr: float
    KitchenQual: str
    TotRmsAbvGrd: float
    Functional: str
    Fireplaces: float
    FireplaceQu: str
    GarageType: str
    GarageYrBlt: float
    GarageFinish: str
    GarageCars: float
    GarageArea: float
    GarageQual: str
    GarageCond: str
    PavedDrive: str
    WoodDeckSF: float
    OpenPorchSF: float
    EnclosedPorch: float
    ThreeSsnPorch: float
    ScreenPorch: float
    PoolArea: float
    PoolQC: str
    Fence: str
    MiscFeature: str
    MiscVal: float
    MoSold: float
    YrSold: float
    SaleType: str
    SaleCondition: str

# class which is returned in the response
class QueryOut(BaseModel):
    saleprice: str
    timestamp: str

# Route definitions
@app.get("/ping")
# Healthcheck route to ensure that the API is up and running
def ping():
    ct = datetime.datetime.now().strftime('%d-%B-%y %H:%M')
    return {"ping": "pong", "timestamp": ct}


@app.post("/predict_house_price", response_model=QueryOut, status_code=200)
# Route to do the prediction using the ML model defined.
# Payload: QueryIn containing the parameters
# Response: QueryOut containing the saleprice predicted (200)
def predict_house_price(query_data: QueryIn):
    ct = datetime.datetime.now().strftime('%d-%B-%y %H:%M')
    output = {"saleprice": predict(query_data), "timestamp": ct}
    return output


# Main function to start the app when main.py is called
if __name__ == "__main__":
    # Uvicorn is used to run the server and listen for incoming API requests on 0.0.0.0:8887
    uvicorn.run("main:app", host="0.0.0.0", port=8887, reload=True)
