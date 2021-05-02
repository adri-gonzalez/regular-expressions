import re

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

# math any url domains:
# s? => makes that s optional
# (www\.)? => make this group optional
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')


# replace urls
# substitute this urls to groups, like slice or strip
subbed_urls = pattern.sub(r'\2\3', urls)
print(subbed_urls)

# lets get the groups within url
for match in matches:
    print(match.group(1))
    print(match.group(2))
    print(match.group(3))
