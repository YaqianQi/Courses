"""
Implement methods 
Input 
DEPOSIT name sum − deposit amount sum to name's account. If the client does not have an account, the account is created.
WITHDRAW name sum − withdraw amount sum from name's account. If the client does not have an account, the account is created.
BALANCE name − find out the balance of the client name.
TRANSFER name1 name2 sum − transfer amount sum from name1's account to name2's account. 
                         If any of the clients does not have an account, an account is created for them.

INCOME p − charge p% of the account's amount for all clients with open accounts. 
        Interest is charged only to clients with a positive account balance, if the client has a negative balance,
        his balance does not change. After interest is accrued, the amount in the account remains integer,
        i.e. only an integer number of monetary units is accrued. 
        he fractional part of the accrued interest is discarded

Output format: For each BALANCE request, the program must print the account balance of that customer. 
If the client with the requested name does not have a bank account, print ERROR.
"""
lst = []
bank_details = {}
while True:
    input_str = input()
    if input_str == '':
        break
    lst.append(input_str)
for i in range(len(lst)):
    input_str = lst[i]
    if input_str.split()[0] == "DEPOSIT":
        name = input_str.split()[1]
        cf = int(input_str.split()[2])
        bank_details[name]= bank_details.setdefault(name, 0) + cf


    if input_str.split()[0] == 'INCOME':
        rate = int(input_str.split()[1])
        for k, v in bank_details.items():
            if v >= 0:
                bank_details[k] = int((1 + rate/100) * v)

    if input_str.split()[0] == 'TRANSFER':
        from_name = input_str.split()[1]
        to_name = input_str.split()[2]
        cf = int(input_str.split()[3])
        from_person_bal = bank_details.setdefault(from_name, 0) - cf
        to_person_bal = bank_details.setdefault(to_name, 0) + cf
        bank_details[from_name] = from_person_bal
        bank_details[to_name] = to_person_bal

    if input_str.split()[0] == 'WITHDRAW':
        name = input_str.split()[1]
        cf = int(input_str.split()[2])
        bank_details[name] = bank_details.setdefault(name, 0) - cf
    if input_str.split()[0] == "BALANCE":
        name = input_str.split()[1]
        if name in bank_details:
            print(bank_details.get(name))
        else:
            print("ERROR")
"""

Input data:
DEPOSIT Ivanov 100  Ivanov: 100 
INCOME 5            Ivanaov: 100 * 1.05
BALANCE Ivanov      105 
TRANSFER Ivanov Petrov 50   Ivanov: 50 Petrov: 50 
WITHDRAW Petrov 100         Petrove: -50 
BALANCE Petrov              -50 
BALANCE Sidorov             Error 


Program output:
105
-50
ERROR
"""