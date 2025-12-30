import pandas as pd
from schema import get_column_names, load_and_validate_schema
from logger import logger
from pathlib import Path

def read_csv(schema, dataset_name, file_path):
    try:
        column_names = get_column_names(schema, dataset_name)
    except Exception as e:
        raise ValueError(f"Error retrieving column names for dataset {dataset_name}: {e}")
    
    try:
        df = pd.read_csv(file_path, names=column_names)
        logger.info(f"CSV file {file_path} read successfully for dataset {dataset_name} with {len(df)} rows.")
        return df
    except Exception as e:
        raise IOError(f"Error reading CSV file {file_path} for dataset {dataset_name}: {e}")
    
schema = load_and_validate_schema(Path("data/retail_db/schemas.json"))
file_path = Path("data/retail_db/categories/part-00000")
dataset_name = "categories"
df = read_csv(schema, dataset_name, file_path)
print(df.head(2))