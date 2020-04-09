from django.shortcuts import render

import requests
import json

app_id = "050970e7"
app_key = "863d4f01d8a7e5b8aa359bbe9c9436aa"
language = "en-gb"

def index(request):
    if request.method == 'POST':
        data = request.POST.copy()
        word_id = data.get('word')
        url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()
        r = requests.get(url, headers={"app_id": app_id, "app_key": app_key})

        results = r.json()['results']
        # print(json.dumps(results,indent=2,sort_keys=True))

        definition = results[0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0]
        example = results[0]['lexicalEntries'][0]['entries'][0]['senses'][0]['examples'][0]['text']
        synonyms = results[0]['lexicalEntries'][0]['entries'][0]['senses'][0]['synonyms']
        pronunciation = results[0]['lexicalEntries'][0]['pronunciations'][0]['audioFile']

        return render(request,'index.html',{'definition':definition,'example': example,'synonyms':synonyms,'pronunciation':pronunciation})

    return render(request,'index.html')


