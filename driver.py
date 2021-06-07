# DDR Coin Wallet

################################################################################

# * Generate a new DDR Coin account instance by using your mnemonic seed phrase

# * Fetch and display the account balance associated with your DDR Coin account
# address.

# * Calculate the total value of an DDR Coin transaction, including the gas
# estimate, that pays a Designated Driver 

# * Digitally sign a transaction that pays driver, and send transaction to the Kovan testnet.

# * Review the transaction hash code associated with the validated blockchain transaction.

# Once you receive the transaction’s hash code, you can confirm on [Kovan’s
# Etherscan](https://kovan.etherscan.io/) website to review the blockchain
# transaction details. 

################################################################################
# Imports
import streamlit as st
from dataclasses import dataclass
from typing import Any, List

################################################################################
# Step 1:
# Import Ethereum Transaction Functions into the Fintech Finder Application

# Complete the following steps:

# 1. Review the code contained in the `wallet.py` script file. Note that
# the Ethereum transaction functions that you have built throughout this
# module-including `wallet`, `wallet.derive_acount`, `get_balance`, `fromWei`,
# `estimateGas`, `sendRawTransaction`, and others&mdash;have now been
# incorporated into Python functions that allow you to automate the process of
# accessing them.

# 2. Add your mnemonic seed phrase and your Infura project id to the '.env` file.

# 3. Import the following functions from the `wallet.py` file:
# * `participant_account`
# * `get_balance`
# * `send_transaction`

# 4. Within the Streamlit sidebar section of code, create a variable named
# `account`. Set this variable equal to a call on the `participant_account` function. 
# This function will create the participants' (in this
# case, your) HD wallet and Ethereum account.

# 5. Within this same section of the `finder.py` file, define a
# new `st.sidebar.write` function that will display the balance of the
# driver's account. Inside this function, call the `get_balance` function
# and pass it your DDR Coin `account.address`.

################################################################################
# Step 1 - Part 3:
# Import the following functions from the `crypto_wallet.py` file:
# * `participant_account`
# * `get_balance`
# * `send_transaction`

# From wallet.py import the functions generate_account, get_balance,
#  and send_transaction
from wallet import participant_account
from wallet import get_balance
from wallet import send_transaction

################################################################################
# Streamlit Code

# Streamlit application headings
st.markdown("# Designated Driver")
st.markdown("## Choose a Designated Driver!")
st.text(" \n")

################################################################################
# Participant Information

# Database of participants including their name, digital address, driver rating and hourly cost per Ether.
# A single Ether is currently valued at $1,500
participant_database = {
    "Susannah": ["Susannah", "0x05BDAc66297e6283d8154a8E2727ee6F4BC9217F", "5.0", 1.0,  "Images/susannah.png"],
    "Sarah": ["Sarah", "0x82D9592130b3B9Ee1e2134873f56C1B56d495108", "4.0", 0.9, "Images/sarah.png"],
    "Callie": ["Callie", "0x947fFc4Be9797e3E8EFdf336692619F242d65DF9", "3.0", 0.8, "Images/callie.png"],
    "Gabriel": ["Gabriel", "0x50b40a7Ba0c437ff25521bA43e47e6b0F1384A02", "2.0", 0.7, "Images/gabriel.png"]
}

# Show participants info
people = ["Susannah", "Sarah", "Callie", "Gabriel"]

def get_people():
    """Display the database of participant information."""
    db_list = list(participant_database.values())

    for number in range(len(people)):
        st.image(db_list[number][4], width=200)
        st.write("Name: ", db_list[number][0])
        st.write("DDR Coin Account Address: ", db_list[number][1])
        st.write("Driver Rating: ", db_list[number][2])
        st.write("Mileage Rate per DDR: ", db_list[number][3], "DDR")
        st.text(" \n")

get_people()


################################################################################
# Streamlit Sidebar Code - Start

st.sidebar.markdown("## Driver Account Address and Balance in DDR Coin")
################################################################################
account = participant_account()

st.sidebar.write(account.address)
# Write the returned ether balance to the sidebar
st.sidebar.write(get_balance(account.address))

# Create a select box to chose a Designated Driver
person = st.sidebar.selectbox('Select a Designated Driver', people)

# Create a input field to record the number of miles the driver drove
mileage = st.sidebar.number_input("Miles Driven")

st.sidebar.markdown("## Designated Driver Name, Rate per Mile, and DDR Coin Address")

# Identify the Driver
driver = participant_database[person][0]

# Write the driver's name to the sidebar
st.sidebar.write(driver)

# Identify the driver's hourly rate
mileage_rate = participant_database[person][3]

# Write the driver's rate to the sidebar
st.sidebar.write(mileage_rate)

# Identify the Driver's DDR Coin Address
driver_address = participant_database[person][1]

# Write the Driver's DDR Coin Address to the sidebar
st.sidebar.write(driver_address)

# Write the Fintech Finder candidate's name to the sidebar

st.sidebar.markdown("## Total Paid in DDR Coin")

ddr_coin = mileage_rate * mileage

# Write the `DDR Coin` calculation to the Streamlit sidebar
st.sidebar.write(ddr_coin)

if st.sidebar.button("Send Transaction"):
    # Call the `send_transaction` function and pass it 3 parameters:
    # Your `account`, the `candidate_address`, and the `wage` as parameters
    # Save the returned transaction hash as a variable named `transaction_hash`
    transaction_hash = send_transaction(account, driver_address, ddr_coin)
    # Markdown for the transaction hash
    st.sidebar.markdown("#### Validated Transaction Hash")
    # Write the returned transaction hash to the screen
    st.sidebar.write(transaction_hash)
    # Celebrate your successful payment
    st.balloons()

