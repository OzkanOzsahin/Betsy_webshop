import sqlite3
from tabulate import tabulate
from models import *


__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

conn = sqlite3.connect('database.db')
cursor = conn.cursor()
cursor.execute('SELECT * FROM product')
rows = cursor.fetchall()
headers = [description[0] for description in cursor.description]
print(tabulate(rows, headers, tablefmt="grid"))
cursor.close()
conn.close()

def search(term):
    products = Product.select().where(
        Product.name.contains(term) | Product.description.contains(term)
    )
    print(f"The search on '{term}' delivers these products:")
    print("========================================================")
    if len(products) == 0:
        print("<< No products were found >>")
    else:
        for product in products:
            print(
                f"Productname: {product.name}  Price: {product.price}  Quantity: {product.quantity}"
            )



def list_user_products(user_id):
    try:
        tag = Tag.get_by_id(user_id)
    except DoesNotExist:
        print(f"Tag_id: '{user_id}' is not found")
        return

    print(f"Tag '{tag.name}' is present in the following products:")
    print("=======================================================")
    products = Product.select().join(ProductTag).where(ProductTag.tag == user_id)
    for product in products:
        print(product.product_id, "|", product.name, "|", product.description)


def list_products_per_tag(tag_id):
    try:
        tag = Tag.get_by_id(tag_id)
    except DoesNotExist:
        print(f"Tag_id: '{tag_id}' is not found")
        return

    print(f"Tag '{tag.name}' is present in the following products:")
    print("=======================================================")
    products = Product.select().join(ProductTag).where(ProductTag.tag == tag_id)
    for product in products:
        print(product.product_id, "|", product.name, "|", product.description)


def add_product_to_catalog(user_id, product):
    try:
        user = User.get_by_id(user_id)
    except DoesNotExist:
        print(f"User with id: '{user_id}' is not found")
        return

    Product.create(
        name=product.name,
        description=product.description,
        price=product.price,
        quantity=product.quantity,
        owner=user_id,
    )
    print(
        f"Product: '{product.name}' has been added. Owner is: {user.username}"
    )



def update_stock(product_id, new_quantity):
    num_upd = Product.set_by_id(product_id, {"quantity": new_quantity})
    if num_upd == 0:
        print(f"Product with id: '{product_id}' is not found")
    else:
        print(
            f"Product with id: '{product_id}' has been updated, new quantity is: {new_quantity}"
        )


def purchase_product(product_id, buyer_id, quantity):
    try:
        product = Product.get_by_id(product_id)
    except DoesNotExist:
        print(f"Product with id: '{product_id}' is not found")
        return

    try:
        user = User.get_by_id(buyer_id)
    except DoesNotExist:
        print(f"Buyer with id: '{buyer_id}' is not found")
        return

    if product.quantity >= quantity:
        new_quantity = product.quantity - quantity
        update_stock(product_id, new_quantity)
        Purchase.create(buyer=user, product_bought=product, quantity_bought=quantity)
        print(
            f"Product with id: '{product_id}' has been sold to '{user.username}', transaction has been added"
        )
    else:
        print(
            f"Product with id: '{product_id}' is not in stock, the current quantity is: {product.quantity}"
        )


def remove_product(product_id):
    try:
        product = Product.get_by_id(product_id)
    except DoesNotExist:
        print(f"Product with id: '{product_id}' is not found")
        return

    product.delete_instance(recursive=True, delete_nullable=True)
    print(f"Product with id: '{product_id}' has been deleted")



def main():
    
    pass


if __name__ == "__main__":
    main() 
