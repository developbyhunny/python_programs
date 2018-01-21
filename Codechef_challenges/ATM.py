withdraw = int(input())
balance = float(input())
if (balance-0.5) > withdraw and withdraw % 5 == 0:
    balance -= (withdraw + 0.50)
print("%.2f" % (balance))
