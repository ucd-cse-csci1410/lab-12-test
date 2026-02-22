"""
test_02_bank_account.py

Author: Chiranth Ajjamane Manohar
Date: 2026-02-05
Version: 0.1
Description: test file for the BankAccount class.
Copyright (c) 2026 University of Colorado Denver - Department of Computer Science

"""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from src.BankAccount import BankAccount


# # BankAccount.py
# # Author: Dr. Salim Lakhani
# # Date: November 07, 2020

# class BankAccount:
#     """Bank Account class which keep track of account balance"""
       

#     def __init__(self):
#         """Initialize balance to 0.00"""
#         self.balance = 0.00

#     def  deposit (self, amount):
#         """Make a deposit by adding amount to balance"""
#         if amount > 0:
#             self.balance = self.balance + amount
#             return True
#         else:
#             return False

#     def withdraw (self, amount):
#         """Withdraw money by deducting amount from the balance and return True.
#         If amount is more than the balance then reject it and return False"""

#         if amount <= self.balance:
#             self.balance = self.balance - amount
#             return True
#         else:
#             return False


#     def getBalance (self):
#         """Return the account balance"""
#         return self.balance


class TestBankAccount(unittest.TestCase):
    """Unit tests for BankAccount class."""

    # case_01: Test deposit method
    def test_01_deposit(self):
        """Test that deposit method adds amount to the balance."""
        bank_account = BankAccount()
        self.assertTrue(bank_account.deposit(100),
                        msg=f"\n Wrong output.\nExpected: True\nReceived: '{bank_account.deposit(100)}'")
       
    # case_02: Test withdraw method
    def test_02_withdraw(self):
        """Test that withdraw method subtracts amount from the balance."""
        bank_account = BankAccount()
        bank_account.deposit(100)
        self.assertTrue(bank_account.withdraw(50),
                        msg=f"\n Wrong output.\nExpected: True\nReceived: '{bank_account.withdraw(50)}'")
      
    # case_03: Test getBalance method
    def test_03_getBalance(self):
        """Test that getBalance method returns the balance."""
        bank_account = BankAccount()
        bank_account.deposit(100)
        self.assertEqual(bank_account.getBalance(), 100,
                         msg=f"\n Wrong output.\nExpected: 100\nReceived: '{bank_account.getBalance()}'")

if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(TestBankAccount))
    runner = unittest.TextTestRunner(stream=sys.stderr)
    result = runner.run(suite)
    if result.wasSuccessful():
        print("Test passed")
    else:
        print("Test failed")
        sys.exit(1)