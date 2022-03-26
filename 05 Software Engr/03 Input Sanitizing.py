import re   # regular expression

# regular expressions are used for finding patterns

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

def validate(email):
    if re.fullmatch(regex, email):
        print(f"{email} is a valid email")
    else:
        print(f"{email} is not a valid email")

validate("coriell@latech.edu")
validate("coriell@email.latech.edu")