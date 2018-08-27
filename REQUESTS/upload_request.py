#!/usr/bin/python3
import requests
import sys
import random
import logging

def get_content(file="aaaaa"):
    url = "https://uploadfiles.io/" + file
    #print(url)
    content = requests.get(url).text
    return content

def elements_str():
    alphabet = "".join([chr(x) for x in range(97, 123)])
    numbers = "".join([str(x) for x in range(0,10)])
    signs = alphabet + numbers
    return signs

def random_signs(elements, l):
    phrase = "".join([random.choice(elements) for x in range(l)])
    return phrase


if __name__ == "__main__":
    elements = elements_str()
    for x in range(100):
        file = random_signs(elements, 5)
        content = get_content(file)
        if "404.gif" in content:
            print(file, " | ", False)
        else:
            if "This file has expired and been automatically deleted" in content:
                print(file, " |>> Deleted")
            else:
                print(file, " |>>>>> Found file!")
