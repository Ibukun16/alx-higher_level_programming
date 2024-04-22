#!/usr/bin/python3
"""Task 7 of ALX python input/output project

A script that adds all arguments to a python list, and save
them to a file.
"""
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

open("add_item.json", "a", encoding="utf-8")

try:
    newfile = load_from_json_file("add_item.json")
except ValueError:
    newfile = []

for i in sys.argv[1:]:
    newfile.append(i)

save_to_json_file(newfile, "add_item.json")
