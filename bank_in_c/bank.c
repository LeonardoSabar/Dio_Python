#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <string.h>

typedef struct bank
{
	char name[100];
	int account_number;
	int balance;
	char transaction_type[100];
	int withdraw_limit;
	time_t time;
	struct bank *next;
} bank;



void	lst_add_back(bank **head, char name[], int account_number, int balance, char transaction_type[], int withdraw_limit)
{
	bank *new_bank = (bank *)malloc(sizeof(bank));
	bank *last = *head;
	new_bank->account_number = account_number;
	new_bank->balance = balance;
	new_bank->withdraw_limit = withdraw_limit;
	strcpy(new_bank->name, name);
	strcpy(new_bank->transaction_type, transaction_type);
	new_bank->time = time(NULL);
	new_bank->next = NULL;

	if (*head == NULL)
	{
		*head = new_bank;
		return;
	}

	while (last->next != NULL)
		last = last->next;

	last->next = new_bank;
}

void	print_history(bank *head)
{
	bank *temp = head;
	printf("Name: %s\n", temp->name);
	printf("Account number: %d\n", temp->account_number);
	while (temp != NULL)
	{
		printf("Balance: %d\n", temp->balance);
		printf("Transaction type: %s\n", temp->transaction_type);
		printf("Withdraw limit: %d\n", temp->withdraw_limit);
		printf("Time: %s\n", ctime(&temp->time));
		printf("\n");
		temp = temp->next;
	}
}

void	store_history_in_file(bank *head)
{
	FILE *file = fopen("history.txt", "w");
	bank *temp = head;
	fprintf(file, "Name: %s\n", temp->name);
	fprintf(file, "Account number: %d\n", temp->account_number);
	while (temp != NULL)
	{
		fprintf(file, "Balance: %d\n", temp->balance);
		fprintf(file, "Transaction type: %s\n", temp->transaction_type);
		fprintf(file, "Withdraw limit: %d\n", temp->withdraw_limit);
		fprintf(file, "Time: %s\n", ctime(&temp->time));
		fprintf(file, "\n");
		temp = temp->next;
	}
	fclose(file);
}

void	free_list(bank **head)
{
	bank *temp = *head;
	bank *next;

	while (temp != NULL)
	{
		next = temp->next;
		free(temp);
		temp = next;
	}
	*head = NULL;
}

int withdraw_limit = 3;

int	main()
{
	bank *head = NULL;
	int choice = 0;
	int account_number = 0;
	int balance = 0;
	int amount = 0;
	char name[100];

	while(1)
	{
		printf("\n============= Welcome to the bank =============\n\n");
		printf("1. Create Account\n");
		printf("2. Deposit\n");
		printf("3. Withdraw\n");
		printf("4. Check Balance\n");
		printf("5. Transaction History\n");
		printf("6. Exit\n");
		printf("\n===============================================\n\n");
		printf("Enter your choice: ");
		scanf("%d", &choice);
		if (choice == 1)
		{
			printf("\n================ Create Account ===============\n\n");
			printf("Enter your name: ");
			scanf("%s", name);
			printf("\nEnter your account number: ");
			scanf("%d", &account_number);
			printf("\nAccount created successfully\n\n");
			lst_add_back(&head, name, account_number, balance, "Create account", withdraw_limit);
		}
		else if (choice == 2)
		{
			printf("\n=================== Deposit ===================\n\n");
			printf("Enter the amount to deposit: ");
			scanf("%d", &amount);
			balance = balance + amount;
			printf("\nAmount deposited successfully\n\n");
			lst_add_back(&head, name, account_number, balance, "Deposit", withdraw_limit);
		}
		else if (choice == 3)
		{
			printf("\n=================== Withdraw ==================\n\n");
			if (withdraw_limit == 0)
				printf("You have reached the withdraw limit!\n");
			printf("Enter the amount to withdraw: ");
			scanf("%d", &amount);

			if (amount > 500)
			{
				printf("\nWithdraw limit exceeded\n");
				lst_add_back(&head, name, account_number, balance, "Withdraw limit exceeded", withdraw_limit);
			}

			else if (amount > balance)
			{
				printf("Insufficient balance\n");
				lst_add_back(&head, name, account_number, balance, "Insufficient balance", withdraw_limit);
			}

			else if (amount <= balance && amount <= 500 && withdraw_limit > 0)
			{
				balance = balance - amount;
				withdraw_limit = withdraw_limit - 1;
				printf("\nAmount withdrawn successfully\n");
				lst_add_back(&head, name, account_number, balance, "Withdraw", withdraw_limit);
			}
		}
		else if (choice == 4)
		{
			printf("\n================ Check Balance ================\n\n");
			if (balance == 0)
				printf("There is no balance history.\n");

			else if (balance > 0)
				printf("Your balance is: R$ %d\n", balance);

			printf("\n===============================================\n\n");

			lst_add_back(&head, name, account_number, balance, "Check balance", withdraw_limit);
		}
		else if (choice == 5)
		{
			if (head == NULL)
				printf("There is no transaction history\n");
			else
			{
				printf("\n============= Transaction History =============\n");
				print_history(head);
				printf("\n===============================================\n");
			}
		}
		else if (choice == 6)
		{
			printf("Exit");
			break;
		}
		else
			printf("Invalid choice");
	}

	store_history_in_file(head);
	free_list(&head);

	return 0;
}
