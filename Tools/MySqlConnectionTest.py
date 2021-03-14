
import mysql.connector as mysql 


def connect(host, port, user, password):
    connection = mysql.connect(
        host=host,
        port=port,
        user=user,
        password=password
    )        
        
    return connection

def connectLocalhost():
    """ 本地伺服器連線 """
    host = "127.0.0.1"
    connection = connect(host, 3306, "root", "among7201")
    if connection:
        print("Connection localhost ok", connection)
        connection.close()


def connectRemoteHost():
    """ 遠端連線測試 """
    host = "192.168.1.112"
    connection = connect(host, 3306, "remoteTest", "remoteTest")
    if connection:
        print("Connection remote ok", connection)
        connection.close()



if __name__ == '__main__':
    
    
    connectLocalhost()  
    connectRemoteHost()