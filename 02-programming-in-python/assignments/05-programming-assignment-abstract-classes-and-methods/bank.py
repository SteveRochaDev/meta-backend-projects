# Import ABC and abstractmethod from the module abc
from abc import ABC, abstractmethod

# Abstract Class Bank
class Bank(ABC):
    """ An abstract bank class """

    def basicinfo(self):
        print("This is a generic bank")
        return "Generic bank: 0"

    @abstractmethod
    def withdraw(self, amount):
        pass


# Subclass Swiss
class Swiss(Bank):
    """ A specific type of bank that derives from class Bank """

    def __init__(self):
        self.bal = 1000

    def basicinfo(self):
        print("This is the Swiss Bank")
        return f"Swiss Bank: {self.bal}"

    def withdraw(self, amount):
        if amount <= self.bal:
            self.bal -= amount
            print(f"Withdrawn amount: {amount}")
            print(f"New Balance: {self.bal}")
            return self.bal
        else:
            print("Insufficient funds")
            return self.bal


# Driver Code
def main():
    assert issubclass(Bank, ABC), "Bank must derive from class ABC"
    s = Swiss()
    print(s.basicinfo())
    s.withdraw(30)
    s.withdraw(1000)


if __name__ == "__main__":
    main()