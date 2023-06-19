from peewee import *
from models import *


db.connect()
db.create_tables([User, Product, Tag, Purchase, ProductTag])
#conn = sqlite3.connect('database.db')
#cursor = conn.cursor()



def populate_products():
    klaas_vaak = User.create(
        username="Klaas Vaak",
        street="de Beurs",
        house_number="2",
        postal_code="3302RR",
        city="Rotterdam",
        country="NL",
        billing_info="802090"
    )

    mango = Product.create(
        name="Mango",
        description="fruit",
        price="2.00",
        quantity="1",
        owner=klaas_vaak
    )

    apple = Product.create(
        name="Apple",
        description="fruit",
        price="1.00",
        quantity="1",
        owner=klaas_vaak
    )

    

    tag1 = Tag.create(
        name="Tag1",
    )

    tag2 = Tag.create(
        name="Tag2",
    )

    ProductTag.create(
        product=mango,
        tag=tag1,
    )

    ProductTag.create(
        product=apple,
        tag=tag2,
    )

    Purchase.create(
        product_bought=mango,
        buyer=klaas_vaak,
        quantity_bought=2,
    )

    Purchase.create(
        product_bought=apple,
        buyer=klaas_vaak,
        quantity_bought=2,
    )



    