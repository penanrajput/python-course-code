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
'''

sentence = 'Start start a sentence and then bring it to an end'

data = open("data.txt", 'r')
text = data.read()
pattern = re.compile('\w\d\d-\d\d\d-\d\d\d\d')


# matches = pattern.finditer(text_to_search)
matches = pattern.finditer(text)

for match in matches:
    print(match)
