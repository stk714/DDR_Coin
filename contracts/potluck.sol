pragma solidity ^0.5.0;

contract BankAccount {
    address payable accountOwner = 0xD81b7D4224c017FC839Dc2a95D77Fbb6237B8383;

    function withdraw(uint amount, address payable recipient) public {
        require(recipient == accountOwner, "You don’t own this account!");
        return recipient.transfer(amount);
    }

    function deposit() public payable {}

    function() external payable {}
}

contract CustomerAccount {
    address payable owner;
    bool isNewAccount;
    uint public accountBalance;
    string customerName;
    string customerLastName;
    address payable authorizedRecipient;

    function getInfo() view public returns(address, address payable, bool, uint, string memory, string memory) {
        return (owner, authorizedRecipient, isNewAccount, accountBalance, customerName, customerLastName);
    }

    function setInfo(address payable newOwner, address payable newAuthorizedRecipient, bool newAccountStatus, uint newAccountBalance, string memory newCustomerName, string memory newCustomerLastName) public {
        owner = newOwner;
        authorizedRecipient = newAuthorizedRecipient;
        isNewAccount = newAccountStatus;
        accountBalance = newAccountBalance;
        customerName = newCustomerName;
        customerLastName = newCustomerLastName;
    }

    function sendRemittance(uint amount, address payable recipient) public {
        require(recipient == owner || recipient == authorizedRecipient, "The recipient address is not authorized!");
        recipient.transfer(amount);
        accountBalance = address(this).balance;
    }

    function deposit() public payable {
        accountBalance = address(this).balance;
    }

    function() external payable {}
}
