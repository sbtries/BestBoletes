import requests
from bs4 import BeautifulSoup 
import json 

boletes = []
page_num = 1
counter = 1

# while page_num < 22: 
while page_num < 2:
    link = "https://boletes.wpamushroomclub.org/page" + str(page_num)
    page = requests.get(link)
    print('page', page)
    print('content', page.content)
    soup = BeautifulSoup(page.content, 'html5lib')
    print(page.status_code)
    print(link)

    all_boletes = soup.findAll('li', attrs = {"class":"product"})
    for item in all_boletes:
        item_dict = {}
        item_dict['model'] = "boletes.bolete"
        item_dict['pk'] = counter
        item_dict['fields'] = {}
        item_dict['fields']['name'] = item.h2.text
        item_dict['fields']['name'] = item_dict['fields']['name'].encode("ascii", "ignore").decode('utf-8')
        item_dict['fields']['description'] = item.p.text
        item_dict['fields']['description'] = item_dict['fields']['description'].encode("ascii", "ignore").decode('utf-8')

        link = item.a['href']
        # link = 'https://boletes.wpamushroomclub.org/product/'+ name + '/'
        response = requests.get(link)
        print(link, response.status_code)
        if response.status_code ==200:
            # item_dict['additional'] = {}
            smallsoup = BeautifulSoup(response.content, 'html5lib')
            xtra_info = smallsoup.find('div', attrs = {"id":"tab-description"})
            if xtra_info:
                tags = xtra_info.findAll('p')
                lists = xtra_info.findAll('ul')
                for tag in tags:
                    text = tag.text
                    # print(text)
                    split = text.split(":", 1)
                    if len(split) == 2:
                        item_dict['fields'][split[0]] = split[1].encode("ascii", "ignore").decode('utf-8')
            # if lists[0]:
            #     for item in lists[0]:
            #         split = text.split(":", 1)
            #     if len(split) == 2:
            #         item_dict['additional']['CHEMICAL TESTS'][split[0]] = split[1] 
            # if lists[1]:
            #     for item in lists[1]:
            #         item_dict['additional']['CHEMICAL TESTS']['link'] = item.li.text

                
        # print(item_dict)

        boletes.append(item_dict)
        counter += 1
    page_num += 1


    
print('LENGTH', len(boletes))       
with open ('boletes.json', 'w') as f: 
    json.dump(boletes, f)


# abrubtibulbus
# abruptibulbus

# https://boletes.wpamushroomclub.org/product/boletus-abrubtibulbus/
# https://boletes.wpamushroomclub.org/product/boletus-abruptibulbus/