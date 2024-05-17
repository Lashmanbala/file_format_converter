import glob
import json
import pandas as pd
import os

src_file_names = glob.glob('data/retail_db/*/part-*', recursive=True) 

def get_column_details(schema,ds_name,sorting_key='column_position'):
    column_details = schema[ds_name]
    columns = sorted(column_details, key=lambda col:col[sorting_key])
    return [col['column_name'] for col in columns]

# reading all the files dynamically
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

def file_converter(ds_name, tgt_base_dir='data/retail_db_json', src_base_dir='data/retail_db'):
    files = glob.glob(f'{src_base_dir}/{ds_name}/part-*')
    schema = json.load(open(f'{src_base_dir}/schemas.json'))

    for file in files:
        df = read_csv(file, schema)
        file_name = file.split('/')[-1]
        to_json(df, tgt_base_dir, ds_name, file_name)
        print('success')

ds_name = 'categories'
file_converter(ds_name)