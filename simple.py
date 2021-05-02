import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

cat
mat
pat
bat
'''

sentence = 'Start a sentence and then bring it to an end'

pattern = re.compile(r'start', re.I)

matches = pattern.search(sentence)

print(matches)



# RAW string is: string prefix with, not to handle slashes in special way
# esto va a printear una tabulacion |	Tab
print('\tTab')
# will not handle in any special way
# esto va a printear simplemente un texto tab => \tTab
print(r'\tTab')


pattern = re.compile(r'abc')  # abc on text
pattern = re.compile(r'cba')  # cba on text => will print not matches
pattern = re.compile(r'\.') # scape all of this meta characters . ^ $ * + ? { } [ ] \ | ( )
pattern = re.compile(r'.')  # match all characters except the new lines
pattern = re.compile(r'\d')  # math all digits between 0-9
pattern = re.compile(r'\D')  # math all non digits
pattern = re.compile(r'\w')  # math all lower case letters, uppercase letters, digits and underscores
pattern = re.compile(r'\W')  # math all not lower case letters, uppercase letters, digits and underscores
pattern = re.compile(r'\s')  # math all spaces, new lines, tabs
pattern = re.compile(r'\S')  # math all not spaces, new lines, tabs

# anchors:
pattern = re.compile(r'\b') # word boundary: invisible position between. whitespace or not alphanumeric
pattern = re.compile(r'\bHa')
# result 2 Ha ==> .Ha .Ha{Ha}

pattern = re.compile(r'\B') # not word boundary: invisible position between. whitespace or not alphanumeric
pattern = re.compile(r'\bHa')
# result 1 Ha ==> {Ha Ha}.Ha

pattern = re.compile(r'\^') # beginning of a string
sentence = "_Start a sentence and then bring it to an end"
pattern = re.compile(r'^Start') # no encontrara un Start ya que empieza _Start
matches = pattern.finditer(sentence)
pattern = re.compile(r'\$') end of a string
pattern = re.compile(r'end$') # encontrara el string end => final de la sentencia
matches = pattern.finditer(sentence)

# for example for any url
pattern = re.compile(r'coreyms\.com') # have to scape the dot.com

# match phone numbers:
pattern = re.compile(r'\d\d\d') # three digits to match all of them

# match phone numbers:
pattern = re.compile(r'\d\d\d.') # three digits to match all of them and dot to match every character

# match phone numbers:
pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d') # three digits to match all of them and dot to match every character

# add a new number that uses: 123*555*1234
# lets match ones with dashes or dots
pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d') no need to scape character sets

# match only 800/900 phone number
pattern = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d')

# match numbers from 1 to 5
pattern = re.compile(r'[1-5]') # match range from 1 to 5
pattern = re.compile(r'[a-z]') # match range from a to z on lowercase
pattern = re.compile(r'[a-zA-Z]') # match range from a to z on lowercase and uppercase
pattern = re.compile(r'[^a-zA-Z]') # in set will negate the set. Everything is not in character set
pattern = re.compile(r'[^b]at') # in set will negate the set. Everything is not in character set

# quantifiers
# {3} - Exact Number
pattern = re.compile(r'\d{3}.\d{3}.\d{4}')

# matching names Mr.
pattern = re.compile(r'Mr\.?\s[A-Z]\w*')

# matching all names - create a group ()
pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z\w*]')
pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z\w*]')

# lets try to open data txt.
# and test the different regular expressions
with open('data.txt', 'r', encoding='utf-8') as f:
    contents = f.read()
    matches = pattern.finditer(contents)

    for match in matches:
        print(match)

# python re module
# findall => return mathicng as list of string,
# if thre are groups will match the groups only
matches = pattern.findall(contents)

# match => return the first match, does not return an array Match Object / none
matches = pattern.match(contents)

# search => return the first match, does not return an array Match Object / none
matches = pattern.search(contents)

# using flags, in this case will ignore upper than lower
re.compile(r'_start', re.IGNORECASE)
