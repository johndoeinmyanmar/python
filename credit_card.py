class CreditCard:
    """A consumer credit card."""

    def __init__(self, customer, bank, acnt, limit):
        """Create a new credit card instance.
	   
	The initial balance is zero.

	customer: the name of the customer(eg. 'John Bowman')
	bank:     the name of the bank (eg, 'California Savings')
	acnt:     the account identifier(eg., '2323 2323 5435 5332')
	limit:    credit card limit (measured in dollars)
	"""
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0

    def get_customer(self):
	"""Return the name of the customer"""
        return self._customer

    def get_bank(self):
	"""Return the bank's name."""
        return self._bank

    def get_account(self):
	"""Return the card identifying number (typically stored as string)."""
        return self._account

    def get_limit(self):
	"""Return current credit limit."""
        return self._limit

    def get_balance(self):
	"""Return the current balance."""
        return self._balance

    def charge(self, price):
	"""Charge given price to the card, assuming sufficient credit limit.
	
	Return True if charge was processed; False if charge is denied.
	"""
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
	"""Process customer payment that reduce payment."""
        self._balance -= amount


if __name__ == '__main__':
    wallet = []
    wallet.append(CreditCard('John', 'California Savings', '2323 4343 2324 6664', 2500))
    wallet.append(CreditCard('Brown', 'California Federal', '3434 3433 5322 4643', 3500))
    wallet.append(CreditCard('Johnny', 'California Finance', '2322 4433 4554 2222', 5000))

for val in range(1,17):
    wallet[0].charge(val)
    wallet[1].charge(2*val)
    wallet[2].charge(3*val)

for c in range(3):
    print('Customer = ', wallet[c].get_customer())
    print('Bank = ', wallet[c].get_bank())
    print('Account = ', wallet[c].get_account())
    print('Limit = ', wallet[c].get_limit())
    print('Balance =', wallet[c].get_balance())
    while wallet[c].get_balance() > 100:
        wallet[c].make_payment(100)
	print('New balance = ', wallet[c].get_balance())
    print()
