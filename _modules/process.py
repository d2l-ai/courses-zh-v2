from bs4 import BeautifulSoup
import requests

import glob
import re

url_re = r'(https?\:\/\/[a-zA-Z0-9\.\/\?\:@\-_=#%]+)'
head = r'^([ \:]+)'
for file in glob.glob('part*.md'):
    with open(file) as f:
        lines = f.readlines()

    for i, l in enumerate(lines):
        res = re.match(head, l)
        if not res: continue
        h = res.group()
        urls = re.findall(url_re, l)
        if not urls: continue
        assert len(urls) == 1, 'Found more than one URL in ' + l
        url = urls[0]
        if url.endswith('html') and not '[' in l:
            page = requests.get(url)
            if not page.ok: continue
            soup = BeautifulSoup(page.content, features="lxml")
            a = soup.find('h1')
            if not a: continue
            title = a.text
            if a.find('a'): title = title.replace(a.find('a').text, '')
            if a.find('span'): title = title.replace(a.find('span').text, '')
            lines[i] = f'{h}[{title}]({url})\n'
        elif 'bilibili' in url:
            url = url.split('?')[0]
            lines[i] = f'{h}[<i class="fas fa-video"></i>]({url})\n'
        elif '.ipynb' in url and 'nbviewer.jupyter.org' not in url:
            url = 'https://nbviewer.jupyter.org/format/slides/url/' \
                + url.replace('http://', '').replace('https://', '')
            lines[i] = f'{h}[<i class="fas fa-code"></i>]({url})\n'
        elif url.endswith('pdf'):
            lines[i] = f'{h}[<i class="fas fa-file-powerpoint"></i>]({url})\n'

    with open(file, 'w') as f:
        f.writelines(lines)