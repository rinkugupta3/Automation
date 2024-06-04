'''
# Following code is standard code to create a database and a table in sqlite3
import sqlite3

def create_table():
# using try block to handle exceptions
    try:
        conn = sqlite3.connect('shoppingcart.db')
        cur = conn.cursor()
    
    # create the products table
    
    # create the customer table
    
    # use the except block to handle any erros that may occur
    except sqlite3.Error as e:
        print('An Error occurred while setting up the database:', e)
        
        
    # use the finally to commit and close connections
    finally:
        conn.commit()
        conn.close()
'''
import sqlite3

# Function
def create_table():
# using try block to handle exceptions
    try:
        conn = sqlite3.connect('shoppingcart.db')
        cur = conn.cursor()
    
        # create the products table
        cur.execute("""
        CREATE TABLE IF NOT EXISTS cart(
            id INTEGER PRIMARY KEY,
            item TEXT NOT NULL,
            price REAL NOT NULL,
            customer_id INTEGER,
            FOREIGN KEY (customer_id) REFERENCES customers(id)
            )""")   
        # create the customer table
        cur.execute("""
        CREATE TABLE IF NOT EXISTS customers(
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL
            )""")
    

    
    # use the except block to handle any erros that may occur
    except sqlite3.Error as e:
        print('An Error occurred while setting up the database:', e)
        
        
    # use the finally to commit and close connections
    finally:
        conn.commit()
        conn.close()

# Funtion      
# insert data into the database add_to_cart.
def add_customer(name,email):
    try:
        conn = sqlite3.connect('shoppingcart.db')
        cur = conn.cursor()
        
        cur.execute("""
        INSERT INTO customers (name, email) VALUES (?,?)""", (name, email))
        
        customer_id = cur.lastrowid
        return customer_id
        
    except sqlite3.Error as e:
        print('An Error occurred while setting up the database:', e)
    
    # Use Finally to commit and close connections
    finally:
        conn.commit()
        conn.close()

# Function  
# insert data into the database view_cart.
def add_to_cart(item, price, customer_id):
    try:
        conn = sqlite3.connect('shoppingcart.db')
        cur = conn.cursor()
        
        cur.execute("""
        INSERT INTO cart (item, price, customer_id) VALUES (?,?,?)""", (item, price, customer_id))
    
        
    except sqlite3.Error as e:
        print('An Error occurred while setting up the database:', e)
    
    finally:
        conn.commit()
        conn.close()  
        
# create funtion to add a tables to the database       

    
# Function
def view_cart(customer_id):
    try: 
        conn = sqlite3.connect('shoppingcart.db')
        cur = conn.cursor()
        
        cur.execute("""SELECT * FROM cart WHERE customer_id = ?""", (customer_id,))
    # when you want to pass a single parameter to a funtion or method as a tuple, 
    # you must include a comma after the parameter or at the end of the tuple.
    
        cart_items = cur.fetchall()

        if not cart_items:
            print('Cart is empty')
        else:
            print('Cart Items:')
            for item in cart_items:
                print(f"{item[0], item[1]} - {item[2]}")
            
            
    except sqlite3.Error as e:
        print('An Error occurred while setting up the database:', e)
    
    finally:
        conn.commit()
        conn.close()  
        
# create funtion to add a tables to the database       
def main():
    create_table()
    
    print ("Welcome to the shopping cart")
    
    # GET the customer details
    name = input('Enter your name: ')
    email = input('Enter your email: ')
    
    customer_id = add_customer(name, email)
    
    item = input('Enter your item name: ')
    price = float(input('Enter the price: '))
    
    add_to_cart(item, price, customer_id)
    
    view_cart(customer_id)
    
    print('Thank you for shopping with us')
    
if __name__ == '__main__':
    main()