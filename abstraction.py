from abc import ABC, abstractmethod


class rent(ABC):
    def paySlip(self, amount):
        print("Your rent purchase amount: ", amount)
# this function is telling us to pass in an argument, but we won't tell you
# how or what kind of data it will be.

    @abstractmethod
    def payment(self, amount):
        pass


class DebitCardPayment(rent):
    # here we've defined how to implement the payment function from
    # it's parent paySlip class.
    def payment(self, amount):
        print('Your rent purchase amount of {} exceeded your $500 limit '.format(amount))


obj = DebitCardPayment()
obj.paySlip("$550")
obj.payment("$550")
