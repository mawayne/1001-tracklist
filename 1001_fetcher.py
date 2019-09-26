import requests
url = 'https://www.1001tracklists.com/' 
headers = {'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
webpage = requests.get(url, headers=headers)
print webpage.text