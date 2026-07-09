import psycopg2

# establishing a db connection
conn = psycopg2.connect(host='localhost',port=5432, user='postgres',password='6979',dbname='flask_myduka')

#creating a cursor object to perform db operations
cur = conn.cursor()


def get_products():
    cur.execute("select * from products")
    products = cur.fetchall()
    return products


def insert_products():
    cur.execute("insert into products(name,buying_price,selling_price)values('shoes',2000,2500)")
    conn.commit()

insert_products()

products = get_products()
print(products)
