"""Functions to manage a user's shopping cart items."""

from collections.abc import Iterable
def add_item(current_cart:dict, items_to_add:Iterable[list])->dict:
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """
    for item in items_to_add:
        current_cart.setdefault(item, 0) 
        current_cart[item] += 1
    return current_cart
     


def read_notes(notes:Iterable[list])->dict:
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """
    
    return dict.fromkeys(notes, 1)


def update_recipes(ideas:dict, recipe_updates:Iterable[list])->dict:
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: iterable -  with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.


        Using **kwargs    
    updated_rec = {**ideas, **recipe_updates}
    return updated_rec
  
    """
    ideas.update(recipe_updates) 
    # writing updated_'dict' = ... returns None as gotcha!!!!
    return ideas


def sort_entries(cart:dict)->dict:
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """
    sorted_cart = dict(sorted(cart.items()))
    return sorted_cart


def send_to_store(cart:dict, aisle_mapping:dict)->dict:
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """
    fulfill_cart = {}                                        # empty dict keys = items and values = count, aisle, refrigerated
    for item, count in sorted(cart.items(), reverse=True):   # Key:Value from cart.items reverse-sorted 
        aisle, refrigerated = aisle_mapping[item]            # for looking up the aisle and refrig info contained in aisle_mapping for each item
        fulfill_cart[item] = [count, aisle, refrigerated]    # adding to the fulfif cart, aka Value of the final dict
        
    return fulfill_cart


def update_store_inventory(fulfillment_cart:dict, store_inventory:dict)->dict:
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """
    # creating a new dictionary, so I don't mutate the originl store_inventory 
    upd_store_inv = {}
    # iterating over store_inventory for each item and unpacked store_inventory
    for item, (store_count, aisle, refrigerated) in store_inventory.items():
        # condition if the item was bought
        if item in fulfillment_cart:           
            # defining cart_count equals to item, [count] in fullfil_cart
            cart_count = fulfillment_cart[item][0]
            #substracting what is in the store with what is in the cart
            new_count = store_count - cart_count
            # if the new_count equals 0, replace 0 with string
            if new_count == 0:
                new_count = 'Out of Stock'
        # and if the item is NOT in cart, the store_inventory's item count is unchanged
        else:
            new_count = store_count
        # creates or overwrites item dictionary[key]=value where the value is updated, unpacked store_inventory where aisle and refrigerated is the same
        upd_store_inv[item] = [new_count, aisle, refrigerated]   
        
    return upd_store_inv
