# Eventually to do this: 
# var storyBody = document.getElementsByClassName('story-body-text')
# for (var i = 0; i < storyBody.length; i++){console.log(storyBody[i].innerText);}

import requests
import os

url = 'https://www.nytimes.com/2017/12/28/business/media/alphonso-app-tracking.html'
r = requests.get(url)

print("Status:", r.status_code)
content = str(r.content)
with open('nyt_article.html', 'w') as file_obj:
    file_obj.write(content)