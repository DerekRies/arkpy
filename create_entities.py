import json
import random

from arkpy import utils
from enum import Enum, IntEnum


# Documentation paragraph for Entities Enums/Maps
docs_msg = """
[Source Code](https://github.com/DerekRies/arkpy/blob/master/arkpy/entities.py)

The Entities Enums and Maps are for easily obtaining the long, complicated
paths that make up the entity path used by the game to represent items.
Entities are broken down first into two categories, `Items` and `Creatures`,
which are further broken down into the categories below.


### Example:
```python
from arkpy import entities

for trophy in entities.Trophy:
    print trophy
    print trophy.value

# Trophy.Alpha_Rex_Trophy
# BlueprintGeneratedClass ..PrimalItemTrophy_AlphaRex.PrimalItemTrophy_AlphaRex
# Trophy.Broodmother_Trophy
# BlueprintGeneratedClass ..PrimalItemTrophy_Broodmother.PrimalItemTrophy_Broodmother
# Trophy.Dragon_Trophy
# BlueprintGeneratedClass ..PrimalItemTrophy_Dragon.PrimalItemTrophy_Dragon
# Trophy.Megapithecus_Trophy
# BlueprintGeneratedClass ..PrimalItemTrophy_Gorilla.PrimalItemTrophy_Gorilla
```
"""


def main():
    items = None
    with open('data/entity_ids_items.json', 'r') as ifile:
        items = json.load(ifile)
        items = items['items']
    categories = {}
    for item in items:
        cat = item.get('category', 'Other')
        if cat == 'Weapon':
            cat = 'Weapons'
        if cat not in categories:
            categories[cat] = []
        name = item.get('name', '')
        name = name.replace(' ', '_')
        name = name.replace(':', '_')
        name = name.replace('-', '_')
        name = name.replace('\'', '')
        name = name.replace('(', '')
        name = name.replace(')', '')
        path = item.get('path', '')
        if '"' not in path:
            path = '""'
        else:
            path = path.replace('Blueprint', 'BlueprintGeneratedClass ', 1)
            path = path.replace('\'', '')
        val = (name, path)
        categories[cat].append(val)
    with open('arkpy/entities.py', 'w') as ofile:
        ofile.write('from enum import Enum\n\n')
        for key in categories.keys():
            ofile.write('class %s(Enum):\n' % key)
            for item in categories[key]:
                # print item
                line = '    %s = %s\n' % item
                ofile.write(line)
            ofile.write('\n\n')
        ofile.write('\n')
    with open('docs/entities.md', 'w') as ofile:
        ofile.write('# Entities Enums/Maps\n\n')
        ofile.write(docs_msg)
        ofile.write('- - -\n\n')
        ofile.write('# Items\n\n')
        ofile.write('- - -\n\n')
        for key in categories.keys():
            prefix = categories[key][0][1].split('/')[:-1]
            prefix = '/'.join(prefix)
            l = len(prefix)

            ofile.write('## `%s` Class\n\n' % key)
            ofile.write('### extends `enum.Enum`\n\n')
            ofile.write('**Path prefix:** `%s`\n\n' % prefix)

            ofile.write('| Name | Path (Value) |\n')
            ofile.write('|------|--------------|\n')
            for item in categories[key]:
                path = item[1][l:]
                ofile.write('| **%s** | %s |\n' % (item[0], path))
            ofile.write('\n\n')

if __name__ == '__main__':
    main()
