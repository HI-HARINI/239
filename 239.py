import hashlib
import json
from time import time

chain = []

def block(proof, previous_hash=None):
	transaction={
	'sender':'Harini',
	'recipient':'Bob',
	'amount':'5 ETH'
	}
	data = {
		'index': 1,
		'timestamp': time(),
		'transactions': transaction,
		'block_reward':2.5554678439, 
		'uncles_reward': 0,
		'difficulty': 798427529305,
		'total_difficulty': 935869878937493984,
		'size': 7856,
		'gas_used': 4835638,
		'gas_limit':5848597,
		'gas/fee': 0.1,
		'proof': proof,
		'previous_hash': previous_hash
	}
	chain.append(data)
	print("block information:", data)
	string_object=json.dumps(data)
	print("json=",string_object)
	block_string=string_object.encode()
	print("encoded=",block_string)
	raw_hash=hashlib.sha256(block_string)
	print("sha256=",raw_hash)
	hex_hash=raw_hash.hexdigest()
	print("hexcode=",hex_hash)
	print(chain)
block(proof=000, previous_hash="No Previous Hash. Since this is the first block. ")