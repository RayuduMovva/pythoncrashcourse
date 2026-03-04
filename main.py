import sys

from src.logging import logger
from src.exception.exception import ProjectException

from src.component.data_ingestion import DataIngestion
from src.component.data_ingestion import DataIngestionArtifact  
from src.component.data_ingestion import DataIngestionConfig




try:
    logger.logging.info("Starting the main.py script")
    data_ingestion = DataIngestion()
    train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()
    logger.logging.info(f"Data Ingestion completed successfully. Train data path: {train_data_path}, Test data path: {test_data_path}")

except Exception as e:
    logger.logging.error("An error occurred: {}".format(str(e)))
    raise ProjectException(e, sys)
