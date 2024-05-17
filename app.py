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
#for file in src_file_names:
#    print(f'processing {file}')
#    ds_name = file.split('/')[2]
#    clms = get_column_details(schema, ds_name)
#    df = pd.read_csv(file, names=clms)
#    print(df.shape)

# creating target files to write json file
#tgt_base_dir = 'data/retail_db_json'
#for file in src_file_names:
#    ds_name = file.split('/')[-2]
#    file_name = file.split('/')[-1]
#    print(f'{tgt_base_dir}/{file_name}/{ds_name}')
#    os.makedirs(f'{tgt_base_dir}/{file_name}/{ds_name}', exist_ok=True)

src_file_path = 'data/retail_db/categories/part-00000'

json_file_path = 'data/retail_db_json/categories/part-00000'
os.makedirs('data/retail_db_json/categories', exist_ok = True)
columns = get_column_details(schema, 'categories')
df = pd.read_csv(src_file_path, names = columns)

#df.to_json(json_file_path)
# {"category_id":{"0":1,"1":2,"2":3,"3":4,"4":5,"5":6,"6":7,"7":8,"8":9,"9":10,"10":11,"11":12,"12":13,"13":14,"14":15,"15":16,"16":17,"17":18,"18":19,"19":20,"20":21,"21":22,"22":23,"23":24,"24":25,"25":26,"26":27,"27":28,"28":29,"29":30,"30":31,"31":32,"32":33,"33":34,"34":35,"35":36,"36":37,"37":38,"38":39,"39":40,"40":41,"41":42,"42":43,"43":44,"44":45,"45":46,"46":47,"47":48,"48":49,"49":50,"50":51,"51":52,"52":53,"53":54,"54":55,"55":56,"56":57,"57":58},"category_department_id":{"0":2,"1":2,"2":2,"3":2,"4":2,"5":2,"6":2,"7":2,"8":3,"9":3,"10":3,"11":3,"12":3,"13":3,"14":3,"15":3,"16":4,"17":4,"18":4,"19":4,"20":4,"21":4,"22":5,"23":5,"24":5,"25":5,"26":5,"27":5,"28":5,"29":6,"30":6,"31":6,"32":6,"33":6,"34":6,"35":6,"36":6,"37":6,"38":6,"39":6,"40":6,"41":7,"42":7,"43":7,"44":7,"45":7,"46":7,"47":7,"48":8,"49":8,"50":8,"51":8,"52":8,"53":8,"54":8,"55":8,"56":8,"57":8},"category_name":{"0":"Football","1":"Soccer","2":"Baseball & Softball","3":"Basketball","4":"Lacrosse","5":"Tennis & Racquet","6":"Hockey","7":"More Sports","8":"Cardio Equipment","9":"Strength Training","10":"Fitness Accessories","11":"Boxing & MMA","12":"Electronics","13":"Yoga & Pilates","14":"Training by Sport","15":"As Seen on  TV!","16":"Cleats","17":"Men's Footwear","18":"Women's Footwear","19":"Kids' Footwear","20":"Featured Shops","21":"Accessories","22":"Men's Apparel","23":"Women's Apparel","24":"Boys' Apparel","25":"Girls' Apparel","26":"Accessories","27":"Top Brands","28":"Shop By Sport","29":"Men's Golf Clubs","30":"Women's Golf Clubs","31":"Golf Apparel","32":"Golf Shoes","33":"Golf Bags & Carts","34":"Golf Gloves","35":"Golf Balls","36":"Electronics","37":"Kids' Golf Clubs","38":"Team Shop","39":"Accessories","40":"Trade-In","41":"Bike & Skate Shop","42":"Camping & Hiking","43":"Hunting & Shooting","44":"Fishing","45":"Indoor\/Outdoor Games","46":"Boating","47":"Water Sports","48":"MLB","49":"NFL","50":"NHL","51":"NBA","52":"NCAA","53":"MLS","54":"International Soccer","55":"World Cup Shop","56":"MLB Players","57":"NFL Players"}}

