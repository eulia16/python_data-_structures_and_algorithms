#Credit card class with option to start an account with a starting balance instead of 0(this is the assignment for this problem)
class CreditCard:
    """A consumer credit card"""

    def __init__(self, customer, bank, act, limit):
        """Create a new credit card instance """
        self._customer = customer
        self._bank = bank
        self._act = act
        self._limit = limit
        #self._balance = balance

    def get_customer(self):
        return self._customer;
    def get_bank(self):
        return bank;
    def get_acct(self):
        return self._act;
    def get_limit(self):
        return self._limit;
    def get_balance(self):
        return self.balance;

    def charge(self, price):
        if price + self._balance > self._limit:
            return False;
        else:
            self._balance += price
            return True;

    def make_payment(self, amt):
        self._balance -= amount

class SecondaryCreditCard(CreditCard):
    
    def __init__(self, customer, bank, act, limit, balance = 0):
        super.__init()
        self.balance = balance
    def get_balance(self):
        return self.balance;

 
