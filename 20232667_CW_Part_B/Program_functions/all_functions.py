'''
Author : Palihawadana A. A. N. Perera
IIT ID : 20232667
UoW ID : 20822596

project: SD 1 CW 1 Part B for year 23/24

'''

'''
Module Name: all_functions.py
-----------------------

'''         
'''
References
----------
NeuralNine (2022), 'Python Coding Conventions You Really Should Follow', YouTube.com (accessed: 13th March 2024)
no code was referenced from this reference, however the coding style and documentation style was adapted based on the recomendation of the author of the video reference.

Gaddis, T. (2008), 'Starting out with Python', 5th edn. London: Pearson. (accessed: March 2024)
Many of the input validation loops used in this program were adapted from code from this reference, as well as fundamental coding principals.

Astanin, S., Marsi, E., Ryder, B., et al (2024), 'Python-Tabulate', pypi.org, available at: https://pypi.org/project/tabulate/ (accessed: 13th March 2024)
The printit.py functions that use tabulate, reference code structure from this document.

Techiediaries (2023), 'Sorting Lists By Date in Python', techiediaries.com, available at: https://www.techiediaries.com/sort-lists-by-date-in-python/ (accessed: 13th March 2024)
the get_sorted_transactions(transactions_to_sort) function from basics.py uses logic recomended in this artich to sort transactions by date.

stackoverflow (2015), 'How to convert Python's .isoformat() string back into datetime object', available at: https://www.stackoverflow.com/questions/28331512/how-to-convert-pythons-isoformat-string-back-into-datetime-object (accessed: on 12th April 2024)
'''



import datetime
from tabulate import tabulate

def get_year() -> int: 
    
    # this function uses nested loops to check for exceptions and input validation.
    while True:  # this is a loop which will only break if the program encounters no exceptions and returns the value
        try:
            year:int = int(input("Enter the year: "))
            current_year:int = datetime.datetime.now().year # this gives us the current year based on system time
            if 0 < year <= current_year:
                return year # breaks all lops and returns the value.

            elif year > current_year: # if year in in the future
                print("Error: Invalid year, year cannot be in the future")

            else: # if the year is not greater than 0 it will continue to prompt the user for a valid input
                print("Error: Invalid Year, Year must be greater than 0")
            
        except ValueError: # expected exception handling.
            print("Error: Invalid Year, Year must be an integer") #afther printing the error message the loop will star over in the next loop iteration

def get_month() -> int:

    while True:
        try:            
            month:int = int(input("Enter the Month: "))
                
            if month in range(1,13,1):
                return month # breaks out of the loop and returns value

            elif month not in range(1,13,1):
                 print("Error: Invalid Month, Month must be an integer between 1 - 12") 
            
        except ValueError:
            print("Error: Invalid Month, Month must be an integer") # loop will start over if an exception happens.

def is_leap(year) -> bool:

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0): # checks if year is leap
        return True
    else:
        return False
    
def get_day(year: int, month: int) -> int:

    """Get a valid day input from the user."""
    # dict containing the maximum days for each month
    days_in_month:dict[int:int] = {
        1: 31, 2: 29 if is_leap(year) else 28,  # check if the year is leap
        3: 31, 4: 30, 5: 31, 6: 30, 7: 31,      # April to July
        8: 31, 9: 30, 10: 31, 11: 30, 12: 31     # August to December
    }
    while True:
        try:
            day:int = int(input(f"Enter the day for {year}-{month} (1-{days_in_month[month]}): "))
            if 1 <= day <= days_in_month[month]:# checks for validity.
                return day # breaks out of the function and loop
            else:
                print(f"Error: Day must be between 1 and {days_in_month[month]}.")
        except ValueError:
            print("Error: Invalid input. Please enter a valid day.")
    
