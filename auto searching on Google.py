#!/usr/bin/env python
# coding: utf-8

try: 
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")

#to search
query = "full leaf green tea"

import webbrowser

for link in search(query, tld="co.in",stop=None,num=10, pause=5):
    if 'ivystea'in link:
        print(link)
        webbrowser.open(link)
        break;
