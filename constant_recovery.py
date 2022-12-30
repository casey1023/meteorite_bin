import json
import setting 

with open('constant_fixed.json', 'r') as f:
    constantfile = json.load(f)

setting.writeconstant(constantfile)