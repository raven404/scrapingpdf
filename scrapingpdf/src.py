import re, pyperclip

phoneRegex=re.compile(r'''
    # 629-555-0000,(629) 555-0000, 555-0000, 555-0000 ext 12345,ext. 12345, x12345
    (((\d\d\d)|(\(\d\d\d\)))?   # area code
    (\s|- )                     # seperator
    \d\d\d                      # first 3 digits
    -                           # seperator
    \d\d\d\d                    # last 4 digits
    (((ext(\.)?\s)|x)           # extension (optional)
        (\d{2,5}))?)            

''', re.VERBOSE)

emailRegex=re.compile(r''' 
    # gee.+_12kay@mail_123.com/in/--
    [a-zA-Z0-9_.+]+        #name
    @                      #@
    [a-zA-Z0-9_.+]+        #domain

''', re.VERBOSE)

text=pyperclip.paste()

extractedContact=phoneRegex.findall(text)
Contacts=[]
for contact in extractedContact:
    Contacts.append(contact[0])
'\n'.join(Contacts)

extractedEmail=emailRegex.findall(text)
emailIds=[]
for email in extractedEmail :
    emailIds.append(email)

result='\n'.join(Contacts)+'\n'+'\n'.join(emailIds)
print("No of contacts found : ", len(Contacts))
print("No. of emailIds found :", len(emailIds))
print(result)

pyperclip.copy(result)