#! coding:utf-8
import MySQLdb
#connec db
def con_db():

    db= MySQLdb.connect(host="127.0.0.1",user="root",passwd="",db="sun",port=3306)
    return db
con_db()

