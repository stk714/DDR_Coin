import os
import json
from web3 import Web3
from pathlib import Path
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

# Define and connect a new Web3 provider
w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))

################################################################################
# Contract Helper function:
# 1. Loads the contract once using cache
# 2. Connects to the contract using the contract address and ABI
################################################################################

# Cache the contract on load
@st.cache(allow_output_mutation=True)

# Define the load_contract function
def load_contract():

    # Load Contract ABI
    with open(Path("./contracts/compiled/contract_abi.json")) as contract_file:
        contract_abi = json.load(contract_file)

    # Set the contract address (this is the address of the deployed contract)
    contract_address = os.getenv("SMART_CONTRACT_ADDRESS")

    # Get the contract using web3
    contract = w3.eth.contract(
        address = contract_address,
        abi = contract_abi
    )

    # Return the contract from the function
    return contract


# Load the contract
contract = load_contract()


################################################################################
# Award Driver
################################################################################

accounts = w3.eth.accounts
account = accounts[0]
dd_account = st.selectbox("Select Designated Driver", options=accounts)
contract_details = st.text_input("Contract Details", value="Designated Driver Receives Payout")
if st.button("Award Designated Driver"):
    contract.functions.awardCertificate(dd_account, contract_details).transact({'from': account, 'gas': 1000000})

################################################################################
# Display Award
################################################################################
award_id = st.number_input("Enter a Award Token ID to display", value=0, step=1)
if st.button("Display Award"):
    # Get the award owner
    award_owner = contract.functions.ownerOf(award_id).call()
    st.write(f"The certificate was awarded to {award_owner}")

    # Get the certificate's metadata
    token_uri = contract.functions.tokenURI(award_id).call()
    st.write(f"The Award's tokenURI metadata is {token_uri}")
