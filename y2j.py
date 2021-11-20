import json
import yaml
import os

def yaml_to_json(file_path: str):
    with open(file_path, 'r') as f:
        output_file = open(os.path.basename(file_path).replace(".yaml","")+'.json','w')
        #file_content = open(file_path,'r')
        output_file_content = yaml.load(f, Loader=yaml.FullLoader)
        json.dump(output_file_content, output_file)
        output_file.close()


yaml_to_json('verify.yaml')
yaml_to_json('xmas.yaml')