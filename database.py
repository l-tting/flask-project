import psycopg2

# establishing a db connection
conn = psycopg2.connect(host='localhost',port=5432, user='postgres',password='6979',dbname='flask_myduka')

#creating a cursor object to perform db operations
cur = conn.cursor()


def get_products():
    cur.execute("select * from products")
    products = cur.fetchall()
    return products


def insert_products(product_values):
    cur.execute("insert into products(name,buying_price,selling_price)values(%s,%s,%s)",product_values)
    conn.commit()


# product1 = ('juice',80,120)
# product2 = ('charger',1500,2000)
# insert_products(product1)
# insert_products(product2)

# products = get_products()
# print(products)

def get_sales():
    cur.execute("select * from sales")
    sales = cur.fetchall()
    return sales


def insert_sales(sale_values):
    cur.execute("insert into sales(pid,quantity)values(%s,%s)",sale_values)
    conn.commit()

# sale1 = (1,30)
# sale2 = (2,20)
# insert_sales(sale1)
# insert_sales(sale2)
# sales = get_sales()
# print(sales)


def get_stock():
    cur.execute("select * from stock")
    stock = cur.fetchall()
    return stock

def insert_stock(stock_values):
    cur.execute("insert into stock(pid,stock_quantity)values(%s,%s)",stock_values)
    conn.commit()

# stock1 = (1,45)
# stock2 = (2,40)
# insert_stock(stock1)
# insert_stock(stock2)
# stock = get_stock()
# print(stock)


def sales_per_product():
    cur.execute("""
        select products.name as p_name , sum(products.selling_price * sales.quantity) as 
        total_sales from products join sales on sales.pid = products.id group by p_name;
    """)
    sales_product = cur.fetchall()
    return sales_product


# sales_product = sales_per_product()
# print(sales_product)


def sales_per_day():
    cur.execute("""
        select date(sales.created_at) as date, sum(products.selling_price * sales.quantity) as 
        total_sales from sales join products on sales.pid = products.id group by date
    """)
    sales_day = cur.fetchall()
    return sales_day


def profit_per_product():
    cur.execute("""
        select products.name as p_name , sum((products.selling_price - products.buying_price) * sales.quantity)
        from sales join products on sales.pid = products.id group by p_name
    """)
    profit_product = cur.fetchall()
    return profit_product


def profit_per_day():
    cur.execute("""
        select date(sales.created_at) as date , sum((products.selling_price - products.buying_price) * sales.quantity)
         from sales join products on sales.pid = products.id group by date
    """)
    profit_day = cur.fetchall()
    return profit_day

