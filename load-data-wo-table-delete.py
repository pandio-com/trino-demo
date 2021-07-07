import psycopg2
import mysql.connector
import faker
import os

from dotenv import load_dotenv

load_dotenv()

data = faker.Faker('en_US')

connm = mysql.connector.connect(
    host=os.getenv('MYSQL_HOST'),
    user=os.getenv('MYSQL_USER'),
    password=os.getenv('MYSQL_PASSWORD'),
    database=os.getenv('MYSQL_DB')
)
connp = psycopg2.connect(
    host=os.getenv('POSTGRES_HOST'),
    database=os.getenv('POSTGRES_DB'),
    user=os.getenv('POSTGRES_USER'),
    password=os.getenv('POSTGRES_PASSWORD')
)

curp = connp.cursor()
curm = connm.cursor()

curm.execute("CREATE TABLE IF NOT EXISTS customers (id VARCHAR(255), name VARCHAR(255))")

curp.execute("CREATE TABLE IF NOT EXISTS customers (id VARCHAR(255), address VARCHAR(255))")

namedict = []
num_of_rows = os.getenv('NUMOFROWS')
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
