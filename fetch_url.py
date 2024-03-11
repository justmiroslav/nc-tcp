import requests

country_language_dict = {}
url = 'https://restcountries.com/v3.1/all'
response = requests.get(url)
data = response.json()

for entity in data:
    country_name = entity['name']['common']
    country = country_name.title().replace(" ", "")
    country_languages = entity['languages'] if country != "Antarctica" else {'nol': "No official language"}
    languages = [lang for lang in country_languages.values()]
    country_language_dict[country] = languages
