import requests
from getTableData import fetchTable as f
postUrl = "https://ipuresult.com/index.php"

session = requests.Session()
#roll = 
data = {'Roll_No': '00696302713'}
response = session.post(postUrl, data=data)
cookie = session.cookies.get_dict()
print cookie
#ch = raw_input()
ch = 'y'
if ch == 'y':
    url = "https://ipuresult.com/overview.php"
    temp = session.get(url, cookies=cookie)
    text = temp.content
    f(text)
