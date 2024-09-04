# Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
import urllib
import os
import urllib.request

try:
    site = urllib.request.urlopen('https://roadmap.sh/python')
except urllib.error.URLError:
    print(f'O site roadmap não está acessível no momento.')
else:
    print('O site roadmap está acessível no momento.')
    
with open('site_content.txt', 'w') as file:
    file.write(site.read().decode('utf-8'))

os.system('notepad site_content.txt')