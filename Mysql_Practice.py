import mysql.connector

dbcon = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='rishu123',
    database='world'
)
dbcur = dbcon.cursor()

sqlstmnt = "SELECT * FROM world.city"

dbcur.execute(sqlstmnt)

dbdata = dbcur.fetchall()

# print(dbdata)

city_list = []
country_code_list = []
City_country_code_dict = {}
for i in dbdata:
    city_list.append(i[1])
    country_code_list.append(i[2])
    City_country_code_dict[i[2]] = i[1]

# print(city_list)
# print(country_code_list)
print(City_country_code_dict)

dbcon.close
