from bs4 import BeautifulSoup
import sys 

def fetchTable(text):
    soup = BeautifulSoup(text, "lxml")
    tables = soup.findAll('table')
    count = 1
    print len(tables)
    tables = [tables[2]]
    database = {}
    for i in tables :
        for j in i.findAll('tr'):
            for k in j.findAll('td'):
               # print k.getText()
                if count %2 != 0:
                    key = k.getText()
                    count += 1
                else:
                    data = k.getText()
                    database[key] = data
                    count += 1
    print database

if __name__ == '__main__':
    text = sys.stdin.read()
    fetchTable(text)
"""
for row in table.findAll('tr'):
    print row.findAll('td')"""
