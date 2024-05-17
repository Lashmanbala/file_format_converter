import glob
import json
import pandas as pd
import os

src_file_names = glob.glob('data/retail_db/*/part-*', recursive=True) 
#print(src_file_names)

schema = json.load(open('data/retail_db/schemas.json'))
#print(schema['departments'])
clm = schema['orders']
clms = sorted(clm, key=lambda col:col['column_position'])
#for i in clms:
#    print(i['column_name'])

def get_column_details(schema,ds_name,sorting_key='column_position'):
    column_details = schema[ds_name]
    columns = sorted(column_details, key=lambda col:col[sorting_key])
    return [col['column_name'] for col in columns]

#print(get_column_details(schema,'orders'))
#print(get_column_details(schema,'order_items'))
#print(get_column_details(schema,'departments'))

#print(src_file_names[0].split('/')[2])
#print(src_file_names[1].split('/')[2])
#print(src_file_names[2].split('/')[2])

#for file in src_file_names:
#    print(file.split('/')[2])

# reading all the files dynamically
for file in src_file_names:
    print(f'processing {file}')
    ds_name = file.split('/')[2]
    clms = get_column_details(schema, ds_name)
    df = pd.read_csv(file, names=clms)
    print(df.shape)

# creating target files to write json file
tgt_base_dir = 'data/retail_db_json'
for file in src_file_names:
    ds_name = file.split('/')[-1]
    file_name = file.split('/')[-2]
    print(f'{tgt_base_dir}/{file_name}/{ds_name}')
    os.makedirs(f'{tgt_base_dir}/{file_name}/{ds_name}', exist_ok=True)