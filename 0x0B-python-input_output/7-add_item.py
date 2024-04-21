#!/usr/bin/python3
"""Task 7 of ALX python input and output project

A script that adds all arguments to a python list
and save them to a file.
"""
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


try:
    itemList = load_from_json_file("add_item.json")
except ValueError:
    itemList = []

itemList.extend(sys.argv[1:])
save_to_json_file(itemList, "add_item.json")