def get_date() -> datetime.date:

    """
    args: None
    Proccess: Get a valid date (year-month-day) after validating the input.
    returns: datetime.date object.
    """

    year: int = get_year()
    if year == datetime.datetime.now().year:
        while True:
            month: int = get_month()
            if month > datetime.datetime.now().month: # checks if the month is in the future
                print("Error: Invalid Month: Month Cannot be in the Future.")
                continue
            else:
                break
    else:
        month: int = get_month()
    
    if year == datetime.datetime.now().year and month == datetime.datetime.now().month:
        while True:
            day:int = get_day(year, month)
            if day > datetime.datetime.now().day: # checks if the day is in the future
                print('Error: Ivalid Day: Day Cannot be in the Future.')
                continue
            else:
                break
    else:
        day: int = get_day(year, month)
    return datetime.date(year, month, day)

def get_amount() -> float :
    
    while True:
        try:
            amount:float = float(input("Enter the amount of your transaction: "))
            if amount > 0: # input validation
                return amount # loop will break and return amount of transaction as integer.
            else:
                print("Error: Invalid amount, Amount must be larger than 0") 
        except ValueError:
            print("Error: Invalid amount, Amount must be a number")

def get_type() -> str :

    types:tuple[str, str] = ("income", "expense") # a transaction can only have one type and it must be in this tuple.

    while True:
        transaction_type:str = input("Enter the type of your transaction (Income or Expense): ").lower() # all inputs will be lowercase.
        if transaction_type in types: #input validation
            return transaction_type
        else:
            print("Error: Invalid transaction, TransactionType must be either Income or Expense")

def get_transaction() -> tuple[str, dict] :
    # code from line 150 - 156 were altered based on test results. see Test Plan 02 - Case 03 for more details.
    while True:
        category:str = input("Enter the category of your transaction (example: Salary, Groceries): ").lower() # all inputs will be lowerg
        if category == "":
            print("Error: category must not be empty")
        else:
            break

    amount:float = get_amount()
    transaction_type:str = get_type()
    date:datetime.date = get_date() # here we get a datetime.date object.

    transaction:dict[str:dict] = {category: {'type':transaction_type, 'transactions':[{'amount':amount, 'date': date}]}}

    return category, transaction

def get_option_choice(options_list:list[int, str]) -> int: # gets input for chosen option.

    print(tabulate(options_list, headers=["No.", "Option Description"])) 
    while True:
        try:
            choice:int = int(input("\nEnter the option number to select option: "))
            if choice in range(1, len(options_list)+1, 1): # check if choice is a valid option number.
                return choice # return the chosen option and break out of the loop
            else:
                print("Error: Option is not an available option, please select another option")
            pass
        except ValueError: # if the dude enteres a str this lil dude will catch it.
            print("Error: Input for option number must be a valid option number")

def get_sorted_transactions(transactions_to_sort:dict[str:dict]) -> dict[str:dict]: # sorts the transactions by date.
    
    sorted_transactions:dict = {} # initialise new dict to store sorted transactions.
        
    for category, details in transactions_to_sort.items():
        sorted_transactions[category] = { 
            'type': details['type'],
            'transactions': sorted(details['transactions'], key=lambda transaction: transaction['date'])
        } #assigns the with datils with the same key to new dict. And sorts the transactions.

    return sorted_transactions

def add_transaction_count(transactions_dict: dict[str, dict]) -> dict:

    '''
    Adds transaction numbers to the transactions in each category.

    args: transactions_dict: A dictionary containing transaction details.

    Returns: A dictionary with transaction numbers added to each transaction.
    '''

    sorted_transactions: dict[str, dict] = get_sorted_transactions(transactions_dict)
    transactions_with_count: dict[str, dict] = {} # Initialize a new dictionary to store transactions with counts

    for category in sorted_transactions:
        count: int = 0 # initialize count
        # create a mirrored transaction dict to store transactions with transaction nums
        transactions_with_count[category] = {'type': sorted_transactions[category]['type'], 'transactions': []}

        for transaction in sorted_transactions[category]['transactions']:
            count += 1
            # Add transaction number to each transaction
            transactions_with_count[category]['transactions'].append({
                'transaction num': count,
                'amount': transaction['amount'],
                'date': transaction['date']
            })

    return transactions_with_count

