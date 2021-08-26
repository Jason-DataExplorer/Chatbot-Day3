import os
import psycopg2


DATABASE_URL = os.popen('heroku config:get DATABASE_URL -a app_name').read()[:-1]

conn = psycopg2.connect(DATABASE_URL, sslmode='require')
cursor = conn.cursor()

postgres_select_query = f"""SELECT * FROM test_table"""

cursor.execute(postgres_select_query)
cursor.fetchall()
