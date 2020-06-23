import Bank
import Input

balance = Bank.ATM.get_balance()
print (str.format("Starting balance: ${:.2f}", balance))
amount = Input.Validator.get_float("Please enter deposit amount ($0.00 - $1000.00): ",0.00,1000.00)
balance = Bank.ATM.deposit(amount)
print (str.format("New Balance: ${:.2f}", balance))

amount = Input.Validator.get_float("Please enter withdrawal amount ($0.00 - $1000.00): ",0.00,1000.00)
balance = Bank.ATM.withdraw(amount)
print (str.format("New Balance: ${:.2f}", balance))
