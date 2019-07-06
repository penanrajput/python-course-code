import re
import sys
import webbrowser

# text_to_search = input("Enter the URL: ")

text_to_search = sys.argv[1]
pattern = re.compile('\d-\d-\d{6}')
matches = re.findall('\d-\d-\d{6}', text_to_search)

# print(matches)

strip_matches = matches[0].split('-')

j=''
for i in strip_matches:
    j=j+i
    
url = 'https://akamaividz.zee5.com/resources/'+matches[0]+'/list/1242x699/'+j+'_list.jpg'

print('\n\n', url)

webbrowser.open_new(url)