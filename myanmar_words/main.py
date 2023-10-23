import json
import re
from pkg_resources import resource_filename

# Get the absolute path to the JSON file using pkg_resources
def get(type):
    absolute_path = resource_filename(__name__, f'data/{type}.json')
    try:
        with open(absolute_path, 'r', encoding='utf-8') as json_file:
            return json.load(json_file)
    except: return ["Invalid type!"]

def find(string):
    words = get("all")
    result = []
    start = 0
    while start < len(string):
        for word in words:
            if string[start:].startswith(word):
                result.append(word)
                start += len(word)
                break
        else:
            start += 1
    return result

def append_and_return(arr, element):
    arr.append(element)
    return arr

def exclude_element(arr, element_to_exclude):
    return [x for x in arr if x != element_to_exclude]

def brake(text, no_spaces=True):
    pattern = f"({'|'.join(map(re.escape,append_and_return(find(text),' ')))})"
    substrings = re.split(pattern, text)
    [substring for substring in substrings if substring]
    substrings=exclude_element(substrings,' ') if no_spaces else substrings
    return exclude_element(substrings,'')

def count(text, no_spaces=True):
    return len(brake(text, no_spaces))
