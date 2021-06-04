pragma solidity ^0.5.17;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20Detailed.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20Mintable.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC721/ERC721Full.sol";

// Create Designated Driver Roulette (DDR) contract inherit the following OpenZeppelin:

contract DDRCoin is ERC20, ERC20Detailed, ERC20Mintable {
    constructor(
        string memory name,
        string memory symbol,
        uint initial_supply
    )
        ERC20Detailed(name, symbol, 18)
        public
    {

    }
}

// Create contract DDRCoin. Deploy contract. Name: DDRCoin, Symbol: DDR, Inital_supply: 40
// Created contract address: 0xa362B0F565f2d864503da1814231951f62D1dFEE

// Create wallet for 4 individuals. Each wallet receives 10 coin
// Account1: Susannah = 0x05BDAc66297e6283d8154a8E2727ee6F4BC9217F
// Account2: Sarah = 0x82D9592130b3B9Ee1e2134873f56C1B56d495108
// Account3: Callie = 0x947fFc4Be9797e3E8EFdf336692619F242d65DF9
// Account4: Gabriel = 0x50b40a7Ba0c437ff25521bA43e47e6b0F1384A02

// Roulette assigns Designated Driver
// Transfer all 40 coins to the Designated Driver
// Edit contract to only payout after event date
