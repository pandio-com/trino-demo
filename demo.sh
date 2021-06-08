pip install -r requirements.txt

python load-data.py

echo "\r"

echo "Join MySQL with PostgreSQL customers table on key 'id'"

echo "\r"

echo "Executing: "

echo "\r"

echo "select * from system.runtime.nodes;"

echo "\r"

./trino.jar --output-format ALIGNED --execute 'select * from system.runtime.nodes;'

echo "\r"

echo "show catalogs;"

echo "\r"

./trino.jar --output-format ALIGNED --execute 'show catalogs;'

echo "\r"

echo "show schemas in mysql;"

echo "\r"

./trino.jar --output-format ALIGNED --execute 'show schemas in mysql;'

echo "\r"

echo "show schemas in postgres;"

echo "\r"

./trino.jar --output-format ALIGNED --execute 'show schemas in postgres;'

echo "\r"

echo "describe mysql.dev.customers;"

echo "\r"

./trino.jar --output-format ALIGNED --execute 'describe mysql.dev.customers;;'

echo "\r"

echo "describe postgres.public.customers;"

echo "\r"

./trino.jar --output-format ALIGNED --execute 'describe postgres.public.customers;'

echo "\r"

echo "select mysql.dev.customers.*, postgres.public.customers.* from mysql.dev.customers join postgres.public.customers on postgres.public.customers.id = mysql.dev.customers.id LIMIT 10;"

echo "\r"

./trino.jar --output-format ALIGNED --execute 'select mysql.dev.customers.*, postgres.public.customers.* from mysql.dev.customers join postgres.public.customers on postgres.public.customers.id = mysql.dev.customers.id LIMIT 10;'