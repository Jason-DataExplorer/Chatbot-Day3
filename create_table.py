import os
import psycopg2

DATABASE_URL = os.popen('heroku config:get DATABASE_URL -a app_name').read()[:-1]

# connect to database
conn   = psycopg2.connect(DATABASE_URL, sslmode='require')
cursor = conn.cursor()

# create a table
create_table_query = '''
    CREATE TABLE test_table(
    id     serial  PRIMARY KEY,
    name   VARCHAR NOT NULL,
    weight NUMERIC NOT NULL,
    height NUMERIC NOT NULL,
    date   DATE    NOT NULL);
    '''

# execute query
cursor.execute(create_table_query)
conn.commit()

cursor.close()
conn.close()
