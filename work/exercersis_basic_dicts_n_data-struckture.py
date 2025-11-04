items = {'rope': 1, 'torch': 6, 'gold coin':
42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def items_display(items):
    sum = 0
    print("Inventory")
    for key, value in items.items():
        print(f'{value}: {key}')
        sum += value
    print(f'Sum of Items: {sum}')

items_display(items)

def addToInventory( inventar: dict, loot:list)->dict:
    new_inventory = inventar.copy()
    for item in loot:
        if item  in new_inventory.keys():
            new_inventory[item] += 1
        else:
            new_inventory[item] = 1
    return new_inventory

inv = addToInventory(items, dragonLoot)
items_display(inv)