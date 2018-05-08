from orm import *
import os

db_filename = raw_input("select the name of the database:")
connectdata(db_filename)

dimitris = Person('Dimitris','Bovasianos',26)
maria = Person('Maria','Kougiou',50)
dimitris.insert()
maria.insert()
dimitris.first_name = 'dimi'
dimitris.update()
dimitris.delete()
maria.select()
