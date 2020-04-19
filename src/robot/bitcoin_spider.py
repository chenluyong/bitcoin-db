import sqlite3
import requests,json


headers = {
  'Content-Type': 'text/plain',
  'Authorization': 'Basic cm9vdDoxMjM0NTY='
}
# for

def get_block_info(height):
    payload = '{"jsonrpc": "1.0", "id":"curltest", "method": "getblockhash", "params": [' + str(height) + '] }'

    response = requests.request("POST", url, headers=headers, data=payload)
    block_id = json.loads(response.text)["result"]
    print("block id:\t" + block_id)

    payload = '{"jsonrpc": "1.0", "id":"curltest", "method": "getblock", "params": ["' + block_id + '"] }'

    response = requests.request("POST", url, headers=headers, data=payload)
    txs = json.loads(response.text)["result"]
    return txs


def get_transaction(txid):
    payload = '{"jsonrpc": "1.0", "id":"curltest", "method": "getrawtransaction", "params": ["' + txid + '"] }'

    response = requests.request("POST", url, headers=headers, data=payload)

    tx_code = json.loads(response.text)
    code = tx_code["result"]

    payload = '{"jsonrpc": "1.0", "id":"curltest", "method": "decoderawtransaction", "params": ["' + code + '"] }'

    response = requests.request("POST", url, headers=headers, data=payload)

    tx = json.loads(response.text)["result"]
    return tx


block_info = get_block_info(511111)

txs = block_info["tx"]
for tx in txs:
    transaction = get_transaction(tx)
    print(transaction)