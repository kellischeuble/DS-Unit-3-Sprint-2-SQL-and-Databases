import sqlite3
import pandas as pd

# 1
# find total characters
# form a connection object
conn = sqlite3.connect('rpg_db.sqlite3')
# get cursor for the connection
# this will act as a pointer to a place in the data base
curs = conn.cursor()
curs.execute('''
SELECT COUNT(distinct character_id) as character_id
FROM charactercreator_character;
''')
curs.close()
conn.commit()
# -------------------------------- #


# 2
# find total characters in each specific subclass
characters = ['cleric', 'fighter', 'mage', 'necromancer', 'thief']
for character in characters:
    curs_character = conn.cursor()
    if character == 'necromancer':
        curs_character.execute(f'''
        SELECT COUNT(mage_ptr_id)
        FROM charactercreator_{character}
        ''')
    else:
        curs_character.execute(f'''
        SELECT COUNT(character_ptr_id) 
        FROM charactercreator_{character}
        ''')
    print(f"Number of {character}s:", curs_character.fetchone()[0])
    curs_character.close()
    conn.commit()
# -------------------------------- #


# 3 
# find total items
# get a different cursor because we need a new one for each
# query
# this will act as a pointer 'armory_item'
curs_items = conn.cursor()
curs_items.execute('''
SELECT COUNT(distinct item_id)
FROM armory_item;
''')
items = curs_items.fetchone()[0]
curs_items.close()
conn.commit()
print(items)
# -------------------------------- #


# 4
# find total characters in each specific subclass
# get a different cursor 
# this will act as a pointer 'armory_weapon'
curs_weapons = conn.cursor()
curs_weapons.execute('''
SELECT COUNT(item_ptr_id)
FROM armory_weapon;
''')
weapons = curs_weapons.fetchone()[0]
curs_items.close()
conn.commit()
print(weapons)
# -------------------------------- #


# from lecture:
# SELECT 
#  sum(w.item_ptr_id is null) as non_weapon_count
#  ,sum(w.item_ptr_id is not null) as weapon_count
# FROM armory_item i
# LEFT JOIN armory_weapon w ON i.item_id = w.item_ptr_id

# -------------------------------- #


# 5 find number of items each character has
# returns first 20 rows
curs_items_per_character = conn.cursor()
curs_items_per_character.execute('''
SELECT
character_id,
count(distinct item_id)
FROM charactercreator_character_inventory
GROUP BY character_id
LIMIT 20
''')
curs_items_per_character.close()
conn.commit()
# -------------------------------- #


# 6 find number of weapons each character has
# returns first 20 rows

# From class.. 
# SELECT
#   c.character_id
#   ,c.name as char_name
#   ,count(inv.item_id) as item_count
#   ,count(w.item_ptr_id) as weapon_count
# FROM charactercreator_character c
# LEFT JOIN charactercreator_character_inventory inv ON inv.character_id = c.character_id
# LEFT JOIN armory_weapon w on inv.item_id = w.item_ptr_id
# GROUP BY c.character_id
# ORDER BY weapon_count DESC
# LIMIT 20
# -------------------------------- #


# 7 find average number of items the characters have

# -------------------------------- #

