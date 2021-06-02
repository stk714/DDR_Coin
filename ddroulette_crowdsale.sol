pragma solidity ^0.5.17;

import "./ddroulette.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/Crowdsale.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/emission/MintedCrowdsale.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/validation/CappedCrowdsale.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/validation/TimedCrowdsale.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/distribution/RefundablePostDeliveryCrowdsale.sol";


// Have the DDRCrowdsale contract inherit the following OpenZeppelin:

contract DDRCrowdsale is Crowdsale, MintedCrowdsale, CappedCrowdsale, TimedCrowdsale, RefundablePostDeliveryCrowdsale { 
    // UPDATE THE CONTRACT SIGNATURE TO ADD INHERITANCE
    // Provide parameters for all of the features of your crowdsale, such as the `rate`, `wallet` for fundraising, and `token`.
    constructor(
        uint256 rate,  // rate in TKNbits
        address payable wallet, // sale beneficiary
        DDRCoin token, // the DDR Coin itself that the DDRCrowdsale will work with
        uint goal, // the crowdsale goal
        uint open, // the crowdsale opening time
        uint close // the crowdsale closing time
        ) public 
            Crowdsale(rate, wallet, token)
            CappedCrowdsale(goal)
            TimedCrowdsale(open, close)
            RefundablePostDeliveryCrowdsale(goal)
        {
        // constructor can stay empty
        }
}

contract DDRCoinCrowdsaleDeployer {
    // Create an `address public` variable called `kasei_token_address` which will store KaseiCoin's address once that contract has been deployed
    // Create an `address public` variable called `kasei_crowdsale_address` which will store KaseiCoinCrowdsale's address once that contract has been deployed
    address public ddr_token_address;
    address public ddr_crowdsale_address;
    
    // Add the constructor.
    constructor(
        string memory name,
        string memory symbol,
        address payable wallet, // this address will receive all Ether raised by the sale
        uint256 goal
    ) public {
        // Create a new instance of the DDRCoin contract.
        DDRCoin token = new DDRCoin(name, symbol, 0);
        
        // Assign the token contract’s address to the `ddr_token_address` variable.
        ddr_token_address = address(token);
        
        // Create a new instance of the `DDRCrowdsale` contract
        DDRCrowdsale ddr_crowdsale = new DDRCrowdsale(1, wallet, token, goal, now, now + 24 hours);
        
        // Assign the `DDRCrowdsale` contract’s address to the `ddr_crowdsale_address` variable.
        ddr_crowdsale_address = address(ddr_crowdsale);
        
        // Set the `DDRCrowdsale` contract as a minter
        token.addMinter(ddr_crowdsale_address);
        
        // Have the `DDRCoinCrowdsaleDeployer` renounce its minter role.
        token.renounceMinter();
    }
}