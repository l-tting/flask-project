from database import get_products

products = get_products()


for i in products:
    print(i[3])