def get_by_date(transactions_dict: dict[str: dict]) -> dict[str: dict]:
    date = get_date()
    filtered_transactions_dict = {}

    for category, transaction_data in transactions_dict.items():
        filtered_transactions = [transaction for transaction in transaction_data['transactions'] if transaction['date'] == date]
        if filtered_transactions:
            filtered_transaction_data = {'type': transaction_data['type'], 'transactions': filtered_transactions}
            filtered_transactions_dict[category] = filtered_transaction_data

    return filtered_transactions_dict

def get_by_type(transactions_dict:dict[str:dict]) -> dict[str:dict]:

    transaction_type:str = get_type()
    transactions_by_type:dict = {}
    for category in transactions_dict:
        if transactions_dict[category]['type'] == transaction_type: # if the transaction type is same add it the new dict with a new key.
            transactions_by_type[category] = transactions_dict[category]

    return transactions_by_type


'''
Author : Palihawadana A. A. N. Perera
IIT ID : 20232667
UoW ID : 20822596

project: SD 1 CW part B for year 23/24

'''

'''
Module: print functions
-----------------------

functions:
    1. print_transactions(transactions_to_print) ------- : Prints the transactions dict passed as args.
    2. peint_with_count(transactions_to_print) --------- : prints the transactions dict passed as args with a count
    3. print_by_date(transactions_dict) ----------------- : prints the transactions dict passed as args based on matching date.
    4. print_by_year(transactions_dict) ----------------- : prints the transactions dict passed as args based on matching year.
    5. print_by_month(transactions_dict) ---------------- : prints the transactions dict passed as args based on matching month.
    6. print_by_type(transactions_dict) ----------------- : prints the transactions dict passed as args based on matching type. 

'''         

def print_transactions(transactions_dict: dict[str:dict]):
    
    '''
    args   : transactions_to_print: dict
    process     : prints the trasactions in the args dict formated as a table.
    returns     : None
    
    '''
    transactions_dict = get_sorted_transactions(transactions_dict)

    if len(transactions_dict) == 0: # check if the transactions dict is empty.
        print("No transactions to display.") 
    else:
        for category in transactions_dict: # for each category of transactions
            transactions_to_print: list[list[float, datetime.date]] = [] # make an empty list for printing using tabulate
            total = 0 # initialize a running total.
            print(f'\nTransaction Category: {category}\nType: {transactions_dict[category]['type']}') # print the transaction category and type
            for item in transactions_dict[category]['transactions']:
                transactions_to_print.append([item['amount'], item['date']])
                total += item['amount']
            print(tabulate(transactions_to_print, headers=['Amount (LKR)', 'Date'], floatfmt="<15,.2f", stralign="left"))
            
            if transactions_dict[category]['type'] == 'expense':
                print(f'------------------------------------\nTotal LKR spent on {category}: {total:,.2f}\n')
            else:
                print(f'------------------------------------\nTotal LKR received from {category}: {total:,.2f}\n')

def print_with_count(transactions_list:dict[str:dict]):

    transactions_to_print:dict[str:dict] = add_transaction_count(transactions_list)
    
    if len(transactions_to_print) == 0:
        print("No transactions to display.") 
    else:
        for element in transactions_to_print: # for each category of transactions
            printable_transactions: list[list[int, float, datetime.date]] = [] # make an empty list for printing using tabulate

            print(f'\nTransaction: {element}\nType: {transactions_to_print[element]['type']}') # print the transaction category and type
            for transaction in transactions_to_print[element]['transactions']:
                printable_transactions.append([transaction['transaction num'], transaction['amount'], transaction['date']])
            print(tabulate(printable_transactions, headers=['No.', 'Amount (LKR)', 'Date'], intfmt="<4,d", floatfmt="<15,.2f", stralign="left"), '\n') 

def print_by_date(transactions_dict:dict[str:dict]):

    '''
    perameters  : transactions_dict: dict
    proccess    : gets a date from the user and prints transactions matching said date.
    returns     : None
    '''

    transactions_by_date:dict[str:dict] = get_by_date(transactions_dict)# matches the date of the transaction with the date provided by the user
    print_transactions(transactions_by_date)

