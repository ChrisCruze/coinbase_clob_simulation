import gzip
import json

def messages_parse(data):
    data_with_no_binary = str(data).split("'")[1:-1][0]
    data_list =[i for i in data_with_no_binary.split('\\n') if i != '']
    messages_data = [json.loads(D) for D in data_list]
    return messages_data 

def messages_read(file="../data/coinbase_BTC-USD_20_10_06_000000-010000.json.gz"):
    file_object = gzip.open(file, "r")
    data = file_object.read()
    messages_data = messages_parse(data)
    return messages_data 

def snapshot_read(file="../data/coinbase_BTC-USD_20_10_06_00_00.json"):
    snaphsot_data = json.loads(open(file,'r').read())
    return snaphsot_data

def messages_filter(messages_data,initial_clob,final_clob):
    messages_data_filtered = [message_dict for message_dict in messages_data if message_dict['sequence'] >= initial_clob['sequence'] and message_dict['sequence'] <= final_clob['sequence']]
    return messages_data_filtered

def data_load():    
    messages_data = messages_read()
    initial_clob = snapshot_read(file="../data/coinbase_BTC-USD_20_10_06_00_00.json")
    final_clob = snapshot_read(file="../data/coinbase_BTC-USD_20_10_06_00_15.json")
    messages_data_filtered = messages_filter(messages_data,initial_clob,final_clob)
    return initial_clob,final_clob,messages_data_filtered

    