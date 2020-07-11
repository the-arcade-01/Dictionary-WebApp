import requests
import json

app_id = "050970e7"
app_key = "863d4f01d8a7e5b8aa359bbe9c9436aa"
language = "en-gb"
word_id = "example"

url = (
    "https://od-api.oxforddictionaries.com:443/api/v2/entries/"
    + language
    + "/"
    + word_id.lower()
)
r = requests.get(url, headers={"app_id": app_id, "app_key": app_key})

results = r.json()
# print(json.dumps(results,indent=2,sort_keys=True))

definition = results[0]["lexicalEntries"][0]["entries"][0]["senses"][0]["definitions"][
    0
]
example = results[0]["lexicalEntries"][0]["entries"][0]["senses"][0]["examples"][0][
    "text"
]
synonyms_list = results[0]["lexicalEntries"][0]["entries"][0]["senses"][0]["synonyms"]
pronunciation = results[0]["lexicalEntries"][0]["pronunciations"][0]["audioFile"]

print(definition)
print(example)
print(pronunciation)
for item in synonyms:
    print(item)