def print_by_year(transactions_dict:dict[str:dict]):

    '''
    perameters  : transactions_dict: dict
    proccess    : gets a year from the user and prints transactions matching said year.
    returns     : None
    '''
    
    year:int = get_year() 

    transactions_by_year:dict[str:dict] = {}

    for category in transactions_dict: # uses the same logic as get_by_date()
        filtered_transactions:list[dict] = []
        for transaction in transactions_dict[category]['transactions']:
            if transaction['date'].year == year:
                filtered_transactions.append(transaction)

        if len(filtered_transactions) > 0: # only if there are transactions matching the year
            transactions_dict[category]['transactions'] = filtered_transactions
            transactions_by_year[category] = transactions_dict[category]

    print_transactions(transactions_by_year)

def print_by_month(transactions_dict:dict[str:dict]):

    '''
    perameters  : transactions_dict: dict
    proccess    : gets a year and month from the user and prints transactions matching said year and month.
    returns     : None
    '''
    
    year:int = get_year()
    month:int = get_month() 

    transactions_by_month:dict[str:dict] = {}

    for category in transactions_dict: # uses the same logic as print_by_year()
        filtered_transactions:list[dict] = []
        for transaction in transactions_dict[category]['transactions']:
            if transaction['date'].year == year and transaction['date'].month == month:
                filtered_transactions.append(transaction)
        
        if len(filtered_transactions) > 0:
            transactions_dict[category]['transactions'] = filtered_transactions
            transactions_by_month[category] = transactions_dict[category]            

    print_transactions(transactions_by_month)

def print_by_type(transactions_dict:dict[str:dict]):

    '''
    args   : transactions_dict: dict
    process     : gets the desired type from the usser and prints all transactions in the paramter list that matches the type of transaction
    return      : None
    '''

    transactions_by_type:dict[str:dict] = get_by_type(transactions_dict)
    print_transactions(transactions_by_type)

'''
Author : Palihawadana A. A. N. Perera
IIT ID : 20232667
UoW ID : 20822596

project: SD 1 CW Part B for year 23/24

'''

'''
Module Name: menu.py or menu functions
-----------------------

functions:
    1. main_menu(transactions_dict) ---------------: houses all main functions of the program and also returns a boolean value for stay_in_menu.
    2. back_to_menu() --------------------------- : return a boolean value for repeat_task.
    3. find_transaction(transactions_dict) ------- : finds transactions and returns a transaction chosen by the user
    4. add_transaction(transactions_dict) -------- : gets a transaction from the user and adds to transactions_dict.
    5. update_transaction(transactions_dict) ----- : updates an already exisisting transaction in transactions_dict
    6. delete_transaction (transactions_dict) ---- : deletes an already exisisting transaction in transactions_dict
    7. view_transactions (transactions_dict) ----- : lets the user view summaries of transactions.

''' 

def main_menu(transactions_dict:dict[str:dict]) -> bool:

    '''
    args        : transactions_dict: dict
    process     : gets the desired option choice from the user and carried out the function.
    return      : boolean value for stay_in_menu
    '''
  
    options_list:list[int, str] = [
        [1, 'Load Bulk Transactions from txt File.'],
        [2, "View Transactions"],
        [3, "Add Transaction"],
        [4, "Update Transaction"],
        [5, "Delete Transaction"],
        [6, "Save and Exit Program"]
    ]

    print("\nMain Menu")
    print("-------------")
    option_choice:int = get_option_choice(options_list) # this gets the option from the user.

    if option_choice == 1:
        read_transactions_from_file('bulk transactions.txt', transactions_dict)
    elif option_choice == 2:
        view_transactions(transactions_dict)
    elif option_choice == 3:
        add_transactions(transactions_dict)
    elif option_choice == 4:
        update_transactions(transactions_dict)
    elif option_choice == 5:
        delete_transactions(transactions_dict)
    elif option_choice == 6:
        stay_in_menu:bool = False # this value will determine if the program needs to be kept running.
        return stay_in_menu
    
