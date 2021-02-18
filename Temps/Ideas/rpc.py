# -*- encoding: utf-8 -*-

'''
* @File    :   rpc.py
* @Time    :   2021/02/17 06:30:49
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''
import os
import sys
sys.path.append(os.getcwd())
import traceback
import zmq
from zmq import Context as ZmqContext
from zmq.auth.thread import ThreadAuthenticator
from threading import Thread, Lock
from datetime import datetime, timedelta


class RemoteProcedureCallServer:
    """ 遠端程序調用伺服器 """

    def __init__(self):
        self.__zmqContext = ZmqContext() # ZMQ Context
        self.__replySocket = self.__zmqContext.socket(zmq.REP) # Reply socket (Request-Reply pattern)
        self.__publishSocket = self.__zmqContext.socket(zmq.PUB) # Publish socket (Publish-subscribe pattern)
        self.__isActive = False
        self.__thread = None
        self.__threadLock = Lock()
        self.__authenticator = None # 線程驗證器用於確保數據安全

    def isActive(self):
        """ 判斷是否正在運行 """
        return self.__isActive

    def setActive(self, isActive):
        """ 設置運行狀態 
        Arguments:
            isActive (bool): 運行狀態
        """
        self.__isActive = isActive

    def start(self, replyAdress, publishAdress, serverSecretKeyPath="", username="", password=""):
        """ 啟動 
        Arguments:
        replyAdress (str): 回應地址
        publishAdress (str): 廣播地址
        serverSecretKeyPath (str): 伺服器密鑰路徑
        username (str): 使用者名稱
        password (str): 密碼
        """
        if self.isActive():
            return

        # 啟動驗證器
        if serverSecretKeyPath:
            self.__authenticator = ThreadAuthenticator(self.__zmqContext)
            self.__authenticator.start()
            self.__authenticator.configure_curve(
                domain="*",
                location=zmq.auth.CURVE_ALLOW_ANY
            )            
            
            publishKey, secretKey = zmq.auth.load_certificate(serverSecretKeyPath)

            self.__publishSocket.curve_secretkey = secretKey
            self.__publishSocket.curve_publishkey = publishKey
            self.__publishSocket.curve_server = True
            self.__replySocket.curve_secretkey = secretKey
            self.__replySocket.curve_publishkey = publishKey
            self.__replySocket.curve_server = True
        elif username and password:
            self.__authenticator = ThreadAuthenticator(self.__zmqContext)
            self.__authenticator.start()
            self.__authenticator.configure_plain(
                domain="*",
                passwords={username: password}
            )                        
            self.__publishSocket.plain_server = True
            self.__replySocket.plain_server = True

        # Bind socket adress 
        self.__replySocket.bind(replyAdress)   
        self.__publishSocket.bind(publishAdress) 

        self.setActive(True)

        self.__thread = Thread(target=self.run)
        self.__thread.start()

    def run(self):
        """ Run Server functions """

        startDatetime = datetime.utcnow()    
        
        while self.isActive():
            currentDatetime = datetime.utcnow()
            delta = currentDatetime - startDatetime

            if delta >= timedelta(seconds=1):
                self.publish("_keep_alive", currentDatetime)

            if not self.__replySocket.poll(1000):
                continue

            # Recieve request data from Reply socket
            request = self.__replySocket.recv_pyobj()

            # Get function name and parameters
            name, arguments, keywordArguments = request
            # Try to get and execute callable function object; capture exception information if it fails
            try:
                func = self.__functions[name]
                r = func(*arguments, **keywordArguments)
                rep = [True, r]
            except Exception as exception:
                rep = [False, traceback.format_exc()]

            # send callable response by Reply socket
            self.__replySocket.send_pyobj(rep)

        self.__publishSocket.unbind(self.__publishSocket.LAST_ENDPOINT)
        self.__replySocket.unbind(self.__replySocket.LAST_END_POINT)



    def publish(self, topic, data):
        """ 發布數據 """
        with self.__threadLock:
            self.__publishSocket.send_pyobj([topic, data])


class RpcService:

    def __init__(self):
        self.__replyAdress = "tcp://*:2014"
        self.__publishAdress = "tcp://*:4102"
        self.__rpcServer = None
        self.initializeRpcServer()


    def initializeRpcServer(self):
        """ 初始化RPC伺服器 """
        self.__rpcServer = RemoteProcedureCallServer()


    def start(self, replyAdress, publishAdress):
        """ 啟動 
        Arguments:
        replyAdress (str): 回應地址
        publishAdress (str): 廣播地址
        """

        if self.__rpcServer.isActive():
            print("RPC 運行中")

        self.__replyAdress = replyAdress
        self.__publishAdress = publishAdress
        
        try:
            self.__rpcServer.start(replyAdress, publishAdress)
        except:
            message = traceback.format_exc()
            print(f"RPC伺服器啟動失敗. [{message}]")
            return False


        print(f"RPC伺服器啟動成功")
        return True    


class RemoteProcedureCallClient():
    """ 遠端程序調用客戶端 """


    


if __name__ == '__main__':
    
    replyAdress = "tcp://127.0.0.1:2014"
    publishAdress = "tcp://127.0.0.1:4102"
    service = RpcService()
    service.start(replyAdress, publishAdress)
    
