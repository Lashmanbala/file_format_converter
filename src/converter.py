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
    


def write_json_files(output_path, df):
    try:
        output_path.parent.mkdir(parents=True, exist_ok=True) # Ensure parent directory exists

        df.to_json(output_path, orient='records', lines=True)

        logger.info(f"Wrote JSON file {output_path}")

    except Exception as e:
        raise OSError("Error writing JFON file {output_path}: {e}") 


schema = load_and_validate_schema(Path("data/retail_db/schemas.json"))
file_path = Path("data/retail_db/categories/part-00000")
dataset_name = "categories"
df = read_csv(schema, dataset_name, file_path)
print(df.head(2))
output_path = Path("data/retail_db_json/categories.json")
write_json_files(output_path, df)