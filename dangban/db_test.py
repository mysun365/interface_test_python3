from db import con_db
import MySQLdb
db = con_db()
cursor = db.cursor()
def insert(username,password):
    cursor.execute("insert into person(firstname,lastname) values ('%s','%s')" %(username,password))
    

def query(username,password):
    cursor.execute("select lastname,firstname from person where lastname='%s' and firstname='%s'" %(username,password))
    result = cursor.fetchone()
    return result

#insert(cursor,"test","test")

r =  query("test","test")
print r
