






import mysql.connector as mysql 


config = {
    "host": "192.168.1.112",
    "port": 3306,
    "user": "lazybong",
    "password": "among7201"
}


connection = mysql.connect(
    **config
)

print(connection)

