from bs4 import BeautifulSoup
import requests
import json

def gather_urls():
    r = requests.get("http://www.politico.com/")
    soup = BeautifulSoup(r.text, 'html.parser')
    divs = soup.find_all('div', class_='fig-graphic')
    return [div.find('a')['href'] for div in divs if div.find('a')]

def parse_data(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    created_at = soup.find('p', class_='timestamp').find('time')['datetime']
    updated_at = soup.find('p', class_='updated').find('time')['datetime']
    js_string = soup.findAll('script')[13].string.split(';')[0].split('= ')[1].strip()
    data = json.loads(js_string)
    data['created_at'] = created_at
    data['updated_at'] = updated_at
    return data
