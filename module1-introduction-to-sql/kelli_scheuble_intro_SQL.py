import sqlite3

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


# 2
# find total characters in each specific subclass

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
curs_items.close()
conn.commit()

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

# 6 find number of weapons each character has
# returns first 20 rows

# 7 find average number of items the characters have



