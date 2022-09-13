from base64 import decode
import json
import requests
import json

transaction = requests.get("https://mempool.observer/api/getMempoolEntries")
transaction =  transaction.json()
with open('getMempoolEntries.json', 'w') as f:
    json.dump(transaction, f)


block = requests.get("https://mempool.observer/api/getBlockEntries")
block =  block.json()
with open('getBlockEntries.json', 'w') as f:
    json.dump(block, f)