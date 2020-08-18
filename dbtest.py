import cx_Oracle

con = cx_Oracle.connect("hr","hr","127.0.0.1:1521/XE")

cu = con.cursor()

cu.execute("""select * from book""")

for book in cu:
    print(book)