#df.to_json(json_file_path, orient = 'records')
#[{"category_id":1,"category_department_id":2,"category_name":"Football"},{"category_id":2,"category_department_id":2,"category_name":"Soccer"},{"category_id":3,"category_department_id":2,"category_name":"Baseball & Softball"},{"category_id":4,"category_department_id":2,"category_name":"Basketball"},{"category_id":5,"category_department_id":2,"category_name":"Lacrosse"},{"category_id":6,"category_department_id":2,"category_name":"Tennis & Racquet"},{"category_id":7,"category_department_id":2,"category_name":"Hockey"},{"category_id":8,"category_department_id":2,"category_name":"More Sports"},{"category_id":9,"category_department_id":3,"category_name":"Cardio Equipment"},{"category_id":10,"category_department_id":3,"category_name":"Strength Training"},{"category_id":11,"category_department_id":3,"category_name":"Fitness Accessories"},{"category_id":12,"category_department_id":3,"category_name":"Boxing & MMA"},{"category_id":13,"category_department_id":3,"category_name":"Electronics"},{"category_id":14,"category_department_id":3,"category_name":"Yoga & Pilates"},{"category_id":15,"category_department_id":3,"category_name":"Training by Sport"},{"category_id":16,"category_department_id":3,"category_name":"As Seen on  TV!"},{"category_id":17,"category_department_id":4,"category_name":"Cleats"},{"category_id":18,"category_department_id":4,"category_name":"Men's Footwear"},{"category_id":19,"category_department_id":4,"category_name":"Women's Footwear"},{"category_id":20,"category_department_id":4,"category_name":"Kids' Footwear"},{"category_id":21,"category_department_id":4,"category_name":"Featured Shops"},{"category_id":22,"category_department_id":4,"category_name":"Accessories"},{"category_id":23,"category_department_id":5,"category_name":"Men's Apparel"},{"category_id":24,"category_department_id":5,"category_name":"Women's Apparel"},{"category_id":25,"category_department_id":5,"category_name":"Boys' Apparel"},{"category_id":26,"category_department_id":5,"category_name":"Girls' Apparel"},{"category_id":27,"category_department_id":5,"category_name":"Accessories"},{"category_id":28,"category_department_id":5,"category_name":"Top Brands"},{"category_id":29,"category_department_id":5,"category_name":"Shop By Sport"},{"category_id":30,"category_department_id":6,"category_name":"Men's Golf Clubs"},{"category_id":31,"category_department_id":6,"category_name":"Women's Golf Clubs"},{"category_id":32,"category_department_id":6,"category_name":"Golf Apparel"},{"category_id":33,"category_department_id":6,"category_name":"Golf Shoes"},{"category_id":34,"category_department_id":6,"category_name":"Golf Bags & Carts"},{"category_id":35,"category_department_id":6,"category_name":"Golf Gloves"},{"category_id":36,"category_department_id":6,"category_name":"Golf Balls"},{"category_id":37,"category_department_id":6,"category_name":"Electronics"},{"category_id":38,"category_department_id":6,"category_name":"Kids' Golf Clubs"},{"category_id":39,"category_department_id":6,"category_name":"Team Shop"},{"category_id":40,"category_department_id":6,"category_name":"Accessories"},{"category_id":41,"category_department_id":6,"category_name":"Trade-In"},{"category_id":42,"category_department_id":7,"category_name":"Bike & Skate Shop"},{"category_id":43,"category_department_id":7,"category_name":"Camping & Hiking"},{"category_id":44,"category_department_id":7,"category_name":"Hunting & Shooting"},{"category_id":45,"category_department_id":7,"category_name":"Fishing"},{"category_id":46,"category_department_id":7,"category_name":"Indoor\/Outdoor Games"},{"category_id":47,"category_department_id":7,"category_name":"Boating"},{"category_id":48,"category_department_id":7,"category_name":"Water Sports"},{"category_id":49,"category_department_id":8,"category_name":"MLB"},{"category_id":50,"category_department_id":8,"category_name":"NFL"},{"category_id":51,"category_department_id":8,"category_name":"NHL"},{"category_id":52,"category_department_id":8,"category_name":"NBA"},{"category_id":53,"category_department_id":8,"category_name":"NCAA"},{"category_id":54,"category_department_id":8,"category_name":"MLS"},{"category_id":55,"category_department_id":8,"category_name":"International Soccer"},{"category_id":56,"category_department_id":8,"category_name":"World Cup Shop"},{"category_id":57,"category_department_id":8,"category_name":"MLB Players"},{"category_id":58,"category_department_id":8,"category_name":"NFL Players"}]

df.to_json(json_file_path, orient = 'records', lines= True)
#{"category_id":1,"category_department_id":2,"category_name":"Football"}
#{"category_id":2,"category_department_id":2,"category_name":"Soccer"}
#{"category_id":3,"category_department_id":2,"category_name":"Baseball & Softball"}
#.
#.
#.
print('success')

