from brownie import *

def main():
    Analysis("0xa308828904977BbcEb91A9B0cb3dB07636734Fb7")

def Analysis(address):
    contract = Contract.from_explorer(address)
    abi = contract.abi
    d = {}
    for value in abi:
        if value['type'] in d:
            d[value['type']] += 1
        else:
            d[value['type']] = 1
    for key in list(d.keys()):
        print(key, ":", d[key])

# contract = Contract.from_explorer(address)
#     abi = contract.abi
#     inputTypes = {}
#     for value in abi:
#         for input in value['inputs']:
#             if input['type'] in inputTypes:
#                 inputTypes[input['type']] += 1
#             else:
#                 inputTypes[input['type']] = 1
#     for key in list(inputTypes.keys()):
#         print(key, ":", inputTypes[key])



    
    