def back_to_menu() -> bool:
  
    '''
    args   : None
    process     : determines if the user wants to repeat the process or go back to main menu.
    return      : boolean value --> True: return to main menu, False: repeat task.
    '''
   
    while True:
        try:
            repeat_task:str = input("Do you wish to repeat task (yes/no): ").lower()
            print("\n")
            while repeat_task != "yes" and repeat_task != "no": # while loop for input validation
                print("Error: Invalid response: Response must be Yes or No")
                repeat_task:str = input("Do you wish to repeat task (yes/no): ")
                print('\n')
            
            if repeat_task == "yes": # this value will be referenced by a while loop in the main program to determine if the program should repeat the task or return to main menu
                return False
            else:
                print("Returning to Main Menu")
                return True
        except AttributeError: 
            print("Error: Invalid response: Response must be yes or no")

def get_transaction_info(transactions_dict: dict[str, dict]) -> tuple[bool, str, int]:
   
    '''
    args: transactions_dict (dict): A dictionary containing transaction details.
    process: Get transaction information from the user.
    Returns:
        tuple: A tuple containing three elements:
            - A boolean indicating if the transaction was found.
            - The transaction category: str.
            - The transaction number: int.
    '''

    while True:
        transaction_category:str = input('Enter the Transaction Category (Example: "Groceries"): ').strip().lower()
        if transaction_category == 'none':
            return False, transaction_category, 0  # No transaction category found, return False for transaction_found. # this also breaks out of the function
        elif transaction_category not in transactions_dict:
            print('Error: Transaction Category Chosen is Not Valid. Choose a Category That Exists or Choose "None".')
        else:
            break

    while True:
        transaction_number:str = input("Enter the transaction number of your chosen transaction: ").strip().lower()
        if transaction_number == 'none':
            return False, transaction_category, 0  # No transaction found, return False for transaction_found
        try:
            transaction_number:int = int(transaction_number)
            if 1 <= transaction_number <= len(transactions_dict[transaction_category]['transactions']): # checks of the number is in the valid range
                return True, transaction_category, transaction_number # transaction found, return True for transaction_found
            else:
                print("Error: Transaction number is out of range")
        except ValueError:
            print("Error: Input must be an integer")

def choose_transaction(transactions_dict: dict[str, dict]) -> tuple[bool, str, dict[str:dict]]:

    '''
    Args: transactions_dict (dict): Dictionary containing transaction details.

    Process: Finds transactions for the user to choose from and lets the user select a transaction.

    Returns:
        tuple: A tuple containing three elements:
            - A boolean indicating if the transaction was found.
            - The transaction category: str.
            - A dictionary containing the chosen transaction.
    '''

    options_list = [
        [1, "Find a Transaction using all transactions"],
        [2, "Find a transaction using date"],
        [3, "Find a transaction using type"],
        [4, "Unable To Find Transaction, Exit Task."]
    ]

    option_choice = get_option_choice(options_list)

    if option_choice == 1: # find transactions using all transactions
        print("\nEnter the Transaction Category and the Transaction Number to Choose a Transaction.")
        print("If the transaction you are looking for is not here enter 'None' for any field.")
        transactions_with_count = add_transaction_count(transactions_dict)
        print_with_count(transactions_with_count)


        transaction_found, transaction_category, transaction_num = get_transaction_info(transactions_with_count)

        if transaction_found:
            chosen_transaction:dict[str:dict] = {transaction_category: {'type': transactions_with_count[transaction_category]['type'], 'transactions': [transactions_with_count[transaction_category]['transactions'][transaction_num - 1]]}} # uses the index to find transaction with in the list.
        else:
            chosen_transaction = None
            print("Transaction not found!")

    elif option_choice == 2: # find transaction by date
        transactions_to_choose_from = get_by_date(transactions_dict) # only transaction of that date.
        
        if len(transactions_to_choose_from) == 0:
            transaction_found:bool = False # user was not able to select a transaction
            transaction_category = None
            chosen_transaction = None
            print("No transaction were found for that date, Returning to main menu.")
            return transaction_found, transaction_category, chosen_transaction
    
        else:
            print("\nEnter the Transaction Category and the Transaction Number to Choose a Transaction.")
            print("If the transaction you are looking for is not here enter 'None' for any field.")
            transactions_with_count = add_transaction_count(transactions_to_choose_from)
            print_with_count(transactions_with_count)
            
            transaction_found, transaction_category, transaction_num = get_transaction_info(transactions_with_count)
            
            if transaction_found:
                chosen_transaction:dict[str:dict] = {transaction_category: {'type': transactions_with_count[transaction_category]['type'], 'transactions': [transactions_with_count[transaction_category]['transactions'][transaction_num - 1]]}} # uses the index to find transaction with in the list.
            else:
                chosen_transaction = None
                print("Transaction not found!")

    elif option_choice == 3:
        transactions_to_choose_from:dict = get_by_type(transactions_dict)

        print("\nEnter the Transaction Category and the Transaction Number to Choose a Transaction.")
        print("If the transaction you are looking for is not here enter 'None' for any field.")        
        transactions_with_count = add_transaction_count(transactions_to_choose_from)
        print_with_count(transactions_with_count)
        
        transaction_found, transaction_category, transaction_num = get_transaction_info(transactions_with_count)

        if transaction_found:
            chosen_transaction:dict[str:dict] = {transaction_category: {'type': transactions_with_count[transaction_category]['type'], 'transactions': [transactions_with_count[transaction_category]['transactions'][transaction_num - 1]]}} # uses the index to find transaction with in the list.
        else:
            chosen_transaction = None
            print("Transaction not found!")

    else:
        transaction_found:bool = False # user was not able to select a transaction
        transaction_category = None
        chosen_transaction = None

    if chosen_transaction != None:
        chosen_transaction[transaction_category]['transactions'][0] = {'amount':chosen_transaction[transaction_category]['transactions'][0]['amount'], 'date':chosen_transaction[transaction_category]['transactions'][0]['date']} # removes the transaction number from the transaction dict.
        print('The chosen transaction is:')
        print_transactions(chosen_transaction)
        print('\n')

    return transaction_found, transaction_category, chosen_transaction

