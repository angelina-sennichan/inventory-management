REPORT_FILE="report.txt"

def inventory_summary_report(sku_list,inv_list):
    '''
    param sku_list:list of each line of SKU data file
    param inv_list:list of each line of Inventory data file
    '''
    with open(REPORT_FILE, 'w') as file:
        file.write("Summary of current inventory levels for all SKUs:\n")
        print("Summary of current inventory levels for all SKUs:")
        file.write("Product ID|Product Name|Product Price|Product Quantity|Product Reorder level\n")
        print("Product ID|Product Name|Product Price|Product Quantity|Product Reorder level")
        for line1 in sku_list[1:]:
            for line2 in inv_list[1:]:
                sku=line1.strip().split("|")
                inv=line2.strip().split("|")
                if(sku[0]==inv[0]):
                    file.write(sku[0]+"|"+sku[1]+"|"+sku[2]+"|"+inv[1]+"|"+inv[2])
                    print(sku[0]+"|"+sku[1]+"|"+sku[2]+"|"+inv[1]+"|"+inv[2])
                
def total_inventory_value_report(sku_list,inv_list):
    '''
    param sku_list:list of each line of SKU data file
    param inv_list:list of each line of Inventory data file
    '''
    total_value=0
    with open(REPORT_FILE, 'w') as file:
        for line1 in sku_list[1:]:
            for line2 in inv_list[1:]:
                sku=line1.strip().split("|")
                inv=line2.strip().split("|")
                if(sku[0]==inv[0]):
                    total_value+=int(sku[2])*int(inv[1])
        file.write("Total value of the entire inventory:"+str(total_value))
        print("Total value of the entire inventory:"+str(total_value))
    
def low_stock_alert_report(sku_list,inv_list):
    '''
    param sku_list:list of each line of SKU data file
    param inv_list:list of each line of Inventory data file
    '''
    low_stock={}
    with open(REPORT_FILE, 'w') as file:        
        for line1 in sku_list:
            sku=line1.strip().split("|")
            for line2 in inv_list:
                inv=line2.strip().split("|")
                if(sku[0]==inv[0] and int(inv[1])<=int(inv[2])):
                    low_stock[sku[1]]=inv[1]
                    
        if not low_stock:
            file.write("No sku has low stock")
            print("No sku has low stock")
        else:
            file.write("List of sku's having low stock\n")
            print("List of sku's having low stock")
            file.write("Product Name|Product Quantity\n")
            print("Product Name|Product Quantity")
            for low in low_stock:
                file.write(low+"|"+low_stock[low]+"\n")
                print(low+"|"+low_stock[low])
                              
                              
                              

