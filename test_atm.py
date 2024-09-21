import unittest
from atm import ATM

class TestATM(unittest.TestCase):
    def setUp(self):
        self.atm = ATM()

    def test_initial_balance(self):
        self.assertEqual(self.atm.balance, 0)

    def test_deposit(self):
        self.atm.deposit(100)
        self.assertEqual(self.atm.balance, 100)

    def test_withdraw(self):
        self.atm.deposit(100)
        self.atm.withdraw(50)
        self.assertEqual(self.atm.balance, 50)

    def test_withdraw_insufficient_funds(self):
        self.atm.withdraw(50)
        self.assertEqual(self.atm.balance, 0)

if __name__ == '__main__':
    unittest.main()
