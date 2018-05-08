import sqlite3
import os

con = None

def connectdata(filename):
    global con
    if not os.path.exists(filename):
        con=sqlite3.connect(filename)
        schema_filename = raw_input("insert the schema name:")
        with open(schema_filename,'rt') as f:
            schema = f.read()
            con.executescript(schema)
    else:
        con = sqlite3.connect(filename)
        print "the database exist so the scheme"


class Person():

    def __init__(self,first_name,last_name,age):
        self.pk = None
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def insert(self):
            c = con.cursor()
            c.execute("INSERT INTO person(first_name,last_name,age) values(?,?,?)",
                      (self.first_name,self.last_name,self.age))
            self.pk = c.lastrowid
            con.commit()
    def update(self):
        c = con.cursor()
        c.execute("update person set first_name=?,last_name=?,age=? where id =?",
                  (self.first_name,self.last_name,self.age,self.pk))
        con.commit()

    def delete(self):
        c = con.cursor()
        c.execute('delete from person where id=?',(self.pk,))
        con.commit()

    def select(self):
         cursor = con.execute('SELECT id,first_name,last_name,age from person')
         for row in cursor:
             print "ID = ",row[0]
             print "first_name = ",row[1]
             print "last_name =",row[2]
             print "age =",row[3],"\n"
         con.close()
