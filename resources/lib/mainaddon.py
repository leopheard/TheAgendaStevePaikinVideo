import requests
import re
from bs4 import BeautifulSoup

def get_soup(URL0):
    page = requests.get(URL0)
    soup = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup))
    return soup
get_soup("http://feeds.tvo.org/tvo/TxZN")


def get_playable_podcast(soup):
    subjects = []
    for content in soup.find_all('item'):
        try:        
            link = content.find('media:content')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
#            desc = content.find('description')
#            desc = desc.get_text()
#            thumbnail = content.find('media:thumbnail')
#            thumbnail = thumbnail.get('url')
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
#                'desc': desc,
                'thumbnail': "http://podcasts.tvo.org/theagenda/images/agenda_1400_201602.jpg",
        }
        subjects.append(item) 
    return subjects
def compile_playable_podcast(playable_podcast):
    items = []
    for podcast in playable_podcast:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
#            'info': podcast['desc'],
            'is_playable': True,
    })
    return items

def get_playable_podcast1(soup):
    subjects = []
    for content in soup.find_all('item', limit=40):
        try:        
            link = content.find('media:content')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
#            desc = content.find('description')
#            desc = desc.get_text()
            thumbnail = content.find('media:thumbnail')
            thumbnail = thumbnail.get('url')
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'desc': desc,
                'thumbnail': "http://podcasts.tvo.org/theagenda/images/agenda_1400_201602.jpg",
        }
        subjects.append(item) 
    return subjects
def compile_playable_podcast1(playable_podcast1):
    items = []
    for podcast in playable_podcast1:
        items.append({
            'label': podcast['title'],
            'path': podcast['url'],
            'thumbnail': podcast['thumbnail'],
#            'info': podcast['desc'],
            'is_playable': True,
    })
    return items

