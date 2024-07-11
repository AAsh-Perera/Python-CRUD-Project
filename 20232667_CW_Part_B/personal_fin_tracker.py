'''
Author : Palihawadana A. A. N. Perera
IIT ID : 20232667
UoW ID : 20822596

project: SD 1 CW 1 Part B for year 23/24

'''

'''
Module Name: personal_fin_tracker.py or __main__.py
-----------------------

import as personal_fin_tracker

functions:
    1. load_transaction(all_transactions) ------ : loads all trasactions from a json file and starts program, it also returns a boolean value indicating whether the program started successfully or not.
    2. end_program(all_transactions) ----------- : saves all transactions to a json file and makes a back-up. then ends the program

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

import json
from tabulate import tabulate
import datetime
from Program_functions import all_functions

def load_transactions(all_transactions:dict[str:dict]) -> tuple[dict[str:dict], bool]:

    '''
    parameter   : all_transactions: dict[str:dict]
    process     : loads the dict of transactions into the program as a dict.
    return      : all_transactions: dict, a boolean indicating whether the program was successful or not
    '''     

    try:

        with open('transactions.json', 'r') as transactions_file: # here we open the json file using a context manager, since it is more efficient for this function compared to using the open() function.
            all_transactions = json.load(transactions_file)

        if len(all_transactions) == 0: # checks if there were any transactions saved. 
            print("No past transactions were found")
            print("Program successfully initialized")
            return all_transactions, True # if none, then returns an empty dict as all_transactions. and also retruns a boolean value indicating if the program was successfully initialized.
        
        else:
            # the below code block is referenced from stackoverflow.com (2015)
            # json deserialization 
            for category, data in all_transactions.items():
                for transaction in data['transactions']:
                    transaction['date'] = datetime.datetime.strptime(transaction['date'], '%Y-%m-%d').date()
            print("All transactions loaded successfully.")
            print("Program successfully initialized")
            return all_transactions, True
            
    except json.decoder.JSONDecodeError: # this error means the json file is empty, so we will add an epty dict to it and also return the empty dict as all_transactions.
        
        with open('transactions.json', 'w') as transactions_file:
            json.dump(all_transactions, transactions_file) # serialize the dict to the file.
        
        print("No past transactions were found")
        print("Program successfully initialized")
        return all_transactions, True        

    except FileNotFoundError:
        
        print("Original transaction file not found")
        with open('transactions.json', 'w') as transactions_file: # create a new transaction file.
            json.dump(all_transactions, transactions_file) # serialize the empty dict to the file.
        
        print("New Trasaction file successfully created")
        print("Program succcessfully initialized")
        return all_transactions, True
    
    except: # catches any other exception and returns False indicating there was an error when loading the transactions
        print("An Unknown Error Occured While Initializing. Please Contact Technical Support")
        return all_transactions, False
    

def end_program(all_transactions:dict[str:dict]):

    '''
    parameter   : all_transactions: dict
    process     : saves the finalized transactions to a file, and backs it up as well.
    return      : None
    ''' 
    
    # Convert datetime.date objects to string representations
    # the bellow code block is referenced from stackovreflow.com (2015)
    for category, data in all_transactions.items():
        for transaction in data['transactions']:
            transaction['date'] = transaction['date'].isoformat()

    # serialize the modified transactions
    with open('transactions.json', 'w') as transactions_file:
        json.dump(all_transactions, transactions_file, indent=4) # serialize the the final transaction dict to the file. Note, this overwrites the original transaction file.

    print("\nAll Transactions Saved Successfully")

    with open('b_transactions.json', 'w') as backup_transactions:
        json.dump(all_transactions, backup_transactions, indent=4) # serialize the final transaction dict to the  back-up file.

    print("Program Terminated Successfully")


def main(all_transactions):
    
    try:
        all_transactions, successfully_loaded = load_transactions(all_transactions)

        if successfully_loaded == True: # check if all transactions were successfully loaded
            stay_in_menu = True
            while stay_in_menu == True or stay_in_menu == None: # loop to keep the program running until the user wants to exit
                stay_in_menu = all_functions.main_menu(all_transactions) # if successfully loaded then starts the program.
            end_program(all_transactions)
        
        else:
            print("\nProgram Failed to initialize, please contact technical support")
    
    except KeyboardInterrupt:
        print("\nProgram was interrupted by User")
        end_program(all_transactions)


if __name__ == '__main__':

    all_transactions = {}
    main(all_transactions)