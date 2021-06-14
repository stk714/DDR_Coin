
pragma solidity ^0.5.17;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20Detailed.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20Mintable.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC721/ERC721Full.sol";

// Create Designated Driver Roulette (DDR) contract inherit the following OpenZeppelin:
contract DDRCoin is ERC20, ERC20Detailed, ERC20Mintable {
    address  payable public owner = 0xD81b7D4224c017FC839Dc2a95D77Fbb6237B8383;
    // address payable susanah = 0x1499112bF48CbCBe1023A9dA7f6bA40e88d28c81;
    // address payable sarah = 0xED8706cf7294f1c4F76D54EBEbD3b48D78C72CA6;
    uint public potluck = 0;
    bool susannah_paid = false;
    bool sarah_paid = false;
    bool gabe_paid = false;
    bool callie_paid = false;

    uint exchange_rate = 1000000;
    constructor(
        string memory name,
        string memory symbol,
        uint initial_supply
    )
        ERC20Detailed(name, symbol, 18)
        public
    {
        // owner = msg.sender;
    }
    
    function sendRemittance(uint amount, address payable recipient, bool susannah_paid) public {
        require(recipient == owner, "The recipient address is not authorized!");
        recipient.transfer(amount);
        return true;
    }
    function deposit(uint balance, address msgSender) public payable {
        balance = address(this).balance;
        msgSender = msg.sender;
        
    // function pay_token(uint amount, address payable recipient) public returns (bool) {
    //     require(msg.sender!=owner, “you can’t buy tokens”);
    //     msg.sender.transfer()
    //     return true;
    // }
}

// contract MsgTest {
//     uint public balance = 0;
//     address public msgSender;
//     uint public msgValue;
//     function deposit() public payable {
//         balance = address(this).balance;
//         msgSender = msg.sender;
//         msgValue = msg.value;
//     }
// }