def add_transactions(transactions_dict: dict[str, dict]) -> None:
    '''
    Args: transactions_dict (dict): Dictionary containing transaction details.
    Process: Lets the user add a transaction to all transactions.
    Returns: None
    '''
    SUCCESS_MESSAGE = "Transaction Successfully Added."
    print('\nEnter the transaction information to add it to all transactions.')
    while True:
        # Get transaction details from the user
        category, transaction_to_add = get_transaction()

        # Check if the category already exists in transactions_dict
        if category in transactions_dict:
            # Check if the type of the transaction matches the existing type
            if transactions_dict[category]['type'] != transaction_to_add[category]['type']:
                print(f'Error: The Type of this transaction must be {transactions_dict[category]['type']}')
                print('Please re-enter the transaction.')
                continue

            # Check if the transaction already exists in the category
            if transaction_to_add[category]['transactions'][0] in transactions_dict[category]['transactions']:
                print("Error: Transaction already exists.")
            else:
                # Add the transaction to the existing category
                transactions_dict[category]['transactions'].append(transaction_to_add[category]['transactions'][0])
                print(f'{SUCCESS_MESSAGE}\n')
        else:
            # Add a new category and transaction
            transactions_dict[category] = transaction_to_add[category]
            print(f'{SUCCESS_MESSAGE}\n')

        # Check if the user wants to add another transaction
        if back_to_menu() == True:
            break

