'''
The Inventory Management System helps manage a store's inventory by adding items, updating stock, checking availability, and generating sales reports. 
'''
inventory = {}

def add_item(item,price,stock):
    if item in inventory.keys():
        print(f"Error: Item '{item}' already exists.")
    else:
        inventory[item] = {
            'price':price,
            'stock':stock
        }
        print(f"Item '{item}' added successfully.")

def update_stock(item,quantity):
    if item not in inventory.keys():
        print(f"Error: Item '{item}' not found.")
    else:
        newStock = inventory[item]['stock']+quantity
        if newStock <0:
            print(f"Error: Insufficient stock for '{item}'.")
        else:
            inventory[item]['stock'] = newStock 
            print(f"Stock for '{item}' updated successfully.")

def update_stock_sales(item,quantity):
    if item not in inventory.keys():
        print(f"Error: Item '{item}' not found.")
    else:
        newStock = inventory[item]['stock']-quantity
        if newStock <0:
            print(f"Error: Sales quanyity is more than number of items in stock'{item}'.")
        else:
            inventory[item]['stock'] = newStock 
        
        
def check_availability(item):
    if item not in inventory.keys():
        return ("Item not found")
    else:
        return ( int(inventory[item]['stock']) )

def sales_report(sales):
    totalRevenue = 0.0
    for key,quantity in sales.items():
        if ( check_availability(key)=='Item not found' ):
            print(f"Error: Item '{key}' not found.")
        elif ( int(inventory[key]['stock']) - int(quantity)<0 ):
            print(f"Error: Insufficient stock for '{inventory[key]['stock']}'.")
        else:
            totalRevenue = totalRevenue+( quantity*inventory[key]['price'] )
            update_stock_sales(key,quantity)
    return(f"Total revenue: ${totalRevenue:.2f}")

add_item("Apple", 0.5, 50)
add_item("Banana", 0.2, 60)
sales = {"Apple": 30, "Banana": 20, "Orange": 10}  # Orange should print an error
print(sales_report(sales))  # Should output: 19.0
print(inventory)
