import os
from cryptography.fernet import Fernet
from getpass import getpass
import random
import datetime

def CreateAccount():
    user = os.getlogin()
    print('> Welcome new user. Fill in the dettails below with the correct information')
    print()
    first_name = input('> What is your first name: ')
    print()
    last_name = input('> What is your last name: ')
    print()
    date_of_birth = input('> Enter your date of birth(date:month:year): ')
    print()
    email = input('> Enter your email: ')
    print()
    number = input('> Enter your mobile number: ')
    print()
    while True:
        pin = getpass('> Create Password: ')
        print()
        confirm_pin = getpass('> Confirm Password: ')
        print()
        if pin == confirm_pin:
            break
        else:
            print('> Error, pins do not match. Try again!')
            print()

    desktop_list = os.listdir(f'C:/Users/{user}/Desktop')
    if 'THE PROTON BANK' in desktop_list:
        pass
    else:
        os.chdir(f'C:/Users/{user}/Desktop')
        os.mkdir('THE PROTON BANK')
    tpg_list = os.listdir(f'C:/Users/{user}/Desktop/THE PROTON BANK')
    if 'Users' in tpg_list:
        pass
    else:
        os.chdir(f'C:/Users/{user}/Desktop/THE PROTON BANK')
        os.mkdir('Users')
    
    os.chdir(f'C:/Users/{user}/Desktop/THE PROTON BANK/Users')
    folder_name = f'{first_name} _ {last_name}'
    new_user = os.mkdir(folder_name)
    os.chdir(f'C:/Users/{user}/Desktop/THE PROTON BANK/Users/{folder_name}')
    os.mkdir('Database')
    create_key = open(f'C:/Users/{user}/Desktop/THE PROTON BANK/Users/{folder_name}/Database/key.key', 'wb')
    create_pass_file = open(f'C:/Users/{user}/Desktop/THE PROTON BANK/Users/{folder_name}/Database/{first_name}.txt', 'wb')
    
    key = Fernet.generate_key()
    create_key.write(key)

    f = Fernet(key)
    encode_pin = confirm_pin.encode()
    encrypted = f.encrypt(encode_pin)
    create_pass_file.write(encrypted)

    os.chdir(f'C:/Users/{user}/Desktop/THE PROTON BANK/Users/{folder_name}/Database') 
    os.mkdir('Profile')

    name_format = f'{first_name} {last_name}'
    create_name_file = open(f'C:/Users/{user}/Desktop/THE PROTON BANK/Users/{folder_name}/Database/Profile/name.txt', 'w').write(name_format)
    create_email_file = open(f'C:/Users/{user}/Desktop/THE PROTON BANK/Users/{folder_name}/Database/Profile/email.txt', 'w').write(email)
    create_number_file = open(f'C:/Users/{user}/Desktop/THE PROTON BANK/Users/{folder_name}/Database/Profile/number.txt', 'w').write(number)
    create_dob_file = open(f'C:/Users/{user}/Desktop/THE PROTON BANK/Users/{folder_name}/Database/Profile/dob.txt', 'w').write(date_of_birth)

    nums = ['1','2','3','4','5','6','7','8','9']
    final = ''
    while len(final) < 11:
        pick = random.choice(nums)
        final += pick
    
    os.chdir(f'C:/Users/{user}/Desktop/THE PROTON BANK/Users/{folder_name}/Database') 
    os.mkdir('Account Info')
    create_account_num_file = open(f'C:/Users/{user}/Desktop/THE PROTON BANK/Users/{folder_name}/Database/Account Info/acc_num.txt', 'w').write(final)
    create_transaction_history_file = open(f'C:/Users/{user}/Desktop/THE PROTON BANK/Users/{folder_name}/Database/Account Info/transaction history.txt', 'x')
    create_balance_file = open(f'C:/Users/{user}/Desktop/THE PROTON BANK/Users/{folder_name}/Database/Account Info/balance.txt', 'w').write('50 Naira')
    os.chdir(f'C:/Users/{user}/Desktop/THE PROTON BANK/Users/{folder_name}/Database/Account Info') 
    os.mkdir('Transactions')
    print(f'> Account created successfully for {first_name} {last_name}.')
    print()
    print(f'> Your account number is: {final}')
    print()
    print('--> You have been given 50 naira for free as a bonus! Thank you for banking with us.')
    print()

def Balance(f_name, l_name):
    print('--> Your Balance: ')
    print()
    open_balance_file =  open(f'C:/Users/{user}/Desktop/THE PROTON BANK/Users/{f_name} _ {l_name}/Database/Account Info/balance.txt', 'r').read()
    print(f'--> {open_balance_file}')
    print()
    another_operation = input('> Do you want to perform another opperation(y/n): ')
    print()
    if another_operation == 'y':
        start()
    elif another_operation == 'n':
        exit()

