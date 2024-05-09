import glob
import json

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
print(get_column_details(schema,'orders'))
print(get_column_details(schema,'order_items'))
print(get_column_details(schema,'departments'))