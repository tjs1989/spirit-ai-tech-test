from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import requests
import json

r = requests.get('https://pokeapi.co/api/v2/ability/51/')

resultContent = json.loads(r.content)

abilityName = resultContent['name']

resultContent = resultContent['pokemon']

lastResult = resultContent[len(resultContent) -1]

pokemonName = lastResult['pokemon']['name']

print len(resultContent), "pokemon are able to use the", abilityName, "ability"
print "We're now going to perform a google search on the last one in that list, which is the", pokemonName, "pokemon"

driver = webdriver.Chrome()
driver.get("http://www.google.com")

assert "Google" in driver.title
elem = driver.find_element_by_css_selector("[name='q']")
elem.clear()
elem.send_keys(pokemonName)
elem.send_keys(Keys.RETURN)

elem = driver.find_elements_by_css_selector("div.r")

for items in elem:
    elem = items.text
    print elem


assert "No results found." not in driver.page_source
driver.close()