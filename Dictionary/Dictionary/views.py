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
        example = ''
        synonyms = []
        definition = ''
        pronunciation = None
        if 'definitions' in results[0]['lexicalEntries'][0]['entries'][0]['senses'][0].keys():
            definition = results[0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0]
        if 'examples' in results[0]['lexicalEntries'][0]['entries'][0]['senses'][0].keys():
            example = results[0]['lexicalEntries'][0]['entries'][0]['senses'][0]['examples'][0]['text']
        if 'synonyms' in results[0]['lexicalEntries'][0]['entries'][0]['senses'][0].keys():
            synonyms_list = results[0]['lexicalEntries'][0]['entries'][0]['senses'][0]['synonyms']
            for item in synonyms_list:
                synonyms.append(item['text'])
        if 'pronunciations' in results[0]['lexicalEntries'][0].keys():
            pronunciation = results[0]['lexicalEntries'][0]['pronunciations'][0]['audioFile']

        return render(request,'index.html',{'definition':definition,'example': example,'synonyms':synonyms,'pronunciation':pronunciation, 'word':word_id})

    return render(request,'index.html')


