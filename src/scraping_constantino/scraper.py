import os
import requests
import re

from bs4 import BeautifulSoup
from dotenv import load_dotenv
load_dotenv()

base_url = os.getenv("BASEURL")
archive_url = os.getenv("ARCHIVEURL")


def get_latest_link(nth=1):
    archive_page = requests.get(archive_url)
    soup = BeautifulSoup(archive_page.content)
    links = []
    for link in soup.findAll('a', attrs={'href': re.compile("^/audio")}):
        links.append(link.get('href'))

    latest_link = f'{base_url}{links[1-nth]}'

    return latest_link


def get_song_list():
    latest_link = get_latest_link()
    latest_page = requests.get(latest_link)
    soup = BeautifulSoup(latest_page.content)
    song_raw_list = soup.findAll(
        'div', attrs={'class': 'aodHtmlDescription'})[0]

    song_list = [i.replace('\xa0', '').replace('\r', '') for i in song_raw_list.text.split(
        '\n') if(i != 'PLAY' and len(i) > 0 and '\t' not in i)]

    return song_list


if __name__ == '__main__':
    print(get_song_list())
