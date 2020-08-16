while True:
    balance=10000
    print("  ATM  ")
    print("""
    1-  Balance
    2-  Withdraw
    3-  Deposit
    4-  Quit
    """)
    try:
        option=int(input("enter option:"))
    except Exception as e:
        print("Error",e)
        print("Enter 1,2,3,4 only")
        continue
    if option==1:
        print("Bal=",balance)
    if option==2:
        print("Bal=",balance)
        Withdraw=float(input("Enter withdraw amount "))
        if Withdraw>0:
            forewardbalance=(balance-Withdraw)
            print("balance =",forewardbalance)
        elif Withdraw>balance:
            print("Low balance")
        else:
            print("no withdraw made")
    if option==3:
         print("Bal=",balance)
         Deposit=float(input("Enter deposit amount "))
         if Deposit>0:
             forewardbalance=(balance+Deposit)
             print("balance =",forewardbalance)
    if option==4:
        exit()
