import psycopg2
import mysql.connector
import faker

data = faker.Faker('en_US')

connm = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database="dev"
)

connp = psycopg2.connect(
    host="localhost",
    database="dev",
    user="admin",
    password="admin")

curp = connp.cursor()
curm = connm.cursor()

curm.execute("DROP table IF EXISTS customers")

curp.execute("DROP TABLE IF EXISTS customers")

curm.execute("CREATE TABLE customers (id VARCHAR(255), name VARCHAR(255))")

curp.execute("CREATE TABLE customers (id VARCHAR(255), address VARCHAR(255))")

namedict = []
for i in range(0, 10):
    namedict.append({
        'id': getattr(data, 'uuid4')(),
        'name': getattr(data, 'name')(),
        'address': getattr(data, 'address')(),
    })

curp.executemany("""INSERT INTO customers (id, address) VALUES (%(id)s, %(address)s)""", tuple(namedict))

curm.executemany("""INSERT INTO customers (id, name) VALUES (%(id)s, %(name)s)""", tuple(namedict))

connp.commit()

connm.commit()
