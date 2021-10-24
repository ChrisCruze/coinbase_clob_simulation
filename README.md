# coinbase_clob_simulation
Load a snapshot of a central limit order book and replay state modifications 


Would it be better to filter out all messages less than the sequence number before or filter only after the first time it appears? The difference could result in different number of messages since sequence number can decrease


Sequence Numbers
Most feed messages contain a sequence number. Sequence numbers are increasing integer values for each product with every new message being exactly 1 sequence number greater than the one before it.

If you see a sequence number that is more than one value from the previous, it means a message has been dropped. A sequence number less than one you have seen can be ignored or has arrived out-of-order. In both situations you may need to perform logic to make sure your system is in the correct state.


- https://docs.cloud.coinbase.com/exchange/docs/overview



