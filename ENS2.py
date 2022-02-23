import json
import urllib.request
import web3

from web3 import Web3
from ens.auto import ENS

# Initialise WEB3 ENS
w3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/e1aff836d3a64d6aba0f028217da381f"))
ns = ENS.fromWeb3(w3)



rrabi = [
  {
    "inputs": [
      {
        "internalType": "contract ENS",
        "name": "_ens",
        "type": "address"
      }
    ],
    "stateMutability": "nonpayable",
    "type": "constructor"
  },
  {
    "inputs": [
      {
        "internalType": "address[]",
        "name": "addresses",
        "type": "address[]"
      }
    ],
    "name": "getNames",
    "outputs": [
      {
        "internalType": "string[]",
        "name": "r",
        "type": "string[]"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  }
]



rrcontract = w3.eth.contract(address = Web3.toChecksumAddress('0x3671aE578E63FdF66ad4F3E12CC0c0d71Ac7510C'), abi = rrabi)


# Get transactions
req = urllib.request.urlopen('https://api.etherscan.io/api?module=account&action=txlist&address=0x084b1c3c81545d370f3634392de611caabff8148&sort=desc&apikey=7I39Q4ZZ6SER7ZZTKQMNGYHD3UTZ6BSQ32')
resp = req.read()
tr = json.loads(resp)

print('---')


addresses = []
i = 0
for txh in tr["result"]:
    
    addresses.append(Web3.toChecksumAddress(txh["from"]))
    i += 1
    if i == 1000:
        break


names = rrcontract.functions.getNames(addresses).call()

i = 0
for n in names:
    print(addresses[i] + "---" + n)
    i += 1





