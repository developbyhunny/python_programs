import re

def fun(s):
    return bool(re.match(r'([a-z][A-Z][0-9][-_])*@*([a-z][A-Z][0-9])*\.(\w){0,3}', s))
    #return bool(re.match(r'(\w)*@*(\w)*\.(\w){0,3}', s))

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)