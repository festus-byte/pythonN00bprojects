
# This programme collects an email address from the user and then find out if the user
# has a custom domain name or a popular domain nameCollect an email address from the user and then find out if the user
# has a custom domain name or a popular domain name
import re

# a loop to ensure user inputs a valid email
while True:
	email_str = input("What's your email address:\n> ").strip()
	if "@" in email_str and (email_str.endswith(".com") or email_str.endswith(".org") or email_str.endswith(".gov") or email_str.endswith(".edu") or email_str.endswith(".net")) and email_str[email_str.index("@") + 1] != "." and email_str[
		0] != "@":
		break
	else:
		print("Invalid email...Try again")
        
# using regular expressions to find matches
# I know string slicing can be used in this tiny program but i choose regex for adventure sake

# this first pattern checks for (lowercases, uppercases, digits or . or _ or + or -) followed by @ 
pattern1 = re.compile(r'([a-zA-Z0-9._+-]+)@') 

# this seconcd pattern checks for (lowercases, uppercases, digits or . or _ or + or -) followed 
# . and (com or gov or org or net or edu)
pattern2 = re.compile(r'@([a-zA-Z0-9._+-]+).(com|.gov|org|net|edu)')

#matches1 and matches2 stores the pattern if any exists
matches1 = pattern1.finditer(email_str)
matches2 = pattern2.finditer(email_str)

# iterating through the matches for each pattern found
for match in matches1:
    username = (match.group(1)) # username stores the first group ([a-zA-Z0-9._+-]+) in the pattern as username
for match in matches2:
    domain = (match.group(1)) # domain stores the ([a-zA-Z0-9._+-]+) in the pattern as domain

# checking for popular domains
if domain == "gmail":
    print(f"Hey {username}, your email service is from Google, that's cool")

elif domain == "yahoo":
    print(f"Hey {username}, your email service is from Yahoo, that's cool")


elif domain == "outlook":
    print(f"Hey {username}, your email service is from Outlook, that's cool")

elif domain == "hotmail":
    print(f"Hey {username}, your email service is from Hotmail, that's cool")

else:
    print(f"Hey {username}, looks like you've got your own custom setup at {domain}")