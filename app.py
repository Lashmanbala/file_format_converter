import glob
import json
import pandas as pd
import os
from dotenv import load_dotenv
import sys


def get_column_details(schema,ds_name,sorting_key='column_position'):
    column_details = schema[ds_name]
    columns = sorted(column_details, key=lambda col:col[sorting_key])
    return [col['column_name'] for col in columns]

def read_csv(file, schema):
    file_path_list = file.split('/')
    ds_name = file_path_list[-2]
    file_name = file_path_list[-1]
    columns = get_column_details(schema, ds_name)
    df = pd.read_csv(file, names=columns)
    return df

def to_json(df, tgt_base_dir, ds_name, file_name):
    json_file_path = f'{tgt_base_dir}/{ds_name}/{file_name}'
    os.makedirs(f'{tgt_base_dir}/{ds_name}')
    df.to_json(json_file_path, orient='records', lines=True)

def file_converter(ds_name, src_base_dir, tgt_base_dir):
    files = glob.glob(f'{src_base_dir}/{ds_name}/part-*')
    schema = json.load(open(f'{src_base_dir}/schemas.json'))

    if len(files) == 0:       # glob.glob returns a list
        raise NameError(f'No files found for {ds_name}')
    for file in files:
        df = read_csv(file, schema)
        file_name = file.split('/')[-1]
        to_json(df, tgt_base_dir, ds_name, file_name)

def process_files(ds_names=None):
    load_dotenv()
    src_base_dir=os.environ.get('SRC_BASE_DIR')
    tgt_base_dir=os.environ.get('TGT_BASE_DIR')
    schema = json.load(open(f'{src_base_dir}/schemas.json'))

    if not ds_names:
        ds_names = schema.keys()
    for ds_name in ds_names:
        try:
            print(f'processing {ds_name}')
            file_converter(ds_name, src_base_dir, tgt_base_dir)
        except NameError as ne:
            print(ne)
            print(f'Error processing {ds_name}')
            pass

if __name__ == '__main__':
    if len(sys.argv) == 2:
        ds_names = json.loads(sys.argv[1])  # argv returns a list with the filename and arguments as its elements.
                                            # run time args should be in json array format. 
                                            # Ex:'["categories", "products"]'  Ex: "[\"categories\",\"product\",\"departments\"]"
        process_files(ds_names)
    else:
        process_files()