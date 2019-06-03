import select
import or


con= cx_Oracle.connect('http://127.0.0.1:8000/')

print(con.version)
cur=con.cursor()
cur.excute(select *from Language)

for result in cur:
    print(result)
    cur.close()
