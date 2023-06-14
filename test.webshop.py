import unittest 
from models import *
import psycopg2


def populate_test_database():
    
    connection = psycopg2.connect(database='your_database_name', user='your_username', password='your_password', host='your_host')
    cursor = connection.cursor()

    # Execute SQL queries to insert example data into your tables
    insert_query = "INSERT INTO your_table (column1, column2) VALUES (%s, %s)"
    data = [
        ('Karel de Grote', 10),
        ('Arne Slot', 20),
        ('Santiago Gimenez', 30)
    ]

    # Execute the insert query for each data item
    for item in data:
        cursor.execute(insert_query, item)

    # Commit the changes and close the connection
    connection.commit()
    connection.close()


class WebshopTestCase(unittest.TestCase):
    def test_get_all_products(self):
        products = Database.get_all_products()
        self.assertEqual(len(products), 1)

def test_search():
    test_search("keywords")

def test_list_user_products():
    test_list_user_products(1)

def test_list_products_per_tag():
    test_list_products_per_tag(1)

def test_add_product_to_catalog():
    test_add_product_to_catalog(1)

def test_update_stock():
    test_update_stock(1)    

def test_purchase_product():
    test_purchase_product(1)

def test_remove_product():
    test_remove_product(1)


def main():
    # Call your test functions here
    populate_test_database()
    unittest.main()
    test_search()
    test_list_user_products()
    test_add_product_to_catalog() 
    test_update_stock()
    test_purchase_product()
    test_remove_product()

if __name__ == '__main__':
    unittest.main()


