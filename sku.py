SKU_FILE="sku_data.txt"

def add_sku(product_id,product_name,product_price):
    '''
    To add a new item in sku
    param product_id:Product ID of item to be added to SKU data file
    param product_name:Product name of item to be added to SKU data file
    param product_price:Product price of item to be added to SKU data file
    '''
    with open(SKU_FILE,'a') as file:
        file.write(f"{product_id}|{product_name}|{product_price}\n")
    print("Product added successfully to SKU data.")
        
def remove_sku(product_id):
    '''
    To remove an item from sku
    param product_id:Product ID of item to be removed from SKU data file
    '''
    with open(SKU_FILE, 'r') as file:
        lines = file.readlines()
    with open(SKU_FILE, 'w') as file:
        for line in lines:
            if line.split('|')[0]!=str(product_id):
                file.write(line)
    print("Product removed successfully from SKU data.")
    
def update_sku(product_id,new_name,new_price):
    '''
    To update an item in the sku
    param product_id:Product ID of item to be updated in SKU data file
    param new_name:Product name of item to be updated in SKU data file
    param new_price:Product price of item to be updated in SKU data file
    '''
    with open(SKU_FILE, 'r') as file:
        lines = file.readlines()
    with open(SKU_FILE, 'w') as file:
        for line in lines:
            if line.split('|')[0]==str(product_id):
                file.write(f"{product_id}|{new_name}|{new_price}\n")
            else:
                file.write(line)
    print("Product updated successfully in SKU data.")
    

        
