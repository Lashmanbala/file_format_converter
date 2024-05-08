import glob
import json

src_file_names = glob.glob('data/retail_db/*/part-*', recursive=True)  # ** is to access all the files and folders
#print(src_file_names)

schema = json.load(open('data/retail_db/schemas.json'))
#print(schema['departments'])