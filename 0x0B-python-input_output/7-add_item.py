#!/usr/bin/python3
"""
Load, add, save task
"""
import sys
from json import load, dump

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if __name__ == "__main__":
    try:
        lst = load_from_json_file("add_item.json")
    except FileNotFoundError:
        lst = []

    for av in sys.argv[1:]:
        lst.append(av)

    save_to_json_file(lst, "add_item.json")
