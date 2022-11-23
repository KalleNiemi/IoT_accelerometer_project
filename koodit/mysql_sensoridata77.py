import mysql.connector
#from password import pw as pw

with open('password.txt') as ss:
    pw = ss.read()
print(pw)
db = mysql.connector.connect(
    host="172.20.241.9",
    user="dbaccess_ro",
    password=pw,
    database="measurements"
)

dbselect = db.cursor()

dbselect.execute("SELECT * FROM rawdata WHERE groupid=77")

dbresult = dbselect.fetchall()

for x in dbresult:
    print(x)
    