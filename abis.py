import os
import json
from typing import List

def read_abi(file_path:str) -> List:
	with open(file_path, 'r') as f:
		abi = json.loads(f.read())
	return abi

dirname = os.path.dirname(__file__)

ERC20_ABI = read_abi(dirname + '/ERC20.json')
ERC721_ABI = read_abi(dirname + '/ERC721.json')
ERC1155_ABI = read_abi(dirname + '/ERC1155.json')
CTOKEN_ABI = read_abi(dirname + '/CTOKEN.json')
CETHER_ABI = read_abi(dirname + '/CETHER.json')
COMPTROLLER_ABI = read_abi(dirname + '/COMPTROLLER.json')
UNISWAP_V2_FACTORY_ABI = read_abi(dirname + '/UNISWAP_V2_FACTORY.json')
