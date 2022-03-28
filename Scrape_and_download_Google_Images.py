#EN: Scrape and download Google Images with Python by SerpApi
#TR: python dili kullanarak ve SerpApi vasitasıyla Google images den resimleri çekme ve indirme 
#AR: باستعمال لغة بايثون "SarpApi"استخراج الصور وتنزيلها من"صور غوغل " بواسطة   

from serpapi import GoogleSearch
import requests

GoogleSearch.SERP_API_KEY = "f6d663513191c06dbb40f77b93a95047441ee02c866563c89702e5d66c547" #please enter viled key from --> https://serpapi.com/
counter=0

for i in range(100):
    search = GoogleSearch({"q": "face mask", "tbm": "isch", "ijn":str(i)})                  #Enter what you want searching - ex: face mask
    #print(search.get_dict())
    for image_result in search.get_dict()['images_results']:
        link = image_result["original"]
        print(str(counter)+"link: " + link)
        counter=counter+1
        
        file_name=str(counter)+"photo.jpg"
        with open(file_name, 'wb') as file:
            file.write(requests.get(link).content)
        
        
