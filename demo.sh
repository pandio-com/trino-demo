pip install -r requirements.txt

python load-data.py

echo "\n\r"

echo "Join MySQL with PostgreSQL customers table on key 'id'"

./trino.jar --output-format ALIGNED --execute 'select mysql.dev.customers.*, postgres.public.customers.* from mysql.dev.customers join postgres.public.customers on postgres.public.customers.id = mysql.dev.customers.id LIMIT 10;'