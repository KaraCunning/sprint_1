class Wallet:

    # First thing we run when we make a class
    # outline required user-provided input values here
    def __init__(self, initial_amount=0):
        # save the user-provided initial_amount as an attribute
        self.balance = initial_amount

    # spend cash METHOD
    def spend_cash(self, amount):
        if self.balance < amount:
            return "not enough money"
        else:
            self.balance = self.balance - amount
            return f"remaining balance: {self.balance}"

    def add_cash(self, amount):
        self.balance = self.balance + amount
        return f"new balance of: {self.balance}"


    # __repr__ method
    # changes how the "object" looks when printed out
    # the presence of the self keyword allows me to access or 
    # modify class attributes within this function
    def __repr__(self):
        return f"wallet with balance of: ${self.balance}"
         



if __name__ == '__main__':
    wallet1 = Wallet(100)
    print(wallet1.add_cash(60))
    print(wallet1.spend_cash(180))
    print(wallet1.spend_cash(120))
    print(wallet1.balance)




