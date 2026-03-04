import sys
import os
from src.logging import logger
from src.exception.exception import ProjectException 
import pandas as pd
import os
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    raw_data_path: str = os.path.join('raw_file', 'raw_data.csv')
    

@dataclass
class DataIngestionArtifact:
    raw_data_path: str = os.path.join('raw_file', 'raw_data.csv')
    train_data_path: str = os.path.join('artifacts', 'train_data.csv')
    test_data_path: str = os.path.join('artifacts', 'test_data.csv')
    validation_data_path: str = os.path.join('artifacts', 'validation_data.csv')

class DataIngestion:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        self.artifact_config = DataIngestionArtifact()

    def initiate_data_ingestion(self):
        logger.logging.info("Data Ingestion started")
        try:
            df = pd.read_csv("notebooks/raw_data.csv")
            logger.logging.info("Raw data read successfully")

            os.makedirs(os.path.dirname(self.data_ingestion_config.raw_data_path), exist_ok=True)
            os.makedirs(os.path.dirname(self.artifact_config.train_data_path), exist_ok=True)
    
            df.to_csv(self.data_ingestion_config.raw_data_path, index=False)

            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            train_set.to_csv(self.artifact_config.train_data_path, index=False)
            test_set.to_csv(self.artifact_config.test_data_path, index=False)
            logger.logging.info("Train and Test data created successfully")

            return(self.artifact_config.train_data_path, self.artifact_config.test_data_path
                   )

            #validation_set, test_set = train_test_split(test_set, test_size=0.5, random_state=42)
            #validation_set.to_csv(self.data_ingestion_config.validation_data_path, index=False)
            #test_set.to_csv(self.data_ingestion_config.test_data_path, index=False)
            #logger.info("Validation data created successfully")

        except Exception as e:
            logger.logging.error(f"Error in Data Ingestion: {e}")
            raise ProjectException(e,sys)