import json
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

r = requests.get('https://pokeapi.co/api/v2/ability/51/')

resultContent = json.loads(r.content)
abilityNameFormatted = resultContent['name'].split("-")[0].capitalize() + " " + resultContent['name'].split("-")[
    1].capitalize()
resultContent = resultContent['pokemon']

lastResult = resultContent[len(resultContent) - 1]

nameOfPokemon = lastResult['pokemon']['name']
pokemonNameFormatted = nameOfPokemon.split("-")[0].capitalize() + " " + nameOfPokemon.split("-")[1].capitalize()

print len(resultContent), "pokemon are able to use the", abilityNameFormatted, "ability"
print "We're now going to perform a google search on the", pokemonNameFormatted, "pokemon, and confirm that the name of the pokemon is in each search result"
print ""

driver = webdriver.Chrome()
driver.get("http://www.google.com")

assert "Google" in driver.title

element = driver.find_element_by_css_selector("[name='q']")
element.clear()
element.send_keys(nameOfPokemon)
element.send_keys(Keys.RETURN)

element = driver.find_elements_by_css_selector("div.r")

for searchResults in element:
    elementText = searchResults.text.split("https")[0].strip('\n')
    try:
        assert nameOfPokemon.lower() in elementText.lower()
    except:
        driver.close()
        print ("Assertion failure for checking that", nameOfPokemon, "is present in all of the search results")

driver.close()