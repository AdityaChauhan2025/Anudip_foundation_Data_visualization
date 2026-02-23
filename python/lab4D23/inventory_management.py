# inventory_management.py

def manage_inventory(stock):
    # Remove items with 0 stock
    stock = [s for s in stock if s > 0]

    # Restock items below 10
    updated_stock = []
    for s in stock:
        if s < 10:
            s += 50
        updated_stock.append(s)

    total_inventory = sum(updated_stock)

    print("\nUpdated Stock:", updated_stock)
    print("Total Inventory Count:", total_inventory)


stock_input = list(map(int, input("Enter product stock quantities: ").split()))
manage_inventory(stock_input)