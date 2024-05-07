WITHDRAW_LIMIT = 3

while TRUE:
		print("Welcome to the bank")
		print("1. Create Account")
		print("2. Deposit")
		print("3. Withdraw")
		print("4. Check Balance")
		print("5. Exit")
		choice = input("Enter your choice: ")

		if choice == '1':
			print("Create Account")
			name = input("Enter your name: ")
			account_number = input("Enter your account number: ")
			balance = input("Enter your balance: ")
			print("Account created successfully")

		if choice == '2':
			print("Deposit")
			amount = input("Enter the amount to deposit: ")
			balance = balance + amount
			print("Amount deposited successfully")

		if choice == '3':
			print("Withdraw")
			if WITHDRAW_LIMIT == 0:
				print("You have reached the withdraw limit")
				continue
			amount = input("Enter the amount to withdraw: ")
			if amount > 500:
				print("Withdraw limit exceeded")
			if amount > balance:
				print("Insufficient balance")
			else:
				balance = balance - amount
				WITHDRAW_LIMIT = WITHDRAW_LIMIT - 1
				print("Amount withdrawn successfully")

		if choice == '4':
			print("\n==========Check Balance==========\n")
			print("There is no balance history." if not balance else balance)
			print(f"Your balance is: R$ {balance:.2f}")
			print("\n=================================\n")

		if choice == '5':
			print("Exit")
			break
		else:
			print("Invalid choice")
			continue
