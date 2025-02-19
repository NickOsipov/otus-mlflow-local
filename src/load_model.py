import os

import mlflow
from mlflow.tracking import MlflowClient
import numpy as np

from loguru import logger
from dotenv import load_dotenv

load_dotenv()

MLFLOW_TRACKING_URI = os.getenv("MLFLOW_TRACKING_URI")


def load_model_from_registry():
    """
    Load model from MLflow model registry
    """
    try:
        logger.info("Starting model loading process")
        
        # Установка URI для MLflow
        logger.info("Setting MLflow tracking URI")
        mlflow.set_tracking_uri(uri=MLFLOW_TRACKING_URI)
        
        # Создание клиента
        logger.info("Creating MLflow client")
        client = MlflowClient()
        model_name = "tracking-quickstart"
        model_alias = "prod"
        
        # Загрузка модели
        logger.info("Loading latest model version")
        model = mlflow.pyfunc.load_model(
            model_uri=f"models:/{model_name}@{model_alias}"
        )
        logger.success("Model loaded successfully")
        
        # Получение информации о модели
        logger.info("Fetching model details")
        model_info = client.get_model_version_by_alias(model_name, model_alias)

        for key, value in model_info.__dict__.items():
            logger.info(f"\t{key}: {value}")
            
        return model
        
    except Exception as e:
        logger.error(f"Error loading model: {str(e)}")
        raise

if __name__ == "__main__":
    try:
        model = load_model_from_registry()
        test_data = np.array([[5.1, 3.5, 1.4, 0.2]])
        logger.info("Making prediction with loaded model")
        prediction = model.predict(test_data)
        logger.info(f"Prediction result: {prediction}")

    except Exception as e:
        logger.error(f"Script failed: {str(e)}")
        raise
