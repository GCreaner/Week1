import yaml
import json
from pprint import pprint

with open("file.json") as f:
  json_list = json.load(f)

with open("file.yml") as f:
  yaml_list = yaml.load(f)

print "JSON List"
pprint(json_list)

print "YAML List"
pprint(yaml_list)
