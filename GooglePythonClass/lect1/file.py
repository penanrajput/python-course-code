# file.py
import re
def Find(pattern, line):
    matches = re.findall(pattern, line)
    # print(matches)
    i = 0
    for match in matches:
        print(i, '->',match)
        i+=1

line = '''
This is new line123

penanrajput1998@gmail.com
sanjeevkumar@gmail.com
'''
# Find(r'[\w]{4}\d+', line)
Find(r'@gmail\.com', line)
