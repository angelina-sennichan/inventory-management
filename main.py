from sku import *
from inventory import *
from report import *

SKU_FILE="sku_data.txt"
INV_FILE="inventory_data.txt"

class ProductIDEmptyError(Exception):
    pass

class ProductIDNegativeError(Exception):
    pass

class ProductIDTypeError(Exception):
    pass

class ProductIDExistsError(Exception):
    pass

class ProductIDDoesNotExistError(Exception):
    pass

class ProductNameEmptyError(Exception):
    pass

class ProductPriceEmptyError(Exception):
    pass

class ProductPriceTypeError(Exception):
    pass

class ProductPriceNegativeError(Exception):
    pass

class ProductQuantityEmptyError(Exception):
    pass

class ProductQuantityTypeError(Exception):
    pass

class ProductQuantityNegativeError(Exception):
    pass

class ProductReOrderEmptyError(Exception):
    pass

class ProductReOrderTypeError(Exception):
    pass

class ProductReOrderNegativeError(Exception):
    pass

class SkuFileEmptyError(Exception):
    pass

class InvFileEmptyError(Exception):
    pass

class SameIdListsError(Exception):
    pass

def sku_file_lines():
    '''This function returns the Product IDs present in sku
    return: id_list
    raise: FileNotFoundError'''
    try:
        with open(SKU_FILE, 'r') as file:
            sku_list = file.readlines()
            id_list=[]
            for line in sku_list[1:]:
                sku_element=line.strip().split("|")
                id_list.append(sku_element[0])
        return id_list
    except FileNotFoundError:
        print("File of SKU data does not exist.")

def inv_file_lines():
    '''This function returns the Product IDs present in inventory
    return: id_list
    raise: FileNotFoundError'''
    try:
        with open(INV_FILE, 'r') as file:
            inv_list = file.readlines()
            id_list=[]
            for line in inv_list[1:]:
                inv_element=line.strip().split("|")
                id_list.append(inv_element[0])
        return id_list
    except FileNotFoundError:
        print("File of Inventory data does not exist.")

def get_old_sku_element_details(product_id):
    '''This function returns the product name and product price of the sku data file
    param product_id:Product ID of item in SKU data file
    return: sku_element[1], sku_element[2]
    raise: FileNotFoundError'''
    try:
        with open(SKU_FILE, 'r') as file:
            for line in file.readlines():
                sku_element = line.strip().split("|")
                if sku_element[0] == str(product_id):
                    return sku_element[1], sku_element[2]
    except FileNotFoundError:
        print("File of SKU data does not exist.")

def get_old_inv_element_details(product_id):
    '''This function returns the product quantity and product reorder level of the Inventory data file
    param product_id:Product ID of item in Inventory data file
    return: inv_element[1], inv_element[2]
    raise: FileNotFoundError'''
    try:
        with open(INV_FILE, 'r') as file:
            for line in file.readlines():
                inv_element = line.strip().split("|")
                if inv_element[0] == str(product_id):
                    return inv_element[1],inv_element[2]
    except FileNotFoundError:
        print("File of Inventory data does not exist.")

def product_id_add_validation(id_list):
    '''This function returns the Product ID after doing the necessary validations
    param: id_list
    return: product_id
    raise: ProductIDEmptyError,ProductIDTypeError,ProductIDNegativeError,ProductIDExistsError'''
    while True:
        try:
            product_id = input("Enter Product ID: ").strip()
            if not product_id:
                raise ProductIDEmptyError("Product ID cannot be empty.")                    
            try:
                product_id = int(product_id)
            except ValueError:
                raise ProductIDTypeError("Product ID must be an integer.")                    
            if product_id <= 0:
                raise ProductIDNegativeError("Product ID cannot be zero or negative.")
            if (str(product_id) in id_list):
                raise ProductIDExistsError(f"Product ID {product_id} already exists.")
        except (ProductIDEmptyError) as e:
            print(f"{e}")
            print("Please enter the details again.\n")
        except (ProductIDTypeError) as e:
            print(f"{e}")
            print("Please enter the details again.\n")
        except (ProductIDNegativeError) as e:
            print(f"{e}")
            print("Please enter the details again.\n")
        except (ProductIDExistsError) as e:
            print(f"{e}")
            print("Please enter the details again.\n")
        else:
            return product_id

def product_name_validation():
    '''This function returns the Product name after doing the necessary validations
    return: product_name
    raise: ProductNameEmptyError'''
    while True:
        try:     
            product_name = input("Enter Product Name: ").strip()
            if not product_name:
                raise ProductNameEmptyError("Product name cannot be empty.")
        except (ProductNameEmptyError) as e:
            print(f"{e}")
            print("Please enter the details again.\n")
        else:
            return product_name

