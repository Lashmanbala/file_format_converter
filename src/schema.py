import json
from pathlib import Path

def load_and_validate_schema(schema_path):
    if not schema_path.exists:
        raise FileNotFoundError(f"Schema file not found at {schema_path}")
    
    if not schema_path.is_file():
        raise ValueError("Provided schema path is not a file.")
    
    if not schema_path.suffix == '.json':
        raise ValueError("Schema file must be a JSON file.")

    try:
        with open(schema_path, 'r') as file:
            schema = json.load(file)
    except json.JSONDecodeError as e:
        raise ValueError(f"Error decoding JSON from schema file: {e}")
    
    for dataset_name, columns in schema.items():
        if not isinstance(columns, list):
            raise ValueError("Columns for dataset {dataset} must be a list")
        
        for i, col in enumerate(columns):
            if not isinstance(col, dict):
                raise ValueError(f"Column definition at indec {i} in dataset {dataset_name} must be a dictionary")
            
            required_columns = {'column_name', 'column_position'}
            if not required_columns.issubset(col.keys()):
                missing = required_columns - col.keys()
                raise ValueError(f"Columns {missing} are missing in column definition at index {i} in dataset {dataset_name}")
            
    return schema

print(load_and_validate_schema(Path("data/retail_db/schemas.json")))