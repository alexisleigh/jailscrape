#invites two external libraries, "requests" and "mechanize" to the party
import requests, mechanize
#invites a tool called "BeautifulSoup" from an external library called "bs4" to the party
from bs4 import BeautifulSoup
#creates a variable called "url"
url = 'https://report.boonecountymo.org/mrcjava/servlet/SH01_MP.I00290s?max_rows=500'
#creates a variable called "br" that involves an object called "mechanize" and a method called "Browser"
br = mechanize.Browser()
#passes the method "open" over the argument url
br.open(url)
#applies the methods "response" and "read" to the br variable, and calls the resulting variable html
html = br.response().read()
#creates a variable called "soup," the result of applying the external tool BeautifulSoup to the variable "html" and parsing the "html" variable
soup = BeautifulSoup(html, "html.parser")
#creates a variable called "main_table," the result of passing the mthod "find" over two arguments — "tbody," or the html abbreviation for table body, and 'id': 'mrc_main_table', also an html label. 
main_table = soup.find('tbody',
    {'id': 'mrc_main_table'}
)
#creates a variable called row_list, the result of passing the find_all method (focusing on the 'tr' or 'table row' argument) over the object 'main_table'
row_list = main_table.find_all('tr')
#runs a loop over each letter in row_list...
for r in row_list:
#creates a variable called "cell_list", the result of passing the find_all method (focusing on the 'td' or 'table data' argument) over the object r (aka each letter in row_list)...
    cell_list = r.find_all('td')
#if data actually exists, as in if the length of cell_list is greater than 0...
    if len(cell_list) > 0:
        #For every letter in cell_list...
        for c in cell_list:
            #print a stripped version of the text (aka delete the spaces before and after the entry)
            print c.text.strip()
#print '---------'
        print '----------'
#print 'IT WORKED!' and give yourself a pat on the back
print 'IT WORKED!'