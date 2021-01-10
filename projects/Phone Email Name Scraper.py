#! python3
import re, pyperclip

# Create a regEx object for phone no
phoneRegex = re.compile(r'''
# 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345
(
((\d\d\d)|(\(\d\d\d\)))?    # area code (optional)
(\s|-)                   # first separator
\d\d\d                   # first 3 digits
-                        # separator
\d\d\d\d                 # last 4 digits
(((ext(\.)?\s)|x)         # extension text mode(optional)
(\d{2,5}))?                # extenion number (optional)
) 
''',re.VERBOSE)

# Create a regEx object for email
emailRegex = re.compile(r'''
# some.+_thing@(\d{2,5}))?.com
[a-zA-Z0-9_.+]+                  # name part
@                   # @ symbol 
[a-zA-Z0-9_.+]+                   # domain name

''',re.VERBOSE)

# Get the text off the clipboard
text =  pyperclip.paste()

#TODO : Extract the email/phone
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

#TODO : Copy the extracted email/phone to the clipboard
phoneNumbers=[]
areaCode=[]
for i in extractedPhone:
    phoneNumbers.append(i[0])
    areaCode.append(i[1])
j=0
for n in phoneNumbers:
    print("Area code :"+areaCode[j]+"\tPhone Number : "+n+'\tEmail ID : '+extractedEmail[j])
    j+=1
