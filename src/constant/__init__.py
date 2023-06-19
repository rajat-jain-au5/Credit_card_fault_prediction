import os


AWS_S3_BUCKET_NAME = "Credit-card-fault-deployment"
MONGO_DATABASE_NAME = "credit_card"
MONGO_COLLECTION_NAME = "credit_card_fault_data"

TARGET_COLUMN = "default payment next month"
MONGO_DB_URL="mongodb+srv://rajatjain852:rajat321@cluster0.drhks7r.mongodb.net/?retryWrites=true&w=majority"

MODEL_FILE_NAME = "model"
MODEL_FILE_EXTENSION = ".pkl"

artifact_folder =  "artifacts"