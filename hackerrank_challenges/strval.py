alphanumeric = alpha = digit = lc = uc = False

s = input()

for i in s:
	if i.isalpha() == True:
		alpha = True
	if i.isdigit() == True:
		digit =  True
	if i.islower() == True:
		lc = True
	if i.isupper() == True:
		uc = True
	if alpha == True and digit == True:
		alphanumeric=True

print(alphanumeric)
print(alpha)
print(digit)
print(lc)
print(uc)