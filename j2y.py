import json
import yaml
import os

def json_to_yaml(file_path: str):
    with open(file_path,) as f:
        output_file_content = {}
        output_file = open(os.path.basename(file_path).replace(".json","")+'.yaml','w')
        output_file_content = json.load(f)
        yaml.dump(output_file_content, output_file)
        output_file.close()

json_to_yaml('donuts.json')
json_to_yaml('emojis.json')