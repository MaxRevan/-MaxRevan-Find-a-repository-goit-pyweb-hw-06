import psycopg2

conn = psycopg2.connect(host="localhost", database="univer", user="postgres", password="12345")
cur = conn.cursor()

query_file = 'query_4.sql' 
with open(query_file, 'r') as file:
    sql_query = file.read()

cur.execute(sql_query)

rows = cur.fetchall()
for row in rows:
    print(row)

cur.close()
conn.close()