def product_price_validation():
    '''This function returns the Product price after doing the necessary validations
    return: product_price
    raise: ProductPriceEmptyError,ProductPriceTypeError,ProductPriceNegativeError,ProductPriceExistsError'''
    while True:
        try:
            product_price = input("Enter Product Price: ").strip()
            if not product_price:
                raise ProductPriceEmptyError("Product price cannot be empty.")
            try:
                product_price = int(product_price)
            except ValueError:
                raise ProductPriceTypeError("Product price must be an integer.")
            if product_price <= 0:
                raise ProductPriceNegativeError("Product price cannot be zero or negative.")
        except (ProductPriceEmptyError) as e:
            print(f"{e}")
            print("Please enter the details again.\n")
        except (ProductPriceTypeError) as e:
            print(f"{e}")
            print("Please enter the details again.\n")
        except (ProductPriceNegativeError) as e:
            print(f"{e}")
            print("Please enter the details again.\n")
        else:
            return product_price

def product_id_remove_or_update_validation(id_list):
    '''This function returns the Product ID after doing the necessary validations
    param: id_list
    return: product_id
    raise: ProductIDEmptyError,ProductIDTypeError,ProductIDNegativeError,ProductIDExistsError'''
    while True:
        try:
            product_id = input("Enter Product ID: ").strip()
            if not product_id:
                raise ProductIDEmptyError("Product ID cannot be empty.")
            try:
                product_id = int(product_id)
            except ValueError:
                raise ProductIDTypeError("Product ID must be an integer.")
            if product_id <= 0:
                raise ProductIDNegativeError("Product ID cannot be zero or negative.")
            if (str(product_id) not in id_list):  
                raise ProductIDDoesNotExistError(f"Product ID {product_id} does not exist in the list.")
        except (ProductIDEmptyError) as e:
            print(f"{e}")
            print("Please enter the details again.\n")
        except (ProductIDTypeError) as e:
            print(f"{e}")
            print("Please enter the details again.\n")
        except (ProductIDNegativeError) as e:
            print(f"{e}")
            print("Please enter the details again.\n")
        except (ProductIDDoesNotExistError) as e:
            print(f"{e}")
            print("Please enter the details again.\n")
        else:
            return product_id
        
def product_quantity_validation():
    '''This function returns the Product quantity after doing the necessary validations
    return: product_quantity
    raise: ProductQuantityEmptyError,ProductQuantityTypeError,ProductQuantityNegativeError,ProductQuantityExistsError'''
    while True:
        try:
            product_quantity = input("Enter Product quantity: ").strip()
            if not product_quantity:
                raise ProductQuantityEmptyError("Product quantity cannot be empty.")
            try:
                product_quantity = int(product_quantity)
            except ValueError:
                raise ProductQuantityTypeError("Product quantity must be an integer.")
            if product_quantity <= 0:
                raise ProductQuantityNegativeError("Product quantity cannot be zero or negative.")
        except (ProductQuantityEmptyError) as e:
            print(f"{e}")
            print("Please enter the details again.\n")
        except (ProductQuantityTypeError) as e:
            print(f"{e}")
            print("Please enter the details again.\n")
        except (ProductQuantityNegativeError) as e:
            print(f"{e}")
            print("Please enter the details again.\n")
        else:
            return product_quantity
                                                               
def product_reorder_validation():
    '''This function returns the Product reorder after doing the necessary validations
    return: product_reorder
    raise: ProductReOrderEmptyError,ProductReOrderTypeError,ProductReOrderNegativeError,ProductReOrderExistsError'''
    while True:
        try:
            product_reorder = input("Enter Product re-order level: ").strip()
            if not product_reorder:
                raise ProductReOrderEmptyError("Product re-order level cannot be empty.")
            try:
                product_reorder = int(product_reorder)
            except ValueError:
                raise ProductReOrderTypeError("Product re-order level must be an integer.")
            if product_reorder <= 0:
                raise ProductReOrderNegativeError("Product re-order level cannot be zero or negative.")              
        except (ProductReOrderEmptyError) as e:
            print(f"{e}")
            print("Please enter the details again.\n")
        except (ProductReOrderTypeError) as e:
            print(f"{e}")
            print("Please enter the details again.\n")
        except (ProductReOrderNegativeError) as e:
            print(f"{e}")
            print("Please enter the details again.\n")
        else:
            return product_reorder

