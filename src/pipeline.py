"""
Demo script for MLflow tracking
"""

import os

import mlflow
from mlflow.models import infer_signature

import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

from dotenv import load_dotenv
from loguru import logger

load_dotenv()

MLFLOW_TRACKING_URI = os.getenv("MLFLOW_TRACKING_URI")


def main():
    """
    Main function to train a model and log it to MLflow    
    """
    logger.info("Starting the MLflow demo script")
    
    # Load the Iris dataset
    logger.info("Loading Iris dataset")
    X, y = datasets.load_iris(return_X_y=True)
    logger.debug(f"Dataset shape: X-{X.shape}, y-{y.shape}")

    # Split the data into training and test sets
    logger.info("Splitting data into train and test sets")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    logger.debug(f"Train set shape: X-{X_train.shape}, y-{y_train.shape}")
    logger.debug(f"Test set shape: X-{X_test.shape}, y-{y_test.shape}")

    # Define the model hyperparameters
    params = {
        "solver": "lbfgs",
        "max_iter": 1000,
        "random_state": 8888,
    }
    logger.info(f"Model hyperparameters: {params}")

    # Train the model
    logger.info("Training Logistic Regression model")
    lr = LogisticRegression(**params)
    lr.fit(X_train, y_train)
    logger.success("Model training completed")

    # Predict on the test set
    logger.info("Making predictions on test set")
    y_pred = lr.predict(X_test)

    # Calculate metrics
    accuracy = accuracy_score(y_test, y_pred)
    logger.info(f"Model accuracy: {accuracy:.2f}")

    # Set our tracking server uri for logging
    logger.info("Configuring MLflow tracking URI")
    mlflow.set_tracking_uri(uri=MLFLOW_TRACKING_URI)

    # Create a new MLflow Experiment
    logger.info("Setting up MLflow experiment")
    mlflow.set_experiment("MLflow Quickstart From Script")

    # Start an MLflow run
    logger.info("Starting MLflow run")

    run_params = dict(
        run_name=f"run_{pd.Timestamp.now().strftime('%Y%m%d%H%M%S')}",
    )
    with mlflow.start_run(**run_params):
        try:
            # Log the hyperparameters
            logger.debug("Logging hyperparameters to MLflow")
            mlflow.log_params(params)

            # Log the loss metric
            logger.debug("Logging metrics to MLflow")
            mlflow.log_metric("accuracy", accuracy)

            # Set a tag that we can use to remind ourselves what this run was for
            logger.debug("Setting MLflow tags")
            mlflow.set_tag("LR Info", "LR model from script")

            # Infer the model signature
            logger.info("Inferring model signature")
            signature = infer_signature(X_train, lr.predict(X_train))

            # Log the model
            logger.info("Logging model to MLflow")
            model_info = mlflow.sklearn.log_model(
                sk_model=lr,
                artifact_path="iris_model",
                signature=signature,
                input_example=X_train,
                registered_model_name="script-tracking-quickstart",
            )

            logger.success("MLflow run completed successfully")
            logger.info(f"Model info: {model_info}")

        except Exception as e:
            logger.error(f"Error during MLflow run: {str(e)}")
            raise

if __name__ == "__main__":
    main()
