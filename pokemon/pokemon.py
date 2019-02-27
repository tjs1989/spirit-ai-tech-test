# try:
#     from googlesearch import search
# except ImportError:
#     print("No module named 'google' found")
#
# # to search
# query = "something"
#
# for j in search(query, tld="co.uk",start=0,stop=10):
#     print(j)

import requests
import json

r = requests.get('https://pokeapi.co/api/v2/ability/51/')

resultContent = json.loads(r.content)

# resultContent = resultContent['pokemon']

resultContent = resultContent['pokemon']

lastResult = resultContent[len(resultContent) -1]

print lastResult

print lastResult['pokemon']['name']

# text = "bill,bob,ben"
# print text.split(",")[1]
