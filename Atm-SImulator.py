#Cajero ATM

class ATM:
    def __init__(self, initial_balance=1000, correct_pin="1234"):
        self.balance = initial_balance
        self.pin = correct_pin
        self.attempts = 3

    def verify_pin(self):
        while self.attempts > 0:
            entered_pin = input("Enter your PIN: ")
            if entered_pin == self.pin:
                print("PIN correct. Accessing ATM...")
                return True
            else:
                self.attempts -= 1
                print(f"Incorrect PIN. Remaining attempts: {self.attempts}")
        print("Too many failed attempts. Account locked.")
        return False

    def check_balance(self):
        print(f"Your current balance is: ${self.balance}")

    def withdraw_money(self):
        try:
            amount = float(input("Enter the amount to withdraw: "))
            if amount > self.balance:
                print("Insufficient funds.")
            elif amount <= 0:
                print("Please enter a valid amount.")
            else:
                self.balance -= amount
                print(f"Withdrawal successful. New balance: ${self.balance}")
        except ValueError:
            print("Invalid input. Please try again.")

    def deposit_money(self):
        try:
            amount = float(input("Enter the amount to deposit: "))
            if amount <= 0:
                print("Please enter a valid amount.")
            else:
                self.balance += amount
                print(f"Deposit successful. New balance: ${self.balance}")
        except ValueError:
            print("Invalid input. Please try again.")

    def menu(self):
        if not self.verify_pin():
            return
        
        while True:
            print("\nATM Menu:")
            print("1. Check Balance")
            print("2. Withdraw Money")
            print("3. Deposit Money")
            print("4. Exit")
            
            option = input("Select an option: ")

            if option == "1":
                self.check_balance()
            elif option == "2":
                self.withdraw_money()
            elif option == "3":
                self.deposit_money()
            elif option == "4":
                print("Thank you for using the ATM. Goodbye.")
                break
            else:
                print("Invalid option. Please try again.")

# Run the ATM
atm = ATM()
atm.menu()
