import yaml

def read_yaml_file(file_path):
   
    fileyaml = open(file_path, encoding="utf-8")

    read_yaml=fileyaml.read()

    data=yaml.safe_load(read_yaml)

    return data


data = read_yaml_file("jps.yaml")
print(data['数字'][0])
print(data['数字'][1])
print(data['数字'][2])
print(data['列表'][0])
print(data['列表'][1])
print(data['列表'][2])