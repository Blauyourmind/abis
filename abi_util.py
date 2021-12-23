from web3 import Web3
import requests
import json
from typing import List
import os

def fetch_contract_abi(contract_address: str) -> List:
    """Fetches ethereum smart contract ABI from the etherscan API
    Args:
        contract_address (string): ethereum address of a smart contract
    Raises:
        ValueError: raises when contract address is of an invalid format 
    Returns:
        JSON object: the input contract's ABI
    """
    
    api_key = os.environ.get("ETHERSCAN_API_KEY")
    url = f"https://api.etherscan.io/api?module=contract&action=getabi&address={contract_address}&apikey={api_key}"

    res = requests.get(url)
    res.raise_for_status()
        
    res_json = res.json()
    if res_json.get('status') == '1':
        abi_string = res_json.get('result')
        abi = json.loads(abi_string)
        return abi 
    else:
        raise ValueError(res_json.get('result'))