def Withdraw(f_name, l_name):
    while True:
        withdraw_amount = input('> How much do you want to withdraw: ')
        print()
        print('---> Processing...')
        print()
        if withdraw_amount == 'cancel':
            print('> Ok.')
            break
        open_balance_file =  open(f'C:/Users/{os.getlogin()}/Desktop/THE PROTON BANK/Users/{f_name} _ {l_name}/Database/Account Info/balance.txt', 'r').read()
        split_naira_amount = int(open_balance_file.split(" ")[0])
        if split_naira_amount < int(withdraw_amount):
            print(f'> You cannot redraw {withdraw_amount} Naira. Your balance is {open_balance_file} Naira. ')
            print()
        else:
            new_balance = split_naira_amount - int(withdraw_amount)
            open_balance_file_for_new_balance =  open(f'C:/Users/{os.getlogin()}/Desktop/THE PROTON BANK/Users/{f_name} _ {l_name}/Database/Account Info/balance.txt', 'a').write(f'{new_balance} Naira')
            print('---> Withdraw successful! Take your cash')
            print()

            x = datetime.datetime.now()
            trans_history = f'-------------------------> \n-----> % Date: {x.strftime("%A, %d %B. %Y")} --> Time: {x.strftime("%I:%M%p")} % \n-----> Manner of transaction: Withdrawal \n-----> Debit: {withdraw_amount} Naira \n-----> Current Account Balance: {new_balance} Naira \n-------------------------> \n\n'
            open_transaction_history_file =  open(f'C:/Users/{os.getlogin()}/Desktop/THE PROTON BANK/Users/{f_name} _ {l_name}/Database/Account Info/transaction history.txt', 'a').write(trans_history)

            create_transaction_file =  open(f'C:/Users/{os.getlogin()}/Desktop/THE PROTON BANK/Users/{f_name} _ {l_name}/Database/Account Info/Transactions/W-DEBIT-{x.strftime("%d-%b-%Y-%I-%M%p")}.txt', 'a').write(trans_history)
            another_operation = input('> Do you want to perform another opperation(y/n): ')
            print()
            if another_operation == 'y':
                start()
            elif another_operation == 'n':
                exit()
            break
            
def Transfer(f_name, l_name):
    user = os.getlogin()
    to_account = input('> To Account(Account Number): ')
    print()
    amount = int(input('> Enter Amount: '))
    print()
    if type(amount) != int:
        print('> Error, amount input must be number digits!')
    else:
        pass
    users_database = os.listdir(f'C:/Users/{user}/Desktop/THE PROTON BANK/Users')
    for i in users_database:
        user_database = open(f'C:/Users/{user}/Desktop/THE PROTON BANK/Users/{i}/Database/Account Info/acc_num.txt').read()
        if user_database == to_account:
            access_user = open(f'C:/Users/{user}/Desktop/THE PROTON BANK/Users/{i}/Database/Account Info/balance.txt', 'r').read().split(" ")[0]
            new_balance = amount + int(access_user)
            change_recipient_balance_due_to_transfer =  open(f'C:/Users/{user}/Desktop/THE PROTON BANK/Users/{i}/Database/Account Info/balance.txt', 'w').write(f'{new_balance} Naira')

            sender_balance = open(f'C:/Users/{user}/Desktop/THE PROTON BANK/Users/{f_name} _ {l_name}/Database/Account Info/balance.txt', 'r').read().split(" ")[0]
            if int(sender_balance) > amount:
                new_sender_balance = int(sender_balance) - amount
                change_sender_balance_due_to_transfer = open(f'C:/Users/{user}/Desktop/THE PROTON BANK/Users/{f_name} _ {l_name}/Database/Account Info/balance.txt', 'w').write(f'{new_sender_balance} Naira')
            else:
                print('> You cannot transfer that sum of money because you do not have up to that in your account!')

            #Transaction History For Recipient
            x = datetime.datetime.now()
            sender_account_number = open(f'C:/Users/{user}/Desktop/THE PROTON BANK/Users/{f_name} _ {l_name}/Database/Account Info/acc_num.txt', 'r').read()
            transfer_history = f'-------------------------> \n-----> % Date: {x.strftime("%A, %d %B. %Y")} --> Time: {x.strftime("%I:%M%p")} % \n-----> Manner of transaction: Credit Transfer \n-----> Transfer From: {sender_account_number} - Account Name: {f_name} {l_name} \n-----> Credit: {amount} Naira \n-----> Current Account Balance: {new_balance} Naira \n-------------------------> \n\n'
            add_transation_to_sender_transaction_file = open(f'C:/Users/{user}/Desktop/THE PROTON BANK/Users/{i}/Database/Account Info/transaction history.txt', 'a').write(transfer_history)
            create_transaction_file =  open(f'C:/Users/{os.getlogin()}/Desktop/THE PROTON BANK/Users/{i}/Database/Account Info/Transactions/T-CREDIT-{x.strftime("%d-%b-%Y-%I-%M%p")}.txt', 'w').write(transfer_history)

            #Transaction History For Sender
            x = datetime.datetime.now()
            transfer_history = f'-------------------------> \n-----> % Date: {x.strftime("%A, %d %B. %Y")} --> Time: {x.strftime("%I:%M%p")} % \n-----> Manner of transaction: Debit Transfer \n-----> Debit: {amount} Naira \n-----> Current Account Balancet: {new_sender_balance} Naira \n-------------------------> \n\n'
            add_transation_to_transaction_file = open(f'C:/Users/{user}/Desktop/THE PROTON BANK/Users/{f_name} _ {l_name}/Database/Account Info/transaction history.txt', 'a').write(transfer_history)
            create_transaction_file =  open(f'C:/Users/{os.getlogin()}/Desktop/THE PROTON BANK/Users/{f_name} _ {l_name}/Database/Account Info/Transactions/T-DEBIT-{x.strftime("%d-%b-%Y-%I-%M%p")}.txt', 'w').write(transfer_history)

            print(f'---> {amount} Naira Transfered to {to_account} successfully!')
            print()
          
            another_operation = input('> Do you want to perform another opperation(y/n): ')
            print()
            if another_operation == 'y':
                start()
            elif another_operation == 'n':
                exit()