def update_transactions(transactions_dict:dict[str:dict]) -> None:
    '''
    args        : transactions_dict: list
    process     : Lest the user update an already saved transaction.
    return      : None
    '''    

    if len(transactions_dict) != 0: # incase the user wants to update a transaction that doesn't exist lol.

        return_to_menu = False
        while return_to_menu is False:
            options_list = [
            [1, "Update Amount of Transaction"],
            [2, "Update Date of Transaction"],
            [3, "Update Type of Transaction"],
            [4, "Update Category of Transaction"]
            ]

            print('\nFind a transaction to update.')
            transaction_found, transaction_category, chosen_transaction = choose_transaction(transactions_dict) # return a bool, str and dict[str:dict]
            print('How do you wish to update the transaction?')
           
            if transaction_found: # means the chosen transaction exists in all transactions
           
                option_choice = get_option_choice(options_list)
           
                if option_choice == 1: # update the amount of the transaction
                    new_amount = get_amount()
                    for transaction in transactions_dict[transaction_category]['transactions']: # iterate over the transactions of that category.
                        if transaction == chosen_transaction[transaction_category]['transactions'][0]:
                            transaction['amount'] = new_amount

                    print('Transaction amount updated successfully.')

                elif option_choice == 2: # update the date of the transaction
                    new_date:datetime.date = get_date()
                    for transaction in transactions_dict[transaction_category]['transactions']: # iterate over the transaction for that category.
                        if transaction == chosen_transaction[transaction_category]['transactions'][0]:
                            transaction['date'] = new_date

                    print('Transaction date updated successfully.')

                elif option_choice == 3: # update the type of the transaction
                    new_type:str = get_type()
                    print(f'Warning: Changing the transaction type will affect all transactions in {transaction_category}.')
                    
                    proceed = '' # initialize the variable
                    while proceed not in ['y', 'n']: 
                        proceed = input("Do you want to proceed? (y/n): ").lower()
                        if proceed not in ['y', 'n']:
                            print("Invalid input. Please enter 'y' or 'n'.")

                    if proceed == 'y':
                        transactions_dict[transaction_category]['type'] = new_type
                        print('Transactions updated successfully.')
                    else:
                        print('Action Terminated, Returning to Main Menu.')
                        break
                                    
                elif option_choice == 4: # update the category of the transaction
                                    
                    print(f'Warning: Changing the category will affect all transactions in {transaction_category}.')
                    proceed = '' # initialize the variable
                    while proceed not in ['y', 'n']: 
                        proceed = input("Do you want to proceed? (y/n): ").lower()
                        if proceed not in ['y', 'n']:
                            print("Invalid input. Please enter 'y' or 'n'.")

                    if proceed == 'y':
                        new_category = input('Enter the new category for the transactions: ')

                        if new_category not in transactions_dict:
                            transactions_dict[new_category] = transactions_dict.pop(transaction_category)
                        else: 
                            # Add transactions to an existing category if new_category already exists
                            transactions_dict[new_category]['transactions'].extend(transactions_dict.pop(transaction_category)['transactions'])

                        print('Transactions updated successfully')
                    else:
                        print('Action Terminated, Returning to Main Menu.')

                return_to_menu = back_to_menu() # returns a boolean.
            else:
                print('Unable to find a transaction to update, returning to main menu')
                return_to_menu = True

    else:
        print('Unable to find transactions to update, returning to main menu')

def delete_transactions(transactions_dict: dict[str:dict]) -> None:


    '''
    args        : transactions_dict: list
    process     : Lest the user delete an already saved transaction.
    return      : None
    '''    

    if len(transactions_dict) != 0: # checks if there are any transactions to delete.
        return_to_menu = False
        while return_to_menu == False:
            print("\nFind a Transaction to Update")
            transaction_found, transaction_category, chosen_transaction = choose_transaction(transactions_dict) # the user needs to find a transaction to delete first.
            
            if transaction_found:
                transactions_dict[transaction_category]['transactions'].remove(chosen_transaction[transaction_category]['transactions'][0])
                print("Transaction deleted successfully")
                return_to_menu = back_to_menu()
            else:
                print('No Transactions Found, Returning to Main Menu.')
                return_to_menu = True
    
    else:
        print("No Past Transactions to Delete")
        print("Returning to main menu")       

def view_transactions(transactions_dict):

    '''
    parameter   : transactions_dict: list
    process     : Lest the user view already saved transactions.
    return      : None
    '''    
    return_to_menu = False

    if len(transactions_dict) != 0: # checks if there are any transactions to print
        
        options_list = [
            [1, "View All Transactions"],
            [2, "View Transactions by Type"],
            [3, "View Transactions by year"],
            [4, "View Transactions by month"],
            [5, "View Transactions by date"]
        ]
        print("\nHow Do You Want to View Transaction summaries?")
        option_choice = get_option_choice(options_list)

        while return_to_menu == False:

            if option_choice == 1:
                print_transactions(transactions_dict) 

            elif option_choice == 2:
                print_by_type(transactions_dict)

            elif option_choice == 3:
                print_by_year(transactions_dict)

            elif option_choice == 4:
                print_by_month(transactions_dict)

            else:
                print_by_date(transactions_dict)
            
            return_to_menu = back_to_menu()


    else:
        print("No Transactions to View") 
        print("Returning to main menue")  

