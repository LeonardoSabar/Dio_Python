import time
from datetime import datetime

class Bank:
    def __init__(self, name, account_number, balance, transaction_type, withdraw_limit):
        self.name = name
        self.account_number = account_number
        self.balance = balance
        self.transaction_type = transaction_type
        self.withdraw_limit = withdraw_limit
        self.time = time.time()
        self.next = None

def lst_add_back(head, name, account_number, balance, transaction_type, withdraw_limit):
    new_bank = Bank(name, account_number, balance, transaction_type, withdraw_limit)
    if head is None:
        return new_bank
    last = head
    while last.next:
        last = last.next
    last.next = new_bank
    return head

def print_history(head):
    temp = head
    while temp:
        print(f"Name: {temp.name}")
        print(f"Account number: {temp.account_number}")
        print(f"Balance: {temp.balance}")
        print(f"Transaction type: {temp.transaction_type}")
        print(f"Withdraw limit: {temp.withdraw_limit}")
        print(f"Time: {datetime.fromtimestamp(temp.time).strftime('%Y-%m-%d %H:%M:%S')}")
        print("\n")
        temp = temp.next

def store_history_in_file(head):
    with open("history.txt", "w") as file:
        temp = head
        while temp:
            file.write(f"Name: {temp.name}\n")
            file.write(f"Account number: {temp.account_number}\n")
            file.write(f"Balance: {temp.balance}\n")
            file.write(f"Transaction type: {temp.transaction_type}\n")
            file.write(f"Withdraw limit: {temp.withdraw_limit}\n")
            file.write(f"Time: {datetime.fromtimestamp(temp.time).strftime('%Y-%m-%d %H:%M:%S')}\n")
            file.write("\n")
            temp = temp.next

def free_list(head):
    temp = head
    while temp:
        next_node = temp.next
        del temp
        temp = next_node
    head = None

def create_account():
	print("\n================ Create Account ===============\n")
	name = input("Enter your name: ")
	account_number = int(input("Enter your account number: "))
	print("\nAccount created successfully\n")
	return name, account_number

def deposit(balance):
	print("\n=================== Deposit ===================\n")
	amount = int(input("Enter the amount to deposit: "))
	balance += amount
	print("\nAmount deposited successfully\n")
	return balance

def withdraw(balance, withdraw_limit):
	print("\n=================== Withdraw ==================\n")
	if withdraw_limit == 0:
		print("You have reached the withdraw limit!\n")
		return balance, withdraw_limit
	amount = int(input("Enter the amount to withdraw: "))
	if amount > 500:
		print("\nWithdraw limit exceeded\n")
		return balance, withdraw_limit
	elif amount > balance:
		print("Insufficient balance\n")
		return balance, withdraw_limit
	elif amount <= balance and amount <= 500 and withdraw_limit > 0:
		balance -= amount
		withdraw_limit -= 1
		print("\nAmount withdrawn successfully\n")
		return balance, withdraw_limit

def check_balance(balance):
	print("\n================ Check Balance ================\n")
	if balance == 0:
		print("There is no balance history.\n")
	else:
		print(f"Your balance is: R$ {balance}\n")
	print("\n===============================================\n")

def menu():
	print("\n============= Welcome to the bank =============\n")
	print("1. Create Account")
	print("2. Deposit")
	print("3. Withdraw")
	print("4. Check Balance")
	print("5. Transaction History")
	print("6. Exit")
	print("\n===============================================\n")
	try:
		choice = int(input("Enter your choice: "))
		return choice
	except ValueError:
		print("\nInvalid choice\n")
		return None

def main():
	withdraw_limit = 3
	head = None
	balance = 0
	while True:
		choice = menu()
		if choice == 1:
			account = create_account()
			if account:
				name, account_number = account
				head = lst_add_back(head, name, account_number, balance, "Create account", withdraw_limit)
		elif choice == 2:
			balance = deposit(balance)
			head = lst_add_back(head, name, account_number, balance, "Deposit", withdraw_limit)
		elif choice == 3:
			balance, withdraw_limit = withdraw(balance, withdraw_limit)
			head = lst_add_back(head, name, account_number, balance, "Withdraw", withdraw_limit)
		elif choice == 4:
			check_balance(balance)
			head = lst_add_back(head, name, account_number, balance, "Check balance", withdraw_limit)
		elif choice == 5:
			if head is None:
				print("There is no transaction history\n")
			else:
				print("\n============= Transaction History =============\n")
				print_history(head)
				print("\n===============================================\n")
		elif choice == 6:
			print("Exit")
			break
		else:
			print("Invalid choice")

	store_history_in_file(head)
	free_list(head)

main()
