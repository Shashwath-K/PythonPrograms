import re
phone_regex=re.compile(r'\+\d{12}')
email_regex=re.compile(r'[A-Za-z0-9._]+@[A-Za-z0-9]+\.[A-Z\a-z]{2,}')
with open('Example.txt','r') as f:
    for line in f:
        matches=phone_regex.findall(line)
        for match in matches:
            print(match)
        matches=email_regex.findall(line)
        for match in matches:
            print(match)