def TransactionHistory(f_name, l_name):
    size = os.path.getsize(f'C:/Users/{user}/Desktop/THE PROTON BANK/Users/{f_name} _ {l_name}/Database/Account Info/transaction history.txt')
    if size == 0:
        print('> No Transactions have taken place')
        print()
    else:
        transaction_files = os.listdir(f'C:/Users/{user}/Desktop/THE PROTON BANK/Users/{f_name} _ {l_name}/Database/Account Info/Transactions')
        for j in transaction_files:
            read_each = open(f'C:/Users/{user}/Desktop/THE PROTON BANK/Users/{f_name} _ {l_name}/Database/Account Info/Transactions/{j}', 'r').read()
            split_point = j.split(".")
            print(f'<===== {split_point[0]} =====>')
            print()
            print(f'{read_each}')
            print()
    
    another_operation = input('> Do you want to perform another opperation(y/n): ')
    print()
    if another_operation == 'y':
            start()
    elif another_operation == 'n':
            exit()

user = os.getlogin()
print('> Welcome to The Proton ATM')
print()

desktop_list = os.listdir(f'C:/Users/{user}/Desktop')
if 'THE PROTON BANK' not in desktop_list:
    CreateAccount()
else:
    pass

create_new = input('> Create new account?(y/n): ')
print()
if create_new == 'y':
    CreateAccount()
elif create_new == 'n':
    pass

i = 0
while i < 3:
    print('> Login')
    print()
    f_name = input('> Enter First Name: ')
    print()
    l_name = input('> Enter Last Name: ')
    print()
    password = getpass('> Enter Password: ')
    print()
    users = os.listdir(f'C:/Users/{user}/Desktop/THE PROTON BANK/Users')
    if f'{f_name} _ {l_name}' in users:
        password_file =  open(f'C:/Users/{user}/Desktop/THE PROTON BANK/Users/{f_name} _ {l_name}/Database/{f_name}.txt', 'rb').read()
        key = create_key = open(f'C:/Users/{user}/Desktop/THE PROTON BANK/Users/{f_name} _ {l_name}/Database/key.key', 'rb').read()
        f = Fernet(key)
        decrypted = f.decrypt(password_file)
        decoded = decrypted.decode()
        if decoded == password:
            print(f'--> Welcome {f_name}')
            print()
            break
        else:
            print('> Error, wrong password was entered. Try again!')
            i+=1
            print(f'--> You have {3-i} more trys')
            if i == 3:
                print('> Suspicious activity detected. Goodbye.')
                exit()
    else:
        print(f'> User "{f_name} {l_name}" does not exist')
        print()
        while True:
            create_new = input(f'> Would you like to create an account for "{f_name} {l_name}" (y/n): ')
            print()
            if create_new == 'y':
                CreateAccount()
                break
            elif create_new == 'n':
                print('> Ok. Good day')
                print()
                break
            else:
                print('> Invalid input!')
def start():
    while True:    
        print('Operations: ')
        print()
        print('1. Withdraw')
        print()
        print('2. Transfer Money')
        print()
        print('3. Check Account Balance')
        print()
        print('4. Transaction History')
        print()
        print('5. Enter 5 to exit')
        print()
        which_opp = input('> How may i help you today: ')
        print()
        if which_opp == '1':
            Withdraw(f_name, l_name)
        elif which_opp == '2':
            Transfer(f_name, l_name)
        elif which_opp == '3':
            Balance(f_name, l_name)
        elif which_opp == '4':
            TransactionHistory(f_name, l_name)
        elif which_opp == '5':
            exit()
        else: 
            print('> Invalid Input')
            print()
start()