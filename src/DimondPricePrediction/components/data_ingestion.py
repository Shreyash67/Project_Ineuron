import pandas as pd
import numpy as np
import os
import sys
from src.DimondPricePrediction.logger import logging
from src.DimondPricePrediction.exception import customeexception


from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from pathlib import Path

class DataIngestionConfig:
    raw_data_path:str = os.path.join("artifacts","raw.csv")
    train_data_path:str = os.path.join("artifacts","train_data.csv")
    test_data_path:str = os.path.join("artifacts","test_data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("data ingestion started")

        try:
            data=pd.read_csv(Path(os.path.join("notebooks/data","gemstone.csv")))
            logging.info("I have read the dataset as df")


            os.makedirs(os.path.dirname(os.path.join(self.ingestion_config.raw_data_path)),exist_ok=True)
            data.to_csv(self.ingestion_config.raw_data_path,index=False)
            logging.info("i have saved the raw dataset in artifact folder")

            logging.info("here i have perform train test split")

            train_data,test_data=train_test_split(data,test_size=0.25)
            logging.info("train test split completed")
            train_data.to_csv(self.ingestion_config.train_data_path,index=False)
            test_data.to_csv(self.ingestion_config.test_data_path,index=False)

            logging.info("Data ingestion path completed")

        except Exception as e:
            logging.info("exception during occured at data ingestion stage")
            raise customeexception(e,sys)