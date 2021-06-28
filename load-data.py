import psycopg2
import mysql.connector
import faker
import os

data = faker.Faker('en_US')

connm = mysql.connector.connect(
    host=os.environ.get('MYSQL_HOST'),
    user=os.environ.get('MYSQL_USER'),
    password=os.environ.get('MYSQL_PASSWORD'),
    database=os.environ.get('MYSQL_DB')
)
connp = psycopg2.connect(
    host=os.environ.get('POSTGRES_HOST'),
    database=os.environ.get('POSTGRES_DB'),
    user=os.environ.get('POSTGRES_USER'),
    password=os.environ.get('POSTGRES_PASSWORD')
)

curp = connp.cursor()
curm = connm.cursor()

curm.execute("DROP table IF EXISTS customers")

curp.execute("DROP TABLE IF EXISTS customers")

curm.execute("CREATE TABLE customers (id VARCHAR(255), name VARCHAR(255))")

curp.execute("CREATE TABLE customers (id VARCHAR(255), address VARCHAR(255))")

namedict = []
num_of_rows = os.environ.get('NUMOFROWS')
num_of_rows = int(num_of_rows)
for i in range(0, num_of_rows):
    namedict.append({
        'id': getattr(data, 'uuid4')(),
        'name': getattr(data, 'name')(),
        'address': getattr(data, 'address')(),
    })

curp.executemany("""INSERT INTO customers (id, address) VALUES (%(id)s, %(address)s)""", tuple(namedict))

curm.executemany("""INSERT INTO customers (id, name) VALUES (%(id)s, %(name)s)""", tuple(namedict))

connp.commit()

connm.commit()
