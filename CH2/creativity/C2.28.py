#code stolen from github guy except the problem asked 


from Code_Fragment_Examples import CreditCard


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
        self.count_charge=0
        
    def charge(self,price):
        """
        Charge given price to the card, assuming sufficient credit limit.
        Return True if charge was processed.
        Return False and assess 5 fee if charge is denied.
        
        """
        self.count_charge+=1
        success = super().charge(price) #call inherited value
        if not success: #if the charge is not successfully processed, charge 5 dolla penalty, then check to see if above 10 calls, charge 1$
            self._balance = self._balance + 5
        if self.count_charge > 10:
            additional_charge()
       return success;  
               

 
    def process_month(self):
        """
        Assess monthly interest on outstanding balance.
        """
        if self._balance > 0:
            # if positive balance, convert APR to monthly multiplicative factor
            monthly_factor = pow(1 + self._apr, 1/12)
            self._balance*=monthly_factor
        return (self._balance)



   
    def additional_charge(self):
        """
        Additional charge of $1 for every additional call
        made to function charge beyond 10 calls
        """
        self._balance=self._balance+1
            
