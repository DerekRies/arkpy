import requests
import json

from bs4 import BeautifulSoup


def scrape_creatures():
    print 'scraping creatures'
    url = 'http://ark.gamepedia.com/Entity_IDs'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    tables = soup.find_all('table')
    creature_table = tables[2]
    container = {}
    creatures = []

    for row in creature_table.find_all('tr')[1:]:
        cols = row.find_all('td')
        creature = {
            'name': cols[2].a.string,
            'category': cols[3].a.string,
        }
        try:
            creature['icon'] = cols[0].div.div.a.img['src']
        except:
            creature['icon'] = None
        try:
            creature['id'] = cols[4].string
        except:
            creature['id'] = None
        try:
            creature['path'] = cols[5].font.string
        except:
            creature['path'] = None
        creatures.append(creature)
    container['creatures'] = creatures
    with open('data/entity_ids_creatures.json', 'w') as ofile:
        ofile.write(json.dumps(container, indent=4,
                               separators=(',', ': ')))


def scrape_items():
    print 'scraping items'
    url = 'http://ark.gamepedia.com/Entity_IDs'
    r = requests.get(url)
    print r
    soup = BeautifulSoup(r.text, 'html.parser')
    tables = soup.find_all('table')

    container = {}
    items = []
    item_table = tables[0]
    for row in item_table.find_all('tr')[1:]:
        cols = row.find_all('td')
        item = {
            'icon': cols[0].div.div.a.img['src'],
            # 'id': int(cols[1].string),
            'name': cols[2].a.string,
            'category': cols[3].a.string,
            # 'path': cols[5].font.string
        }
        try:
            item['id'] = int(cols[1].string)
        except:
            item['id'] = None

        try:
            item['path'] = cols[5].font.string
        except:
            item['path'] = ''

        items.append(item)
    # print items
    container['items'] = items
    with open('data/entity_ids_items.json', 'w') as ofile:
        ofile.write(json.dumps(container, indent=4,
                               separators=(',', ': ')))


def main():
    # scrape_items()
    scrape_creatures()


if __name__ == '__main__':
    main()
