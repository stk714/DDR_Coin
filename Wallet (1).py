# Cryptocurrency Wallet
################################################################################

# This file contains the Ethereum transaction functions that you have created throughout this module’s lessons. By using import statements, you will integrate this `crypto_wallet.py` Python script into the Fintech Finder interface program that is found in the `fintech_finder.py` file.

################################################################################
# Imports
import os
import requests
from dotenv import load_dotenv
load_dotenv()
from bip44 import Wallet
from web3 import Account
from web3.auto.infura.kovan import w3
from web3 import middleware
from web3.gas_strategies.time_based import medium_gas_price_strategy
from main.py import load_contract
from web3 import Web3
from web3 import EthereumTesterProvider 
from web3.auto import w3
from eth_account.messages import encode_defunct 

################################################################################
###Connecting to Blockchain using Web3.py Provider###

#Create an instance of Web3
w3 = Web3()

 #Create an instance of EthereumTesterProvider 
provider = EthereumTesterProvider()

 #Update the Web3 insatnce to include the provider
w3 = Web3(provider)

#Access information from the most recent blockchain 
w3.eth.get_block("latest")

#Access a list of accounts on block chain 
w3.eth.accounts

#Print list of accounts on the blockchain 
print(w3.eth.accounts)

#Access the balance of accounts using the address
w3.eth.get_balance()

#Access balance of an account using the address 
balance = w3.eth.get_balance()

#Convert balance from wei to ether
w3.fromWei(balance,"ether")

# Wallet functionality
#Module 19.1.5 ^

#Module 19.2.6
def participant_account():
    """Create a digital wallet and Ethereum account from a mnemonic seed phrase."""
    # Fetch mnemonic from environment variable.
    mnemonic = os.getenv("MNEMONIC")

    # Evaluate the contents of the mnemonic variable
    # Create a new mnemonic seed phrase if the value of mnemonic equals None
    if mnemonic is None:
        mnemonic = Mnemonic("english")
    mnemonic = mnemo.generate(strength=128)

    #Display value of mnemomic 
    display(mnemonic)

    # Create Wallet Object
    wallet = Wallet(mnemonic)
    wallet

    # Derive Ethereum Private Key
    private, public = wallet.derive_account("eth")

    #Display private key
    private

    # Convert private key into an Ethereum account
    account = Account.privateKeyToAccount(private)

    return account

def get_balance(address):
    """Using an Ethereum account address access the balance of Ether"""
    # Get balance of address in Wei
    wei_balance = w3.eth.get_balance(address)

    # Convert Wei value to ether
    ether = w3.fromWei(wei_balance, "ether")

    # Return the value in etherpi 
    return ether

#Module 19.2.8
#Signing and Verifying messages 

msg = ("")
message = encode_defunct(text=msg)

#Signing our message 
signed_messages = w3.eth.account,sign_message(message, private_key=private)
signed_messages

#Validate the transation signature against public key 
w3.eth.account.recover_message(message, signature=signed_messages.signature)

#Module 19.3.5

#Creating Transaction 
amount = ()
value = w3.toWei(amount,"ether")

#Specify receiver 
receiver = ""


def send_transaction(account, to, wage):
    """Send an authorized transaction to the Kovan testnet."""
    # Set gas price strategy
    w3.eth.setGasPriceStrategy(medium_gas_price_strategy)

    # Convert eth amount to Wei
    #value = w3.toWei(wage, "ether") --  repeated above

    # Calculate gas estimate
    gasEstimate = w3.eth.estimateGas({"to": to, "from": account.address, "value": value})

    # Construct a raw transaction
    raw_tx = {
        "to": to,
        "from": account.address,
        "value": value,
        "gas": gasEstimate,
        "gasPrice": w3.eth.generateGasPrice(),
        "nonce": w3.eth.getTransactionCount(account.address)
    }

    # Sign the raw transaction with ethereum account
    signed_tx = account.signTransaction(raw_tx)

    # Send the signed transactions
    return w3.eth.sendRawTransaction(signed_tx.rawTransaction)