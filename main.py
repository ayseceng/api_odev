import requests
URL = "https://openlibrary.org/search/authors.json?q=j%20k%20rowling"
result = requests.get(URL)
data = result.json()
print(data)
