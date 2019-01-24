#!/usr/local/bin/python3


#brew install mysql
#brew tap homebrew/services
#brew services start mysql
#pip3 install mysql client
import MySQLdb
db = MySQLdb.connect(host='ocalhost', port='3306', user='root', passwd="", db="testpython")
cursor = db.cursor()

#retrieve manual entry from db
cursor.execute("SELECT * FROM TestPerson")
data = cursor.fetchall()
for row in data:
    id = row[0]
    print(str(id))
cursor.close()
db.close()