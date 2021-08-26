import os
import psycopg2


DATABASE_URL = os.popen('heroku config:get DATABASE_URL -a app_name').read()[:-1]

conn = psycopg2.connect(DATABASE_URL, sslmode='require')
cursor = conn.cursor()

new = "Danny"
origin = "David"
postgres_update_query = f"""UPDATE test_table set name = %s WHERE name = %s"""

cursor.execute(postgres_update_query, (new, origin))
conn.commit()

count = cursor.rowcount
print(count, "Record update successfully into table")
