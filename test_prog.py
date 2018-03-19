import yaml
import json

my_list = range(5)
my_list.append({})

my_list[-1] = {"ip_address": "10.10.10.10", "new": True}

with open("file.yml", "w") as f:
  f.write(yaml.dump(my_list, default_flow_style=True))

with open("file.json", "w") as f:
  json.dump(my_list, f)
