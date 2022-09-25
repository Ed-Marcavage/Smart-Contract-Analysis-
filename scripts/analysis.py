from brownie import *

def main():
    Analysis("0xa308828904977BbcEb91A9B0cb3dB07636734Fb7")

def Analysis(address):
    contract = Contract.from_explorer(address)
    print(contract.info())
