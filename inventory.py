INV_FILE="inventory_data.txt"

def add_inv(product_id,product_quantity,product_reorder):
    '''
    param product_id:Product ID of item to be added to Inventory data file
    param product_quantity:Product quantity of item to be added to Inventory data file
    '''
    with open(INV_FILE,'a') as file:
        file.write(f"{product_id}|{product_quantity}|{product_reorder}\n")
    print("sku quantity added successfully to INVENTORY data.")
    
def remove_inv(product_id):
    '''
    param product_id:Product ID of item to be removed from Inventory data file
    '''
    with open(INV_FILE,'r') as file:
        lines = file.readlines()
    with open(INV_FILE,'w') as file:
        for line in lines:
            if line.split('|')[0]!=str(product_id):
                file.write(line)
    print("sku quantity removed successfully from INVENTORY data.")

def update_inv(product_id,new_quantity,new_reorder):
    '''
    param product_id:Product ID of item to be updated in Inventory data file
    param new_product_quantity:Product quantity of item to be updated in Inventory data file
    '''
    with open(INV_FILE,'r') as file:
        lines = file.readlines()
    with open(INV_FILE,'w') as file:
        for line in lines:
            if line.split('|')[0]== str(product_id):
                file.write(f"{product_id}|{new_quantity}|{new_reorder}\n")
            else:
                file.write(line)
    print("sku quantity updated successfully in INVENTORY data.")
    