def read_transactions_from_file(file_path: str, transactions_dict: dict[str, dict]) -> None:
    """
    Read transaction data from a text file and convert it into a dictionary.

    Args:
    - file_path (str): The path to the text file containing transaction data.
    - transactions_dict (dict): The dictionary to which the transaction data will be added.

    Returns:
    - None
    """

    try:
        print("WARNING: This function will read transactions from a text file and add them to the current database.\n")
        
        print("The file must be in the same directory as the main program, and named 'bulk_transactions.txt' and adhere to the following format:")
        print("Each line represents one transaction and must have the following six elements separated by commas:")
        print("Transaction category, Transaction type (income or expense only), Amount (numeric form), Year (numeric), Month (numeric), Day (numeric)\n")
        
        proceed = input("Do you want to proceed? (y/n): ").lower()
        if proceed != "y":
            print('Action was Cancelled, Returning to Main Menu')
            return
        
        skipped_lines = []  # Initialize list to store line numbers of skipped transactions
        line_count = 0  # Initialize line count

        print('\nLoading all transactions from file: bulk transactions.txt')
        with open(file_path, 'r') as file:
            for line in file:
                line_count += 1  # Increment line count for each line read
                parts = line.strip().split(',') 

                # Check if the transaction has exactly 6 parts :)
                if len(parts) != 6:
                    print(f"Skipped Transaction at line {line_count}: Transaction does not meet the data structure standard.")
                    skipped_lines.append(line_count)
                    continue  # Skip to the next line

                category = parts[0].strip().lower() # convert the category to lowercase and strips spaces.
                transaction_type = parts[1].strip().lower()  # Convert transaction type to lowercase
                
                # Attempt to convert amount to float
                try:
                    amount = float(parts[2].strip())
                except ValueError:
                    print(f"Skipped Transaction at line {line_count}: Amount cannot be converted to float.")
                    skipped_lines.append(line_count)
                    continue  # Skip to the next line
                
                # Attempt to convert year, month, and day to integers
                try:
                    year = int(parts[3].strip())
                    month = int(parts[4].strip())
                    day = int(parts[5].strip())
                except ValueError:
                    print(f"Skipped Transaction at line {line_count}: Year, month, or day cannot be converted to integer values.")
                    skipped_lines.append(line_count)
                    continue  # Skip to the next line
                
                # Check if the transaction date is in the future
                current_date = datetime.date.today()
                transaction_date = datetime.date(year, month, day)
                if transaction_date > current_date:
                    print(f"Skipped Transaction at line {line_count}: Transaction date is in the future.")
                    skipped_lines.append(line_count)
                    continue  # Skip to the next line
                
                # Check if category already exists in transactions_dict
                if category in transactions_dict:
                    if transactions_dict[category]['type'] != transaction_type: # checks to see if the type is valid or not.
                        print(f"Skipped Transaction at line {line_count}: Transaction type does not match existing type for category '{category}'.")
                        skipped_lines.append(line_count)
                        continue  # Skip to the next line
                    transactions_dict[category]['transactions'].append({"amount": amount, "date": transaction_date})
                else:
                    transactions_dict[category] = {"type": transaction_type, "transactions": [{"amount": amount, "date": transaction_date}]}
            
            # im absolutely loving this function!! it is deffinitely my favorite one so far!! :D

        print('\nLoading Complete\n')
        if len(skipped_lines) == 0:
            print('Transactions Loaded Successfully')
        else:
            print('Transactions at the Following Lines Were Not Loaded Successfully:')
            for line in skipped_lines:
                print(line, end=',')
            print('\n')
        print('Returning to Main Menu')


    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e: # catches all other exceptions
        print(f"An error occurred while reading the file: {e}")
