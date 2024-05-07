WITHDRAW_LIMIT = 3

while True:
		print("Welcome to the bank")
		print("1. Create Account")
		print("2. Deposit")
		print("3. Withdraw")
		print("4. Check Balance")
		print("5. Exit")

		try:
			choice = int(input("Enter your choice: "))
		except ValueError:
			print("\nInvalid choice\n")
			continue

		if choice == 1:
			print("Create Account\n")
			name = input("Enter your name: ")
			try:
				account_number = int(input("Enter your account number: "))
				balance = int(input("Enter your balance: "))
			except ValueError:
				print("\nInvalid input\n")
				continue
			print("\nAccount created successfully\n")

		elif choice == 2:
			print("Deposit")
			try:
				amount = int(input("Enter the amount to deposit: "))
			except ValueError:
				print("\nInvalid input\n")
				continue
			balance = balance + amount
			print("Amount deposited successfully\n")

		elif choice == 3:
			print("Withdraw")
			if WITHDRAW_LIMIT == 0:
				print("You have reached the withdraw limit")
				continue
			try:
				amount = int(input("Enter the amount to withdraw: "))
			except ValueError:
				print("\nInvalid input\n")
				continue
			if amount > 500:
				print("\nWithdraw limit exceeded\n")
			elif amount > balance:
				print("Insufficient balance\n")
			else:
				balance = balance - amount
				WITHDRAW_LIMIT = WITHDRAW_LIMIT - 1
				print("Amount withdrawn successfully\n")

		elif choice == 4:
			print("\n==========Check Balance==========\n")
			print("There is no balance history." if not balance else f"Your balance is: R$ {balance:.2f}")
			print("\n=================================\n")

		elif choice == 5:
			print("Exit")
			break
		else:
			print("Invalid choice")