def read_and_validate_files():
    '''This function reads and validates the sku and inventory data files
    return: sku_list,inv_list
    raise: SkuFileEmptyError,InvFileEmptyError,FileNotFoundError'''
    try:
        with open(SKU_FILE, 'r') as sku_file:
            sku_list = sku_file.readlines()[1:] 
        with open(INV_FILE, 'r') as inv_file:
            inv_list = inv_file.readlines()[1:]         
        if not sku_list:
            raise SkuFileEmptyError("SKU data file is empty.")
        if not inv_list:
            raise InvFileEmptyError("Inventory data file is empty.")        
        return sku_list,inv_list
    except (SkuFileEmptyError) as e:
        print(f"{e}")
        
    except (InvFileEmptyError) as e:
        print(f"{e}")
        
    except FileNotFoundError:
        print("File not found.")
        
                                                                     
def main():
    '''This is the main function'''
    while True:
        print('''
Operations in SKU data
Enter 1 to add product into SKU data
Enter 2 to remove product from SKU data
Enter 3 to update product in SKU data
Enter 4 to add SKU quantity into INVENTORY data
Enter 5 to remove SKU quantity from INVENTORY data
Enter 6 to update SKU quantity in INVENTORY data
Enter 7 to show Inventory Summary Report
Enter 8 to show Total Inventory Value Report
Enter 9 to show Low Stock Alert Report
Enter 10 to Exit''') 
        choice=input("Enter your choice:").strip()
        
        if(choice=="1"):
            id_list = sku_file_lines()
            product_id = product_id_add_validation(id_list)
            product_name = product_name_validation()
            product_price = product_price_validation()
            add_sku(product_id,product_name,product_price)

        elif(choice == "2"):
            try:
                id_list=sku_file_lines()
                if not id_list:
                    raise SkuFileEmptyError("SKU data file is empty")
            except (SkuFileEmptyError) as e:
                print(f"{e}")
            else:
                product_id=product_id_remove_or_update_validation(id_list)
                remove_sku(product_id)
 
        elif(choice == "3"):
            try:
                id_list=sku_file_lines()
                if not id_list:
                    raise SkuFileEmptyError("SKU data file is empty")
            except (SkuFileEmptyError) as e:
                print(f"{e}")
            else:
                product_id=product_id_remove_or_update_validation(id_list)
                old_name,old_price =get_old_sku_element_details(product_id)

            while True:
                try:
                    input_choice1 = input("Do you want to update the product name?\nEnter 1 for yes\nEnter 2 for no\n").strip()
                    if input_choice1 not in ["1", "2"]:
                        raise ValueError("Invalid choice. Enter 1 for yes or 2 for no.")
                    if input_choice1 == "1":
                        new_name = input("Enter new Product Name: ").strip()
                        if not new_name:
                            raise ProductNameEmptyError("Product name cannot be empty.")
                    else:
                        new_name = old_name
                    break
                except (ProductNameEmptyError) as e:
                    print(f"{e}")
                    print("Please enter the details again.\n")
                except ValueError as e:
                    print(f"{e}")
                    print("Please enter the details again.\n")
            
            while True:
                try:   
                    input_choice2 = input("Do you want to update the product price?\nEnter 1 for yes\nEnter 2 for no\n").strip()
                    if input_choice2 not in ["1", "2"]:
                        raise ValueError("Invalid choice. Enter 1 for yes or 2 for no.")
                    if input_choice2 == "1":
                        new_price = input("Enter new Product Price: ").strip()
                        if not new_price:
                            raise ProductPriceEmptyError("Product price cannot be empty.")
                        try:
                            new_price = int(new_price)
                        except ValueError:
                            raise ProductPriceTypeError("Product price must be an integer.")
                        if new_price <= 0:
                            raise ProductPriceNegativeError("Product price cannot be zero or negative.")
                    else:
                        new_price = old_price
                    break
                except (ProductPriceEmptyError) as e:
                    print(f"{e}")
                    print("Please enter the details again.\n")
                except (ProductPriceTypeError) as e:
                    print(f"{e}")
                    print("Please enter the details again.\n")
                except (ProductPriceNegativeError) as e:
                    print(f"{e}")
                    print("Please enter the details again.\n")
                except ValueError as e:
                    print(f"{e}")
                    print("Please enter the details again.\n")
            update_sku(product_id, new_name, new_price)
                                
        elif(choice=="4"):
            while True:
                try:
                    id_list_inv= inv_file_lines()
                    id_list_sku= sku_file_lines()
                    if(id_list_inv==id_list_sku):
                        raise SameIdListsError("Quantity and Reorder level of Product IDs in sku is already present in Inventory data file.\nTo add elements in Inventory, add elements in SKU or please choose other option of your choice.")
                except (SameIdListsError) as e:
                    print(f"{e}")     
                else:
                    product_id =product_id_add_validation(id_list_inv)
                    if(str(product_id) not in id_list_sku):
                        print("Product ID does not exist in SKU data file.")
                    else:
                        product_quantity =product_quantity_validation()
                        product_reorder = product_reorder_validation()
                        add_inv(product_id,product_quantity,product_reorder)
                        break
    
        elif(choice == "5"):
            try:
                id_list=inv_file_lines()
                if not id_list:
                    raise InvFileEmptyError("Inventory data file is empty")
            except (InvFileEmptyError) as e:
                print(f"{e}")            
            else:
                product_id=product_id_remove_or_update_validation(id_list)
                remove_inv(product_id)
            
        elif(choice == "6"):
            try:
                id_list=inv_file_lines()
                if not id_list:
                    raise InvFileEmptyError("Inventory data file is empty")
            except (InvFileEmptyError) as e:
                print(f"{e}") 
            else:
                product_id=product_id_remove_or_update_validation(id_list)
                old_quantity,old_reorder =get_old_inv_element_details(product_id)
            while True:
                try:
                    input_choice1 = input("Do you want to update the product quantity?\nEnter 1 for yes\nEnter 2 for no\n").strip()
                    if input_choice1 not in ["1", "2"]:
                        raise ValueError("Invalid choice. Enter 1 for yes or 2 for no.")
                    if (input_choice1 == "1"):
                        new_quantity = input("Enter new Product quantity: ").strip()
                        if not new_quantity:
                            raise ProductQuantityEmptyError("Product quantity cannot be empty.")
                        try:
                            new_quantity = int(new_quantity)
                        except ValueError:
                            raise ProductQuantityTypeError("Product quantity must be an integer.")
                        if new_quantity <= 0:
                            raise ProductQuantityNegativeError("Product quantity cannot be zero or negative.")
                    else:
                        new_quantity = old_quantity
                    break
                except (ProductQuantityEmptyError) as e:
                    print(f"{e}")
                    print("Please enter the details again.\n")
                except (ProductQuantityTypeError) as e:
                    print(f"{e}")
                    print("Please enter the details again.\n")
                except (ProductQuantityNegativeError) as e:
                    print(f"{e}")
                    print("Please enter the details again.\n")
                except ValueError as e:
                    print(f"{e}")
                    print("Please enter the details again.\n")
                    
            while True:
                try:   
                    input_choice2 = input("Do you want to update the product reorder level?\nEnter 1 for yes\nEnter 2 for no\n").strip()
                    if input_choice2 not in ["1", "2"]:
                            raise ValueError(f"Invalid choice. Enter 1 for yes or 2 for no.")        
                    if(input_choice2=="1"):
                        new_reorder = input("Enter new product reorder level: ").strip()
                        if not new_reorder:
                            raise ProductReOrderEmptyError("Product price cannot be empty.")
                        try:
                            new_reorder = int(new_reorder)
                        except ValueError:
                            raise ProductReOrderTypeError("Product price must be an integer.")
                        if new_reorder <= 0:
                            raise ProductReOrderNegativeError("Product price cannot be zero or negative.")
                    else:
                        new_reorder = old_reorder
                    break
                except (ProductReOrderEmptyError) as e:
                    print(f"{e}")
                    print("Please enter the details again.\n")
                except (ProductReOrderTypeError) as e:
                    print(f"{e}")
                    print("Please enter the details again.\n")
                except (ProductReOrderNegativeError) as e:
                    print(f"{e}")
                    print("Please enter the details again.\n")
                except ValueError as e:
                    print(f"{e}")
                    print("Please enter the details again.\n")
            update_inv(product_id,new_quantity,new_reorder)
                                
        elif(choice=="7"):
            sku_list,inv_list =read_and_validate_files()
            inventory_summary_report(sku_list,inv_list)
                                          
        elif(choice=="8"):
            sku_list,inv_list =read_and_validate_files()
            total_inventory_value_report(sku_list,inv_list)
                        
        elif(choice=="9"):
            sku_list,inv_list =read_and_validate_files()
            low_stock_alert_report(sku_list,inv_list)
            
        elif(choice=="10"):
            break
            
        else:
            print("Wrong choice selected.Enter another choice from 1 to 10.")
            
if __name__ == "__main__":
    main()
