
import os
import sys
sys.path.append(os.getcwd())
from enum import Enum





class TradeOrderService:


    def sendTradeOrder(self, tradeAccount, tradeOrder):
        """ 送出委託 """

    def cancelTradeOrderByTradeOrderId(self, tradeOrderId):
        """ 取消委託 
        Arguments:
            tradeOrderId (str): 委託單代號
        """ 
        tradeOrder.pendingCancel()
        exchangeTradingService.cancelTradeOrder(tradeOrder)
               


    def getTradeOrders(self):
        """
        Returns:
            List(TradeOrder)
        """

    def getOrderEstimate(self):
        """ """    

class EventType(Enum):
    """ 事件類型 """

    TICK_UPDATED_EVENT = 0
    KBAR_UPDATED_EVENT = 1
    TRADE_ORDER_SUBMIITED_EVENT = 2
    
    
    @classmethod
    def toList(cls):
        """"""
        return [typeTuple[1] for typeTuple in enumerate(EventType)]


class Event:

    def __init__(self, eventType):
        self.__eventType = eventType

    def getEventType(self):
        return self.__eventType        

class TickUpdatedEvent(Event):
    
    def __init__(self):
        super(TickUpdatedEvent, self).__init__(EventType.TICK_UPDATED_EVENT)


class EventMulticaster:

    def __init__(self):
        self.__eventHandlers = {}
        for eventType in EventType.toList():
            self.__eventHandlers[eventType] = []
        
    def getEventHandlers(self):
        """"""
        return self.__eventHandlers        


    def registerEventHandler(self, eventType, handler):
        self.__eventHandlers[eventType].append(handler)


    def multicastEvent(self, event):
        eventType = event.getEventType()
        self.__multicastEvent(event, eventType)

    def __multicastEvent(self, event, eventType):
        handlers = self.__eventHandlers[eventType]
        for handler in handlers:
            self.invokeHandler(handler, event, eventType)

    def invokeHandler(self, handler, Event, eventType):
        if eventType == EventType.TICK_UPDATED_EVENT:
            handler.onTickUpdatedEvent(event)




      

class ServiceHandler():


    def onBarUpdatedEvent(self, barUpdatedEvent):
        """ """
        print(barUpdatedEvent)

    def onTickUpdatedEvent(self, tickUpdatedEvent):
        """ """
        print(f"HANDLE EVENT: {tickUpdatedEvent.getEventType()}")

if __name__ == '__main__':
    eventMulticaster = EventMulticaster()
    eventHandler = ServiceHandler()
    eventMulticaster.registerEventHandler(EventType.TICK_UPDATED_EVENT, eventHandler)

    print(eventMulticaster.getEventHandlers())

    events = [
        TickUpdatedEvent(),
        TickUpdatedEvent(),
        TickUpdatedEvent(),
        TickUpdatedEvent(),
        TickUpdatedEvent(),
        TickUpdatedEvent(),
        TickUpdatedEvent(),
        TickUpdatedEvent()
    ] 
    for event in events:
        eventMulticaster.multicastEvent(event)
