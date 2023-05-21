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
        self.assertEqual(len(products), 10)


if __name__ == '__main__':
    unittest.main()


