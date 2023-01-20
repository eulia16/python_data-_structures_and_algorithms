#insert _set_balance and _get_balance methods in CreditCard and PredatoryCraditCard classes


class CreditCard():
    
    """A Consumer Credit Card"""
    
    def __init__(self,customer,bank,acct,limit):
        """
        Create a new Credit Card Instance
        
        The initial balance is Zero
        customer - the name of the customer (e.g., John Bowman )
        bank - the name of the bank (e.g., California Savings )
        acnt - the acount identifier (e.g., 5391 0375 9387 5309 )
        limit credit limit (measured in dollars)
        
        """
        self._customer = customer
        self._bank = bank
        self._account = acct
        self._limit = limit
        self._balance = 0
        
    def _set_balance(self, passedNum):
        """
        A function to Change the  balance and manipulate it
        
        """
        self._balance = passedNum       
 
        #Write your Function here to play with 'balance' parameter......
        #pass
         
    def get_customer(self):
        
        """get the name of the customer"""
        
        return (self._customer)
    
    def get_bank(self):
        
        """Returns the bank's name"""
        
        return (self._bank)
    
    def get_account(self):
        
        """Returns the card identifying number (String)"""
        
        return (self._account)
    
    def get_limit(self):
        
        """Returns the current credit limit"""
        
        return (self._limit)
    
    def get_balance(self):
        
        """Returns the current balance"""
        
        return (self._balance)
    
    def charge(self,price):
        
        """
        Charge given price to the card, assuming sufficient credit limit.
        Return True if charge was processed; False if charge was denied.
        
        """
        if price + self._balance > self._limit:
            return False
        else:
            self._balance+=price
            return True
        
    def make_payment(self,amount):
        
        """
        Makes payment that reduces balance
        """
        
        self._balance = self._balance-amount
        
class PredatoryCreditCard(CreditCard):
    
    def __init__(self,customer,bank,acct,limit,apr):
        """
        Create a new predatory credit card instance.
        The initial balance is zero.
        
        customer the name of the customer (e.g., John Bowman )
        bank the name of the bank (e.g., California Savings )
        acnt the acount identifier (e.g., 5391 0375 9387 5309 )
        limit credit limit (measured in dollars)
        apr annual percentage rate (e.g., 0.0825 for 8.25% APR)
        
        """
        super().__init__(customer,bank,acct,limit)
        self._apr=apr
        super()._set_balance()
        
    def charge(self,price):
        """
        Charge given price to the card, assuming sufficient credit limit.
        Return True if charge was processed.
        Return False and assess 5 fee if charge is denied.
        
        """
        success = super().charge(price) #call inherited value
        if not success:
            self._balance+=5            #assess penalty
        return success                  #caller expects value
    
    def process_month(self):
        """
        Assess monthly interest on outstanding balance.
        
        """
        if self._balance > 0:
            # if positive balance, convert APR to monthly multiplicative factor
            monthly_factor = pow(1 + self._apr, 1/12)
            self._balance*=monthly_factor
        return (self._balance)
            
#Code Fragment 2.7: A subclass of CreditCard that assesses interest and fees.
#CreditCard and PredatoryCreditCard are changed accordingly 

