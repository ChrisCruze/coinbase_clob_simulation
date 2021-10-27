import logging
import queue
import data_load


logging.basicConfig(level=20)
logger = logging.getLogger()

class OrderDictTable:
    def __init__(self, order_items):
        self.order_dict = {} 
        self.assign_orders_dict(order_items)
        
    def assign_orders_dict(self,order_items):
        keys = [subli[2] for subli in order_items]#map(lambda price,size,order_id: order_id,order_items)
        self.order_dict = dict([(order_id,order_item) for (order_id,order_item) in zip(keys,order_items) ])
    
    def get_values(self):
        return self.order_dict.values()

    def get_obj(self):
        return self.order_dict

class CLOB:
    def __init__(self,clob):
        self.bids_obj = OrderDictTable(clob['bids']).get_obj()
        self.asks_obj = OrderDictTable(clob['asks']).get_obj()
        
    def order_remove(self,clob_bids_or_ask_dict,order_id):
        #logger.info('order_id: %s', str(order_id))
        removed_order = clob_bids_or_ask_dict.pop(order_id,None)
        #logger.info('clob_bids_or_ask_dict: %s', str(removed_order))
        
    def order_add(self,clob_bids_or_ask_dict,price,size,order_id):
        clob_bids_or_ask_dict[order_id] = [price,size,order_id]
        
    def update_from_message(self,message_obj):
        #logger.info('message_obj: %s', str(message_obj))
        message_type = message_obj['type']
        message_side = message_obj['side']
        clob_bids_or_ask_dict = self.asks_obj if message_side == 'sell' else self.bids_obj 
        #logger.info('message_side: %s', str(message_side))
        #logger.info('message_type: %s', str(message_type))

        if message_type == 'done':
            self.order_remove(clob_bids_or_ask_dict,message_obj['order_id'])
        elif message_type == 'open':
            self.order_add(clob_bids_or_ask_dict,message_obj['price'],message_obj['remaining_size'],message_obj['order_id'])
        
    def get_clob(self):
        return {
            'bids':self.bids_obj.values(),
            'asks':self.asks_obj.values()
        }


class CLOBSync:
    def clob_sync(self,initial_clob,final_clob,messages_data_filtered):
        clob = CLOB(initial_clob)
        q = queue.Queue()
        messages_queue_data = sorted(messages_data_filtered,key=lambda i: i['sequence'])


        list(map(q.put,messages_queue_data ))
        while not q.empty():
            message_obj = q.get()
            clob.update_from_message(message_obj)
        final_clob_processed = clob.get_clob()
        return final_clob_processed

initial_clob,final_clob,messages_data_filtered = data_load.data_load()

CLOBSync().clob_sync(initial_clob,final_clob,messages_data_filtered)




