import bankAccount

acct = bankAccount.BankAccount('Alice') # We create an account for Alice.
acct.deposit(120) # _balance can be affected through deposit()
acct.withdraw(40) # _balance can be affected through withdraw()
# Changing _name or _balance outside of BankAccount is impolite, but allowed:
acct._balance = 1000000000
acct.withdraw(1000)
acct._name = 'Bob' # Now we're modifying Bob's account ledger!
acct.withdraw(1000) # This withdrawal is recorded in BobLedger.txt!