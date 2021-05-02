import re

emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''

# match primer mail
pattern = re.compile(r'[a-zA-Z]+@[a-zA-Z]+\.com')

# match primer y segundo mail
pattern = re.compile(r'[a-zA-Z.]+@[a-zA-Z]+\.(com|edu)')

# match los tres mails
pattern = re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z-]+\.(com|edu|net)')

# match cualquier mail
# 1er range: matches toodoo hasta el simbolo @
# 2do range: matches minusculas, mayusculas, todos los digitos, -
# 3er range: despues del punto, va a matchear minusculas, y mayusculas
pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')

matches = pattern.finditer(emails)

for match in matches:
    print(match)
