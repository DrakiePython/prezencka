"""Functions to keep track and alter inventory."""

def create_inventory(items:list)->dict:
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """
    
    counts = {}
    for item in items:
        counts[item] = counts.get(item, 0) + 1
#   counts = {item: items.count(item) for item in set(items)}
    return counts
    



def add_items(inventory:dict, items:list)->dict:
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """
    for item in items:
        inventory.setdefault(item, 0)
        inventory[item] += 1     
    return inventory



def decrement_items(inventory:dict, items:list)->dict:
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """

    for item in items:
        if item in inventory:
            inventory[item] = max(inventory[item] - 1, 0)           
    return inventory



def remove_item(inventory:dict, items:list)->dict:
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """
    inventory.pop(items, None)
    return inventory

def list_inventory(inventory:dict)->list:
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """
    return list(filter(lambda item: item[1] > 0, inventory.items()))
#   return [(item, count) for item, count in inventory.items() if count > 0] -> item comprehension

