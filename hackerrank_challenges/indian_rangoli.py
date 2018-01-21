#--------e--------
#------e-d-e------
#----e-d-c-d-e----
#--e-d-c-b-c-d-e--
#e-d-c-b-a-b-c-d-e
#--e-d-c-b-c-d-e--
#----e-d-c-d-e----
#------e-d-e------
#--------e--------

n = 5

for _ in range(n+2):

    for a1 in range(n, 0, -1):
        print(a1, end='')
    print()
