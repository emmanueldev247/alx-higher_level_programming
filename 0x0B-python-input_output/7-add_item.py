#!/usr/bin/python3
"""Create a function that creates an Object from a “JSON file”
"""


import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"
length = len(sys.argv)

try:
    args_list = load_from_json_file(filename)
except BaseException:
    args_list = []
for i in range(1, length):
    args_list.append(sys.argv[i])

save_to_json_file(args_list, filename)
